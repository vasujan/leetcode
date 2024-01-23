from solution import Solution, ListNode

# t.add(TestCase([0, 1, 1], l1 = [0, 2], l2 = [0, 9]))

def _test_func(l1: list, l2: list) -> list:
    l1_ln = ListNode.fromList(l1)
    l2_ln = ListNode.fromList(l2)
    return Solution().addTwoNumbers(l1_ln, l2_ln).toList()

def test_outtype():
    l1 = ListNode.fromList([0])
    l2 = ListNode.fromList([1])
    out = ListNode(1, None)
    assert type(Solution().addTwoNumbers(l1, l2)) == ListNode

def test_1():
    l1 = [0]
    l2 = [0, 1]
    out = [0, 1]
    assert out == _test_func(l1, l2)

def test_2():
    l1 = [1, 1, 1]
    l2 = [2, 2, 2]
    out = [3, 3, 3]
    assert out == _test_func(l1, l2)

def test_3():
    l1 = [1, 1, 1]
    l2 = [2, 2, 9]
    out = [3, 3, 0, 1]
    assert out == _test_func(l1, l2)
