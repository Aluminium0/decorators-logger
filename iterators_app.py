"""Small iterator/generator app instrumented with the logger decorator.

This mirrors the "iterators, generators, yield" homework style and shows
how to apply logger_with_path to real application code.
"""

from logger import logger_with_path


class FlatIterator:
    """Iterate over nested lists and yield scalar items one by one."""

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.outer_index = 0
        self.inner_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.outer_index < len(self.list_of_lists):
            current_list = self.list_of_lists[self.outer_index]
            if self.inner_index < len(current_list):
                value = current_list[self.inner_index]
                self.inner_index += 1
                return value

            self.outer_index += 1
            self.inner_index = 0

        raise StopIteration


def flat_generator(list_of_lists):
    """Generator version of FlatIterator."""
    for inner_list in list_of_lists:
        for item in inner_list:
            yield item


@logger_with_path('iterators_app.log')
def collect_flat_items(list_of_lists):
    """Collect flattened items using the generator version."""
    return list(flat_generator(list_of_lists))


@logger_with_path('iterators_app.log')
def count_flat_items(list_of_lists):
    """Count flattened items using the iterator version."""
    return len(list(FlatIterator(list_of_lists)))


def demo():
    nested = [[1, 2, 3], [4], [5, 6]]

    items = collect_flat_items(nested)
    total = count_flat_items(nested)

    assert items == [1, 2, 3, 4, 5, 6]
    assert total == 6


if __name__ == '__main__':
    demo()
