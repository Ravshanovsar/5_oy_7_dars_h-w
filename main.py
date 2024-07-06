# -- Generator

# def even(stop: int):
#     i = 0
#     while i <= stop:
#         yield i
#         i += 2
#
# for number in even(10000):
#     print(number)

# -- Iterator

# class MyRange:
#     def __init__(self, stop):
#         self.start = 0
#         self.stop = stop
#         self.step = 2
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start > self.stop:
#             raise StopIteration
#         else:
#             number = self.start
#             self.start += self.step
#             return number
# my_range = MyRange(29)
# for i in my_range:
#     print(i)