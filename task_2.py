import os
from datetime import datetime
from functools import wraps


def _write_log(path, func_name, args, kwargs, result):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(
            f"{datetime.now()} | "
            f"{func_name} | "
            f"args={args} | "
            f"kwargs={kwargs} | "
            f"result={result}\n"
        )


def logger(path):  

    def __logger(old_function):

        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            _write_log(
                path=path,   
                func_name=old_function.__name__,
                args=args,
                kwargs=kwargs,
                result=result
            )

            return result

        return new_function

    return __logger


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

        with open(path, encoding='utf-8') as f:
            content = f.read()

        assert 'summator' in content

        for item in (4.3, 2.2, 6.5):
            assert str(item) in content


if __name__ == '__main__':
    test_2()
