from collections import UserList


class UnorderedList(UserList):
    def __init__(self, *args):
        super(UnorderedList, self).__init__(*args)

    def sort(self, *_, **__):
        raise NotImplementedError("sort not implemented for UnorderedList")

    def reverse(self):
        raise NotImplementedError("reverese not implemented for UnorderedList")

    def extend(self, *args):
        if not isinstance(self, UnorderedList):
            raise TypeError("UnorderedList expected")
        return super(UnorderedList, self).extend(*args)

    def __eq__(self, other):
        if not isinstance(other, UnorderedList):
            return NotImplemented
        if len(self) != len(other):
            return False
        other = list(other)
        for item in self:
            found = False
            for i, o in enumerate(other):
                if o == item:
                    del other[i]
                    found = True
                    break
            if not found:
                return False
        return True

    def __lt__(self, _):
        return NotImplemented

    def __le__(self, _):
        return NotImplemented

    def __gt__(self, _):
        return NotImplemented

    def __ge__(self, _):
        return NotImplemented
