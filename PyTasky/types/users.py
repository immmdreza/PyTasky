class UserInfo:
    def __init__(self, id, point) -> None:
        self.id = id
        self.point = point

    @staticmethod
    def parse(j):
        return UserInfo(j['userId'], j['userPoint'])
