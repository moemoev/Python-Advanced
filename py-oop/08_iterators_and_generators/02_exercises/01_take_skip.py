class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.start * self.step
        self.start += 1
        if self.start > self.count:
            raise StopIteration

        return value

#note:Judge did expect the solution above, but the tutors implied taht we should use the lower version where we create
# a separate Iterator class, return from class the iterator , init inside with the class, define the next behavior.

# class take_skip:
#     def __init__(self, step: int, count: int):
#         self.step = step
#         self.count = count
#
#     def __iter__(self):
#         return TakeSkipIterator(self)
#
# class TakeSkipIterator():
#     def __init__(self, take_skip: take_skip):
#         self.take_skip = take_skip
#         self.start = 0
#
#     def __next__(self):
#         value = self.start * self.take_skip.step
#         self.start += 1
#         if self.take_skip.count < self.start:
#             raise StopIteration
#
#         return value



numbers = take_skip(10, 5)
for number in numbers:
    print(number)