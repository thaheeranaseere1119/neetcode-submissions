class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.store:
            self.store[key] = []

        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""

        values = self.store[key]

        start = 0
        end = len(values) - 1

        res = ""

        while start <= end:

            mid = (start + end) // 2

            if values[mid][0] <= timestamp:
                res = values[mid][1]
                start = mid + 1

            else:
                end = mid - 1

        return res