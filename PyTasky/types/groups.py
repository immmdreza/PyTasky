class GroupInfo:
    def __init__(self, name, link, point) -> None:
        self.name = name
        self.point = point
        self.link = link

    @staticmethod
    def parse(j):
        return GroupInfo(j['groupName'], j['groupLink'], j['groupPoint'])
