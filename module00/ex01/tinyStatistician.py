import numpy as np

class TinyStatistician:
    def mean(arr):
        try:
            s = 0
            for v in arr:
                s += v
            return s / len(arr)
        except:
            return None

    def median(arr):
        try:
            numbers = sorted(arr)
            mid = len(numbers) // 2

            if (len(numbers) % 2 == 0):
                return (numbers[mid - 1] + numbers[mid]) / 2
            return numbers[mid]
        except:
            return None

    def quartile(arr):
        try:
            numbers = sorted(arr)
            nlen = len(numbers)
            return [ numbers[nlen // 4], numbers[3 * (nlen // 4)] ]
        except:
            return None

a = [1, 42, 300, 10, 59]
print(TinyStatistician.quartile(a))