from . import BitPermutations


def sum_chain(numbers: str, total_elements: int):
    print(f"take {total_elements} summands from {numbers}:")
    total_size = len(numbers)
    base_number = total_size // total_elements
    number_of_extensions = total_size % total_elements

    permutations = BitPermutations(total_elements, number_of_extensions)

    for positions in permutations:
        sum = 0
        parts = []
        pos = 0
        for index in range(total_elements):
            size = base_number + (1 if index in positions else 0)
            value_string = numbers[pos:pos + size]
            parts.append(value_string)
            value = int(value_string)
            sum += value
            pos += size

        print(positions, sum, "=", "+".join(parts))
