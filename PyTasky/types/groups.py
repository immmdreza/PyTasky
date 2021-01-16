class GroupInfo:
    def __init__(self, name, link, point) -> None:
        self.name = name
        self.point = point
        self.link = link

    @staticmethod
    def parse(j):
        return GroupInfo(j['groupName'], j['groupLink'], j['groupPoint'])

class GroupFullInfo:
    def __init__(self, title, point, rank, link, lgc, gcc, creator_id) -> None:
        self.title = title
        self.point = point
        self.link = link
        self.rank = rank
        self.lgc = lgc
        self.gcc = gcc
        self.creator_id = creator_id

    @staticmethod
    def parse(j):
        return GroupFullInfo(
            j['title'], 
            j['point'], 
            j['rank'],
            j['link'],
            j['lgc'],
            j['gcc'],
            j['creatorId']
        )
