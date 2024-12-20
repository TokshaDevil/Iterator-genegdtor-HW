class FlatIterator:

    def __init__(self, lst):
        self.list = lst
        self.index1 = 0
        self.index2 = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index1 >= len(self.list):
            raise StopIteration()
        el_list = self.list[self.index1]
        steps = len(el_list) - 1
        if '__iter__' in dir(el_list):
            self.index2 += 1
            if self.index2 == steps:
                tmp_ind1 = self.index1
                tmp_ind2 = self.index2
                self.index2 = -1
                self.index1 += 1
                return self.list[tmp_ind1][tmp_ind2]
            return self.list[self.index1][self.index2]
        else:
            self.index1 += 1
            return self.list[self.index1]


def test():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test()
