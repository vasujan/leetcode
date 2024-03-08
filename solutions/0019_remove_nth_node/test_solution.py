from solution import Solution, ListNode

def test_reverse():
    i = [1, 2, 3, 4, 5]
    o = [5, 4, 3, 2, 1]
    s = Solution()
    assert o == ListNode.toList(s.reverse_ll(ListNode.fromList(i)))
