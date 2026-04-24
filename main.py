import os
from logger import logger, logger_with_path


# TEST 1
def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world()
    result = summator(2, 2)
    assert result == 4

    result = div(6, 2)
    assert result == 3

    assert os.path.exists(path)

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as f:
        content = f.read()

    assert 'summator' in content
    for item in (4.3, 2.2, 6.5):
        assert str(item) in content


# TEST 2
def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger_with_path(path)
        def hello_world():
            return 'Hello World'

        @logger_with_path(path)
        def summator(a, b=0):
            return a + b

        @logger_with_path(path)
        def div(a, b):
            return a / b

        assert hello_world() == 'Hello World'
        assert summator(2, 2) == 4
        assert div(6, 2) == 3

        summator(4.3, b=2.2)

    for path in paths:
        assert os.path.exists(path)

        with open(path) as f:
            content = f.read()

        assert 'summator' in content
        for item in (4.3, 2.2, 6.5):
            assert str(item) in content


if __name__ == '__main__':
    test_1()
    test_2()
