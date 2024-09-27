

def q1_get_sum(nums: list[int], target: int) -> int:
    total = sum(nums)
    print(nums)
    print([x * 2 for x in nums])
    st = set()

    return total * target