from ipykernel.kernelbase import Kernel


class metacall_jupyter(Kernel):
    """
    Defines the Jupyter Kernel declaration for MetaCall Core
    """

    implementation = "Jupyter Kernel for MetaCall Core"
    implementation_version = "0.1"
    language = "MetaCall Core"
    language_version = "0.4.0"
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
            """
            TODO:

            This is the initial skeleton right here. The next step here would be to
            directly run a subprocess to load a Python script from a Jupyter UI and
            execute it using MetaCall. Right now, I have ran into a problem with the
            MetaCall installation which I would be hopefully fixing using Docker to
            ensure that the skeleton can atleast take up a Python script from the
            Jupyter UI and execute it with a rich logger output.

            The next steps would be simple: I will make use of Python magics to ask the
            user to specify filenames for each script they load in a functional way. The
            kernel would save them as files and further execute them by loading them. This
            would pave way for a plug-gable architecture where we can rely on scripting to
            load files to the MetaCall, execute them and ensure that the language mixing
            process happens clearly.
            """
            logger_output = "success"
            stream_content = {"name": "stdout", "text": logger_output}
            self.send_response(self.iopub_socket, "stream", stream_content)

        return {
            "status": "ok",
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {},
        }
