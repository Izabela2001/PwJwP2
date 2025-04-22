from typing import List


def average(numbers: List[float]) -> float:

    if not numbers:
        raise ValueError("Lista liczb nie może być pusta")

    return sum(numbers) / len(numbers)

data = [3.5, 4.0, 5.5, 6.0]
print(average(data))