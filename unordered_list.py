from collections import UserList


class unordered_list(UserList):
    def __init__(self, *args):
        super(unordered_list, self).__init__(*args)

    def sort(self, *_, **__):
        raise NotImplementedError("sort not implemented for unordered_list")

    def reverse(self):
        raise NotImplementedError("reverese not implemented for unordered_list")

    def extend(self, *args):
        if not isinstance(self, unordered_list):
            raise TypeError("unordered_list expected")
        return super(unordered_list, self).extend(*args)

    def __eq__(self, other):
        if not isinstance(other, unordered_list):
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
