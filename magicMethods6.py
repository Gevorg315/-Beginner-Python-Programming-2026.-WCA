import os


class Cd:
    def __init__(self, path):
        if not os.path.isdir(path):
            raise ValueError(f"{path} is not a directory or does not exist")
        self.path = os.path.abspath(path)
        self.prev_cwd = os.getcwd()

    def __enter__(self):
        os.chdir(self.path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.prev_cwd)


import tempfile
from contextlib import redirect_stdout
from io import StringIO


def test_cd():
    with tempfile.TemporaryDirectory() as tempdir:
        with Cd(tempdir):
            assert os.getcwd() == tempdir

        assert os.getcwd() != tempdir

    with tempfile.TemporaryDirectory() as tempdir:
        non_existing_dir = os.path.join(tempdir, 'non_existing')
        with Cd(non_existing_dir):
            pass

        assert os.getcwd() != non_existing_dir

    with tempfile.TemporaryDirectory() as tempdir:
        non_existing_dir = os.path.join(tempdir, 'non_existing')
        with redirect_stdout(StringIO()):
            try:
                with Cd(non_existing_dir):
                    pass
            except ValueError as e:
                assert str(e) == f"{non_existing_dir} is not a directory or does not exist"
            else:
                assert False, "Expected ValueError to be raised"


        assert os.getcwd() != non_existing_dir