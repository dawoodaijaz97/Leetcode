def solve(nums1: list[int], nums2: list[int]) -> int:
    n = len(nums1)
    operations = 0
    j = 0

    for i in range(n):
        if nums1[i] == nums2[j]:
            j += 1
        else:
            operations += 1

    return operations