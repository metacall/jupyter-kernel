import subprocess
import tempfile
import re
import sys
import os
import json
import logging
import sqlite3
import traceback
import nest_asyncio
from traitlets import List
from ipykernel.kernelbase import Kernel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

HISTORY_DB = None
nest_asyncio.apply()


class metacall_jupyter(Kernel):
    """
    Defines the Jupyter Kernel declaration for MetaCall Core
    """

    implementation = "Jupyter Kernel for MetaCall Core"
    implementation_version = "0.1"
    language = "MetaCall Core"
    language_version = "0.4.12"
    language_info = {
        "name": "MetaCall Core",
        "mimetype": "text/plain",
        "file_extension": ".txt",
    }
    banner = "Wrapper Kernel for MetaCall Core Library leveraging IPython and Jupyter"
    help_links = List(
        [
            {
                "text": "MetaCall Core",
                "url": "https://github.com/metacall/core",
            },
            {
                "text": "MetaCall Polyglot REPL",
                "url": "https://github.com/metacall/polyglot-repl",
            },
            {
                "text": "MetaCall Jupyter Kernel",
                "url": "https://github.com/metacall/jupyter-kernel",
            },
        ]
    )

    history = {}
    results = {}
    history_db_ready = False

    def __init__(self, **kwargs):
        """init method for the Kernel"""
        Kernel.__init__(self, **kwargs)
        self._start_metacall()

    def _start_metacall(self):
        """
        Starts the MetaCall REPL Subprocess to take user input and execute the user code.
        """
        try:
            self.metacall_subprocess = subprocess.Popen(
                ["metacall", "repl.js"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            self.metacall_subprocess.stdout.readline()
        except Exception as e:  # noqa: F841
            logger.exception("MetaCall Subprocess failed to start")

    def start_history(self):
        """
        Starts the MetaCall Kernel History Database
        """
        db_name = HISTORY_DB
        try:
            self.history_db = sqlite3.connect(db_name)
            c = self.history_db.cursor()
            c.execute(
                "create table if not exists history (session text, execution_count int, code text, result text)"  # noqa: E501
            )
            self.history_db_ready = True
        except:  # noqa: E722
            print(sys.exc_info()[0])
            traceback.print_tb(sys.exc_info()[2])

    def record_history(self, session, count, code, data):
        """
        Record the user code and the result of the user code to the history database.
        """
        try:
            result = data._repr_text_()
            if type(result) == list:
                result = str(result)
            c = self.history_db.cursor()
            c.execute(
                "insert into history values (?,?,?,?)", (session, count, code, result)
            )
            self.history_db.commit()
        except:  # noqa: E722
            print(sys.exc_info()[0])
            traceback.print_tb(sys.exc_info()[2])

    def do_execute(  # noqa: C901
        self, code, silent, store_history=True, user_expressions=None, allow_stdin=False
    ):
        """
        Executes the User Code

        Parameters:
            code: The code to be executed
            silent: Whether to display output
            store_history:  Whether to record this code in history and increase the execution count
            user_expressions: Mapping of names to expressions to evaluate after the code has run
            allow_stdin: Whether the frontend can provide input on request

        Returns:
            send_response: Sends the execution result
        """

        if store_history:
            self.history[self.execution_count] = code

        if not silent:
            try:

                def error_message(code):
                    """Highlights the error message in red color"""
                    code = "\033[0;31m" + code + "\033[0m"
                    return code

                def newfile_magic(code):
                    """
                    Function to save a new file using the `$newfile` magic.

                    Parameters:
                        code: The code to be executed

                    Returns:
                        A success message once the file has been saved
                    """

                    code = code + "\n"
                    magic_argument = code.split("\n")[0]
                    file_name = magic_argument.lstrip("$newfile ")
                    file_input = code.split("\n", 1)[1]
                    with open(file_name, "a", encoding="utf-8") as file:
                        file.write(file_input)
                    return "File " + file_name + " is saved."

                def metacall_repl(code):
                    """
                    Function to execute the user code and return the result
                    through MetaCall subprocess.

                    Parameters:
                        code: The code to be executed

                    Returns:
                        result: The result of the execution
                    """
                    code = code.lstrip() + "\n"
                    arr = bytes(code, "utf-8")
                    self.metacall_subprocess.stdin.write(arr)
                    self.metacall_subprocess.stdin.flush()
                    output = self.metacall_subprocess.stdout.readline()
                    return output

                def metacall_loadcell(code, extension):
                    """
                    Loads a function on MetaCall's REPL subprocess enabling cross-language
                    function calls.

                    Parameters:
                        code: Code to executed by the MetaCall subprocess
                        extension: The extension of the code to create a temporary file from

                    Returns:
                        logger_output: The log output generated by the subprocess
                                       after a successful save and load.
                    """
                    with tempfile.NamedTemporaryFile(suffix=extension, dir="") as temp:
                        temp.write(code.encode())
                        temp.flush()
                        filename = str(temp.name)[1:]
                        filepath, filename = os.path.split(filename)
                        code = "%load " + extension[1:] + " " + filename
                        code = code.lstrip() + "\n"
                        code_bytes = bytes(code, "utf-8")
                        self.metacall_subprocess.stdin.write(code_bytes)
                        self.metacall_subprocess.stdin.flush()
                        self.metacall_subprocess.stdout.readline()
                        return "The code has been successfully loaded on Kernel"

                def loadcell_extension(code):
                    """
                    Parses the code to extract the code and file extension from the user input.

                    Parameters:
                        code: User input consisting the code and file extension

                    Returns:
                        code: The code to be saved in the temporary file.
                        extension: The temporary file extension.
                    """
                    code = code + "\n"
                    magic_argument = code.split("\n")[0]
                    extension = magic_argument.lstrip("$loadcell ")
                    code = code.split("\n", 1)[1]
                    extension = "." + extension
                    return code, extension

                def byte_to_string(code):
                    """Function to convert the result of the execution to string"""
                    return code.decode("UTF-8")

                def split_magics(code):
                    """
                    Grabs the langage name passed in the magic and returns the magic and the code

                    Parameters:
                        code: Code to be parsed from and the magic extracted

                    Returns:
                        magics: The Language Name passed through Magic
                        code: The parsed code with the magic extracted from the same
                    """
                    code_lines = []
                    magics = []
                    lines = code.split("\n")

                    state = "magics"
                    for line in lines:
                        if state == "magics":
                            if line.startswith(">"):
                                magics.append(line.lstrip(">"))
                                continue
                            elif not line:
                                continue
                        state = "code"
                        code_lines.append(line)
                    return (magics, "\n".join(code_lines))

                def metacall_execute(code, extension):
                    """
                    Executes the Code passed by creating a temporary file
                    using a MetaCall Subprocess

                    Parameters:
                        code: Code to executed by the MetaCall subprocess
                        extension: The extension of the code to create a temporary file from

                    Returns:
                        logger_output: The log output generated by the subprocess
                                       after a successful execution
                    """
                    with tempfile.NamedTemporaryFile(suffix=extension) as temp:
                        temp.write(code.encode())
                        temp.flush()
                        result = subprocess.Popen(
                            ["metacall", str(temp.name)],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                        )
                        stdout_value, stderr_value = result.communicate()
                        std_output = repr(stdout_value)
                        std_error = repr(stderr_value)
                        full_output = std_output + "\n" + std_error
                        exact_output = full_output[2:-5]
                        split_output = exact_output.split("\\n")
                        logger_output = ""
                        for item in split_output:
                            logger_output += item + "\n"

                    temp.close()
                    return logger_output

                def shell_execute(code, shcmd):
                    """
                    Executes the Shell Commands using a Subprocess

                    Parameters:
                        code: Shell Command to executed by the subprocess
                        shcmd: Configuration to call Shell Commands

                    Returns:
                        logger_output: The log output generated by the subprocess
                                       after a successful execution
                    """
                    from subprocess import run, PIPE, STDOUT

                    cmd = str(code[len(shcmd):].lstrip())
                    exact_output = run(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
                    if exact_output.returncode == 0:
                        logger_output = exact_output.stdout.decode()
                    else:
                        logger_output = error_message(exact_output.stdout.decode())
                    return logger_output

                def metacall_inspect():
                    """
                    Executes the %inspect on the REPL subprocess to check all loaded functions

                    Returns:
                        inspect: A dictionary showing all available functions across the REPL state
                    """
                    code = "%inspect"
                    code = code.lstrip() + "\n"
                    code_bytes = bytes(code, "utf-8")
                    self.metacall_subprocess.stdin.write(code_bytes)
                    self.metacall_subprocess.stdin.flush()
                    inspect = ""
                    while True:
                        line = self.metacall_subprocess.stdout.readline()
                        inspect = inspect + line.decode("utf-8")
                        if line == b"\n":
                            break
                    return json.loads(inspect)

                def metacall_load(code):
                    """
                    Loads a function through the Kernel on the REPL Subprocess for
                    inter-language function calls

                    Parameters:
                        code: Load command in the format: `%load <tag> <file_0>... <file_N>`
                    """
                    try:
                        code = code.lstrip() + "\n"
                        code_bytes = bytes(code, "utf-8")
                        self.metacall_subprocess.stdin.write(code_bytes)
                        self.metacall_subprocess.stdin.flush()
                        self.metacall_subprocess.stdout.readline()
                        return "The file has been successfully loaded"
                    except:  # noqa: E722
                        return "The file was not loaded onto the Kernel"

                def delete_line_from_string(code):
                    """Delete the Script loading message from the execution"""
                    regex = re.compile(r"Script \(.+\) loaded correctly")
                    match = regex.search(code)
                    if match:
                        code = regex.sub("", code)
                    return code

                def trim_empty_lines(text):
                    """Trim the empty lines from the logger output for better formatting"""

                    text = os.linesep.join([s for s in text.splitlines() if s])
                    return text

                def available_repl():
                    """
                    Function to check for available REPLs on the MetaCall Kernel

                    Returns:
                        available_repl: List of REPLs available on the Kernel
                    """
                    code = byte_to_string(metacall_repl("%available"))
                    lang = code.split(":")[1].lstrip().rstrip()
                    lang = list(lang.split(" "))
                    repl_languages = {
                        "py": "Python: Use `%repl py` to activate",
                        "node": "JavaScript: Use `%repl node` to activate",
                    }
                    available_repl = ""
                    for key, value in repl_languages.items():
                        for i in lang:
                            if key == i:
                                available_repl = available_repl + value + "\n"
                    return available_repl.lstrip()

                extensions = {"python": ".py", "javascript": ".js"}

                (magics, code) = split_magics(code)
                shcmd = "!"
                shutd = "$shutdown"
                newfile = "$newfile"
                inspect_command = "%inspect"
                load_command = "$loadfile"
                help_command = "$help"
                logger_output = ""
                loadcell = "$loadcell"
                available = "$available"

                if code.startswith(help_command):
                    logger_output = (
                        "1. ! : Run a Shell Command on the MetaCall Jupyter Kernel\n"
                        + "2. $shutdown : Shutdown the MetaCall Jupyter Kernel\n"
                        + "3. $inspect : Inspects the MetaCall to check all loaded functions\n"
                        + "4. $loadfile: Loads a file onto the MetaCall which can be evaluated\n"
                        + "5. $newfile: Creates a new file and appends the code mentioned below\n"
                        + "6. %repl <tag>: Switch from different REPL (available tags: node, py)\n"
                        + "7. >lang: Execute scripts using the MetaCall exec by saving them in a "
                        + "temporary file (available languages: python, javascript)\n"
                        + "8. $loadcell <tag>: Loads a function onto the MetaCall to be evaluated\n"
                        + "9. $help: Check all the commands and tags you can use while accessing "
                        + "the MetaCall Kernel\n"
                        + "10. $available: Checks all the available REPLs on the Kernel"
                    )
                elif code.startswith(available):
                    logger_output = available_repl()

                elif code.startswith(loadcell):
                    code, extension = loadcell_extension(code)
                    logger_output = metacall_loadcell(code, extension)

                elif code.startswith(shcmd):
                    logger_output = shell_execute(code, shcmd)

                elif code.startswith(inspect_command):
                    logger_output = json.dumps(metacall_inspect())

                elif code.startswith(load_command):
                    code = code.split(" ", 1)[1]
                    code = "%load " + code
                    logger_output = metacall_load(code)

                elif code.startswith(newfile):
                    logger_output = newfile_magic(code)

                elif code.startswith(shutd):
                    self.do_shutdown(False)

                elif magics:
                    magic_lang = "".join(map(str, magics))
                    magic_lang = magic_lang.lower()
                    if magic_lang in extensions:
                        extension = extensions[magic_lang]
                        logger_output = metacall_execute(code, extension)

                    else:
                        logger_output = (
                            "We don't suppport "
                            + magic_lang
                            + " language, yet.\nPlease try another language or add support for "
                            + magic_lang
                            + " language.\n"
                        )

                else:
                    output = metacall_repl(code)
                    logger_output = byte_to_string(output)

            except Exception as e:
                logger_output = error_message(str(e))

            if store_history:
                self.results[self.execution_count] = logger_output

            self.record_history(
                self.session.session, self.execution_count, code, logger_output
            )

            if "error" in logger_output:
                logger_output = error_message(logger_output)

            stream_content = {
                "name": "stdout",
                "text": trim_empty_lines(delete_line_from_string(logger_output)),
            }
            self.send_response(self.iopub_socket, "stream", stream_content)

        return {
            "status": "ok",
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {},
        }

    def do_history(
        self,
        hist_access_type,
        output,
        raw,
        session=None,
        start=None,
        stop=None,
        n=None,
        pattern=None,
        unique=False,
    ):
        """
        Parameters:
            hist_access_type (str): 'tail' or 'range'
            output (bool): If True, then the history is printed to stdout.
                           Otherwise, it is returned as a string.
            raw (bool): If True, then the history is not formatted in any way.
            session (str): The name of the session.
            start (int): The first execution count from the history to get.
            stop (int): The last execution count from the history to get.
            n (int): The number of executions to get.
            pattern (str): The pattern to search the history with.
            unique (bool): If True, then only unique history items are shown.

        Returns:
            history (str): The history of the session.
        """
        if hist_access_type == "tail":
            hist = self.get_tail(n, raw=raw, output=output, include_latest=True)
        elif hist_access_type == "range":
            hist = self.get_range(session, start, stop, raw=raw, output=output)
        elif hist_access_type == "search":
            hist = self.search(pattern, raw=raw, output=output, n=n, unique=unique)
        else:
            hist = []

        return {"history": list(hist)}

    def get_tail(self, n, raw, output, include_latest):
        """
        Parameters:
            n (int): The number of lines to be fetched
            raw (bool): Whether to include raw_history
            output (bool): Whether to include output
            include_latest (bool): Whether to include the latest

        Returns:
            list: A list of lines
        """
        n = n or self.history.__len__()
        key_range = list(self.history.keys())[-n:]
        result = []
        for key in key_range:
            r = (key + 1, self.history[key], self.results[key]._repr_text_())
            result.append(r)
        return result

    def get_range(self, session, start, stop, raw, output):
        """
        Parameters:
            session: session name
            start: start line number
            stop: stop line number
            raw: True to get the raw input
            output: True to get the formatted output

        Returns:
            result: A list of tuples (source, input, output)
        """
        start = start or 0
        stop = stop or self.history.__len__()
        start = start if start == 0 else start - 1
        key_range = list(self.history.keys())[start:stop]
        result = []
        for key in key_range:
            r = (key + 1, self.history[key], self.results[key]._repr_text_())
            result.append(r)
        return result

    def do_shutdown(self, restart):
        """
        Shuts down the Kernel.

        Parameters:
            restart: Boolean value to determine the kernel is shutdown or restarted

        Returns:
            restart: Boolean value to signal the kernel shutdown
        """
        code = "%exit"
        code = code.lstrip() + "\n"
        arr = bytes(code, "utf-8")
        self.metacall_subprocess.stdin.write(arr)
        self.metacall_subprocess.stdin.flush()
        self.metacall_subprocess.stdout.readline()
        logger_output = "Kernel Shutdown!"
        stream_content = {"name": "stdout", "text": logger_output}
        self.send_response(self.iopub_socket, "stream", stream_content)
        return {"restart": False}
