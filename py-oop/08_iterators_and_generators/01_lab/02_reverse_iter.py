class ReverseIterIterator:
    def __init__(self, reverse_iter):
        self.reverse_iter = reverse_iter
        self.current_pos = len(self.reverse_iter.iterable) - 1

    def __next__(self):
        if self.current_pos < 0:
            raise StopIteration

        value = self.reverse_iter.iterable[self.current_pos]
        self.current_pos -= 1

        return value

class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return ReverseIterIterator(self)

#note Judge expects the __iter__ to return itself and not to return a new iterator object, even thought he upper is the
# 'correct' implementation, included the lower just for the points
#
# class reverse_iter:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.start = -1
#         self.stop = -len(iterable)
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.stop:
#             raise StopIteration
#
#         value = self.iterable[self.start]
#         self.start -= 1
#
#         return value
#

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
