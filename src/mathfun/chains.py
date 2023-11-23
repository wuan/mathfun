from dataclasses import dataclass
from typing import List

from . import BitPermutations


@dataclass
class ChainResult:
    sum: int
    summands: List[int]
    longer_indexes: List[int]


def sum_chain(numbers: str, total_elements: int) -> List[ChainResult]:
    total_size = len(numbers)
    base_number = total_size // total_elements
    number_of_extensions = total_size % total_elements

    permutations = BitPermutations(total_elements, number_of_extensions)

    results = []

    for positions in permutations:
        sum = 0
        summands = []
        pos = 0
        for index in range(total_elements):
            size = base_number + (1 if index in positions else 0)
            value = int(numbers[pos:pos + size])
            summands.append(value)

            sum += value
            pos += size

            results.append(ChainResult(sum, summands, positions))

    return results
