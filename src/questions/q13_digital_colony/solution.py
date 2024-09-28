
def q13_solution(generations: int, colony: str):
    weight = sum([int(x) for x in colony])

    for _ in range(generations):
        new_weight = weight
        new_colony = ""
        n = len(colony)
        for i in range(n - 1):
            x, y = int(colony[i]), int(colony[i + 1])
            val = weight + (x - y if x >= y else 10 - (y - x))
            new_digit = str(val)[-1]
            new_weight += int(new_digit)
            new_colony += str(x)
            new_colony += new_digit

        new_colony += colony[-1]
        colony = new_colony
        weight = new_weight

    return str(weight)
