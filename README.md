# Logger Decorators

Python decorators that log:
- timestamp
- function name
- arguments
- return value

## Files
- logger.py - decorators
- main.py - tests

## Usage

```python
@logger_with_path('log.txt')
def add(a, b):
    return a + b
