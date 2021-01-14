class InvalidToken(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnknownError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
