def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Length Error")
    else:
        count = 0
        for a, b in zip(strand_a, strand_b):
            if a is not b:
                count += 1
    return count
