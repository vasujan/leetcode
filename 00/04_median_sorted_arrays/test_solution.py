from solution import Solution

_test = Solution().findMedianSortedArrays

def test_odd():
    nums1 = [1, 2]
    nums2 = [3]
    output = 2.000
    assert output == _test(nums1, nums2)

def test_even():
    nums1 = [1, 2]
    nums2 = [3, 4]
    output = 2.500
    assert output == _test(nums1, nums2)

def test_left():
    nums1 = [1, 2, 3, 4]
    nums2 = []
    output = 2.5
    assert output == _test(nums1, nums2)