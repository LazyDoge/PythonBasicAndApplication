class NonPositiveError(BaseException):
    pass


class PositiveList(list):
    def append(self, addable):
        if addable > 0:
            list.append(self, addable)
        else:
            raise NonPositiveError


pl = PositiveList()

pl.append(2)

print(pl)

pl.append(-2)

print(pl)
