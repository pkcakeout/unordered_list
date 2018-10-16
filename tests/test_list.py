import pytest


from unorderedlist import UnorderedList


def test_list_call():
    """
    >>> def f():
    ...     yield 1
    ...     yield 2
    ...
    >>> UnorderedList(f())
    UnorderedList([1, 2])
    """
    def f():
        yield 1
        yield 2
    assert UnorderedList(f()) == UnorderedList([1, 2])


def test_list_sort():
    """
    >>> test_list_sort()
    Raised NotImplementedError
    """
    l1 = UnorderedList([2, 3, 1, 4])
    with pytest.raises(NotImplementedError):
        l1.sort()


def test_list_sort_reversed():
    """
    >>> test_list_sort_reversed()
    Raised NotImplementedError
    """
    l1 = UnorderedList([2, 3, 1, 4])
    with pytest.raises(NotImplementedError):
        l1.sort(reversed=True)


def test_list_reverse():
    """
    >>> test_list_reverse()
    Raised NotImplementedError
    """
    l1 = UnorderedList([4, 3, 2, 1])
    with pytest.raises(NotImplementedError):
        l1.reverse()


def test_list_append():
    """
    >>> test_list_append()
    UnorderedList([1, 2, 3, 4])
    """
    l1 = UnorderedList([2, 1])
    l1.append(3)
    l1.append(4)
    assert l1 == UnorderedList([4, 3, 2, 1])


def test_list_append_unbound():
    """
    >>> test_list_append_unbound()
    UnorderedList([1, 2, 3, 4])
    """
    l1 = UnorderedList([2, 1])
    UnorderedList.append(l1, 3)
    UnorderedList.append(l1, 4)
    assert l1 == UnorderedList([4, 3, 2, 1])


def test_list_append_unbound_assigned():
    """
    >>> test_list_append_unbound_assigned()
    [1, 2, 3, 4]
    """
    append = UnorderedList.append
    l1 = UnorderedList([4, 3, 2, 1])
    append(l1, 3)
    append(l1, 4)


def test_list_append_insert():
    """
    >>> test_list_append_insert()
    UnorderedList(['first', 'second'])
    """
    l = UnorderedList([])
    l.append("second")
    l.insert(0, "first")
    assert l == UnorderedList(["first", "second"])
    assert l == UnorderedList(["second", "first"])


def test_list_pop():
    l1 = UnorderedList([1, 2])
    i = l1.pop()
    assert i in [1, 2]
    assert len(l1) == 1


def test_list_pop0():
    l1 = UnorderedList([1, 2])
    i = l1.pop(0)
    assert i in [1, 2]
    assert len(l1) == 1


def test_list_pop_all():
    """
    >>> test_list_pop_all()
    True
    """
    l1 = UnorderedList([1, 2])
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
    l = UnorderedList([1, 2, 3])
    l.extend([])
    l.extend(())
    l.extend(set())  # not currently optimised (not worth the trouble)
    assert l == UnorderedList([1, 2, 3])
    assert len(l) == 3
    l.extend([4,x+1,6])
    l.extend([7,8,9,10,11,12,13,14,15,16])
    assert l == UnorderedList(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])


def test_list_extend_unbound():
    """
    >>> test_list_extend_unbound()
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    """
    x = 4
    l = UnorderedList([1, 2, 3])
    UnorderedList.extend(l, [])
    UnorderedList.extend(l, ())
    try:
        UnorderedList.extend((), ())
    except TypeError:
        pass
    else:
        assert False, "TypeError not raised!"
        UnorderedList.extend(l, set())  # not currently optimised (not worth the trouble)
    assert l == UnorderedList([1, 2, 3])
    assert len(l) == 3
    UnorderedList.extend(l, [4, x + 1, 6])
    UnorderedList.extend(l, [7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    assert l == UnorderedList(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])


def test_comparisons():
    l = UnorderedList([{2: 2}, {2: 2}, 3])
    l2 = UnorderedList([{2: 2}, 3])
    l3 = UnorderedList([3, {2: 2}])
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
