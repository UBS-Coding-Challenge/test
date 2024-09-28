

def q5_efficient_hunter_kazuma(nums: list[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0

    circle, attack, cooldown = -nums[0], 0, 0

    for i in range(1, n):
        circle, attack, cooldown = max(circle, -nums[i] + cooldown), nums[i] + circle, max(cooldown, attack)

    return max(circle, attack, cooldown)
