import os

from logger import logger_with_path


def logger(path):
    """Name kept as in homework statement: logger(path)."""
    return logger_with_path(path)


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert hello_world() == 'Hello World'
        assert summator(2, 2) == 4
        assert div(6, 2) == 3

        summator(4.3, b=2.2)

    for path in paths:
        assert os.path.exists(path)

        with open(path, encoding='utf-8') as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content


if __name__ == '__main__':
    test_2()
