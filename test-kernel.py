import re
from metacall_jupyter import metacall_jupyter


class TestKernel:
    """
    Defines the unit-tests for the MetaCall Kernel
    """

    def test_start_metacall(self):
        """Testing the MetaCall Subprocess start function"""
        kernel = metacall_jupyter()
        kernel._start_metacall()

    def test_create_kernel(self):
        """Testing whether the metacall_jupyter() exists or not"""
        assert metacall_jupyter() is not None

    def test_misc(self):
        """Testing miscellaneous settings for the MetaCall Jupyter Kernel"""
        kernel = metacall_jupyter()
        assert kernel.banner is not None
        assert kernel.language is not None
        assert kernel.language_version is not None
        assert kernel.implementation is not None
        assert kernel.implementation_version is not None
        assert kernel.language_info is not None
        assert kernel.help_links is not None

    def test_byte_to_string(self):
        """Testing whether a byte is converted into the string"""
        kernel = metacall_jupyter()
        code = b'print("Hello World")'
        mock = 'print("Hello World")'
        response = kernel.byte_to_string(code)
        assert response == mock

    def test_newfile_magic(self):
        """Testing the newfile magic for the MetaCall Jupyter Kernel"""
        kernel = metacall_jupyter()
        code = """$newfile app.py
        print("Hello World")"""
        mock = "File app.py is saved."
        response = kernel.newfile_magic(code)
        assert response == mock

    def test_metacall_execute(self):
        """Testing the MetaCall execute functionality"""
        kernel = metacall_jupyter()
        code = "print(2+3)"
        extension = ".py"
        mock = "5"
        response = kernel.metacall_execute(code, extension)
        regex = re.compile(r"Script \(.+\) loaded correctly")
        match = regex.search(response)
        if match:
            response = regex.sub("", response)
        print(response)
        assert response.lstrip().replace("\n", "") == mock

    def test_shell_execute(self):
        """Testing the Shell execute functionality on the MetaCall Kernel"""
        import time

        kernel = metacall_jupyter()
        code = "!date +%s"
        shcmd = "!"
        mock = int(time.time())
        response = kernel.shell_execute(code, shcmd)
        assert int(response.replace("\n", "")) == mock

    def test_metacall_repl(self):
        """Testing the Polyglot REPL for the MetaCall Kernel"""
        kernel = metacall_jupyter()
        code = "%repl node"
        mock = "REPL 'node' has been selected."
        response = kernel.metacall_repl(code)
        assert response.decode("utf-8").lstrip().replace("\n", "") == mock
