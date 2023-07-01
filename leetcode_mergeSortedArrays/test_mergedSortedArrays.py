from mergeSortedArrays import mergeAndSortArrays
def testMergedArraysMatchExpectedValues():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    assert mergeAndSortArrays(nums1, m, nums2, n) == [1,2,2,3,5,6]

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    assert mergeAndSortArrays(nums1, m, nums2, n) == [1]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    assert mergeAndSortArrays(nums1, m, nums2, n) == [1]
