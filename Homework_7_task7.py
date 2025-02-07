import pytest

class FileProcessor:
    """Класс для работы с файлами."""

    @staticmethod
    def write_to_file(file_path: str, data: str):
        with open(file_path, 'w') as f:
            f.write(data)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        with open(file_path, 'r') as f:
            return f.read()

def test_file_write_read(tmpdir):
    file = tmpdir.join("testfile.txt")
    FileProcessor.write_to_file(file, "Hello, World!")
    content = FileProcessor.read_from_file(file)
    assert content == "Hello, World!"
