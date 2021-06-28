import subprocess
import tempfile
import nest_asyncio
from ipykernel.kernelbase import Kernel

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

    def do_execute(
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
        if not silent:
            try:
                with tempfile.NamedTemporaryFile(suffix=".js") as temp:
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

                    def remove_last_line_of_string(code):
                        return "\n".join(code.split("\n")[:-3])

            except Exception as e:
                logger_output = str(e)

            finally:
                temp.close()

            stream_content = {
                "name": "stdout",
                "text": remove_last_line_of_string(logger_output),
            }
            self.send_response(self.iopub_socket, "stream", stream_content)

        return {
            "status": "ok",
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {},
        }
