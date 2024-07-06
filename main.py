# -- Iterator

class Prime:
    def __init__(self, stop):
        self.start = 2
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            pr = 0
            for q in range(1, 10):
                if self.start % q == 0:
                    pr += 1
            if pr == 2:
                return self.start
        else:
            for i in range(2, 10):
                if self.start % i == 0:
                    break
                else:
                    return self.start
            self.start += 1



for i in Prime(20):
    print(i)




def prime_num(stop):
    nm = 2
    s = 0
    while s < stop:
        pr = 0
        if nm < 10:
            for q in range(1, 10):
                if nm % q == 0:
                    pr += 1
        if pr == 2:
            yield nm
        else:
            for i in range(2, 10):
                if nm % i == 0:
                    break
                else:
                    yield nm
        nm += 1
        s += 1
for numbers in prime_num(20):
    print(numbers)