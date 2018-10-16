import pytest

from unordered_list import unordered_list


def test_list_call():
    """
    >>> def f():
    ...     yield 1
    ...     yield 2
    ...
    >>> unordered_list(f())
    unordered_list([1, 2])
    """

    def f():
        yield 1
        yield 2
    assert unordered_list(f()) == unordered_list([1, 2])

def test_list_sort():
    """
    >>> test_list_sort()
    Raised NotImplementedError
    """
    l1 = unordered_list([2,3,1,4])
    with pytest.raises(NotImplementedError):
        l1.sort()


def test_list_sort_reversed():
    """
    >>> test_list_sort_reversed()
    Raised NotImplementedError
    """
    l1 = unordered_list([2,3,1,4])
    with pytest.raises(NotImplementedError):
        l1.sort(reversed=True)


def test_list_reverse():
    """
    >>> test_list_reverse()
    Raised NotImplementedError
    """
    l1 = unordered_list([4, 3, 2, 1])
    with pytest.raises(NotImplementedError):
        l1.reverse()


def test_list_append():
    """
    >>> test_list_append()
    unordered_list([1, 2, 3, 4])
    """
    l1 = unordered_list([2, 1])
    l1.append(3)
    l1.append(4)
    assert l1 == unordered_list([4, 3, 2, 1])


def test_list_append_unbound():
    """
    >>> test_list_append_unbound()
    unordered_list([1, 2, 3, 4])
    """
    l1 = unordered_list([2, 1])
    unordered_list.append(l1, 3)
    unordered_list.append(l1, 4)
    assert l1 == unordered_list([4, 3, 2, 1])


def test_list_append_unbound_assigned():
    """
    >>> test_list_append_unbound_assigned()
    [1, 2, 3, 4]
    """
    append = unordered_list.append
    l1 = unordered_list([4, 3, 2, 1])
    append(l1, 3)
    append(l1, 4)


def test_list_append_insert():
    """
    >>> test_list_append_insert()
    unordered_list(['first', 'second'])
    """
    l = unordered_list([])
    l.append("second")
    l.insert(0, "first")
    assert l == unordered_list(["first", "second"])
    assert l == unordered_list(["second", "first"])


def test_list_pop():
    l1 = unordered_list([1, 2])
    i = l1.pop()
    assert i in [1, 2]
    assert len(l1) == 1


def test_list_pop0():
    l1 = unordered_list([1, 2])
    i = l1.pop(0)
    assert i in [1, 2]
    assert len(l1) == 1


def test_list_pop_all():
    """
    >>> test_list_pop_all()
    True
    """
    l1 = unordered_list([1, 2])
    i = 0
    try:
        l1.pop()
        i = 1
        l1.pop(-1)
        i = 2
        l1.pop(0)
        i = 3
    except IndexError:
        return
    pytest.fail()


def test_list_extend():
    """
    >>> test_list_extend()
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    """
    x = 4
    l = unordered_list([1,2,3])
    l.extend([])
    l.extend(())
    l.extend(set())  # not currently optimised (not worth the trouble)
    assert l == unordered_list([1,2,3])
    assert len(l) == 3
    l.extend([4,x+1,6])
    l.extend([7,8,9,10,11,12,13,14,15,16])
    assert l == unordered_list(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])


def test_list_extend_unbound():
    """
    >>> test_list_extend_unbound()
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    """
    x = 4
    l = unordered_list([1,2,3])
    unordered_list.extend(l, [])
    unordered_list.extend(l, ())
    try:
        unordered_list.extend((), ())
    except TypeError:
        pass
    else:
        assert False, "TypeError not raised!"
        unordered_list.extend(l, set())  # not currently optimised (not worth the trouble)
    assert l == unordered_list([1,2,3])
    assert len(l) == 3
    unordered_list.extend(l, [4,x+1,6])
    unordered_list.extend(l, [7,8,9,10,11,12,13,14,15,16])
    assert l == unordered_list(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])


def test_comparisons():
    l = unordered_list([{2: 2}, {2: 2}, 3])
    l2 = unordered_list([{2: 2}, 3])
    l3 = unordered_list([3, {2: 2}])
    assert l == l
    assert not (l != l)
    assert not (l == l2)
    assert l != l2
    assert l2 == l3
    assert not (l3 != l2)
    with pytest.raises(TypeError):
        l < l
    with pytest.raises(TypeError):
        l > l
    with pytest.raises(TypeError):
        l <= l
    with pytest.raises(TypeError):
        l >= l
