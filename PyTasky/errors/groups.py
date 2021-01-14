class GroupNotConnected(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class GroupNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
