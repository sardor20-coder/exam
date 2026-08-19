from collections import Counter

def rearrange_by_frequency(nums: list[int]) -> list[int]:
    count = Counter(nums)

    return sorted(nums, key=lambda x: (-count[x], x))