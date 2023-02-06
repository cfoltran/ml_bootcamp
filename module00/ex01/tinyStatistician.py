import numpy as np

class TinyStatistician:
    def mean(data):
        try:
            return sum(data) / len(data)
        except:
            return None

    def median(data):
        try:
            data_sorted = sorted(data)
            mid = len(data_sorted) // 2

            if (len(data_sorted) % 2 == 0):
                return (data_sorted[mid - 1] + data_sorted[mid]) / 2
            return data_sorted[mid]
        except:
            return None

    def quartile(data):
        try:
            data_sorted = sorted(data)
            nlen = len(data_sorted)
            return [ data_sorted[nlen // 4], data_sorted[3 * (nlen // 4)] ]
        except:
            return None

    def percentile(data, p):
        try:
            data_sorted = sorted(data)
            n = len(data_sorted)
            p = (p * (n - 1) / 100) + 1
            index = int(p)
            residual = p - index
            percentile = data_sorted[index - 1] + residual * (data_sorted[index] - data_sorted[index - 1])
            return percentile
        except:
            return None

    def var(data):
        try:
            data = sorted(data)
            return sum((x - TinyStatistician.mean(data)) ** 2 for x in data) / len(data)
        except:
            return None

    def std(data):
        try:
            data = sorted(data)
            return TinyStatistician.var(data) ** 0.5
        except:
            return None

a = [1, 42, 300, 10, 59]
