def mergeAndSortArrays(nums1, m, nums2, n):
    nums1 = nums1[0:m]
    nums2 = nums2[0:n]
    print(nums1)
    print(nums2)
    print(m)
    print(n)

    merged = nums1 + nums2
    return sorted(merged)