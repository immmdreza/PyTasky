from PyTasky.errors.users import UserNotFound
from typing import List
import requests
from urllib.parse import urljoin
from .types import GroupInfo, UserInfo, GroupFullInfo
from .errors import (
    LimitedToken,
    InvalidToken,
    GroupNotConnected,
    GroupNotFound,
    UnknownError,
    ListTooLarge
)


class TaskSystem:
    errors = {
        "INVALID_ACCOUNT": InvalidToken,
        "GROUP_NOT_CONNECTED": GroupNotConnected,
        "GROUP_NOT_FOUND": GroupNotFound,
        "USER_NOT_FOUND": UserNotFound,
        "LIMITED": LimitedToken,
        "LIST_TOO_LARGE": ListTooLarge
    }

    def __init__(self, token: str) -> None:
        self.token = token
        if not self.__validate_token():
            raise InvalidToken("Token is invalid")

        self.__base_url = 'https://taskyonline.com/app/api/client{token}/'.format(
            token=self.token
        )

    def __validate_token(self) -> bool:
        parts = self.token.split(':')
        if parts.__len__() != 2:
            return False

        if not parts[0].__len__() > 5 or not parts[0].isdigit():
            return False

        if parts[1].__len__() != 36:
            return False

        return True

    def _error(self, error_code: str):
        return self.errors.get(error_code, UnknownError)

    def _send_request(self, end_point: str, params=None):
        if params is None:
            params = {}
        url = urljoin(self.__base_url, end_point)
        result = requests.get(url, params=params)

        if result.status_code != 200:
            raise requests.ConnectionError('Invalid status code')

        json_result = result.json()
        if not json_result['ok']:
            code = json_result['errorCode']
            dis = json_result['description']
            raise self._error(code)(dis)

        return json_result['result']  # response is ok so return result

    def top_groups(self, offset: int = 0, limit: int = 10) -> List[GroupInfo]:
        json = self._send_request('topGroups', {'offset': offset, 'limit': limit})
        result = []
        for x in json:
            result.append(
                GroupInfo.parse(x)
            )

        return result

    def users_count(self):
        return self._send_request('usersCount')

    def is_user(self, user_id: int) -> bool:
        return self._send_request('isUser', {'userId': user_id})

    def get_user(self, user_id: int) -> List[GroupInfo]:
        return UserInfo.parse(self._send_request('getUser', {'userId': user_id}))

    def get_users(self, offset: int = 0, limit: int = 10) -> List[UserInfo]:
        json = self._send_request('getUsers', {'offset': offset, 'limit': limit})
        result = []
        for x in json:
            result.append(
                UserInfo.parse(x)
            )

        return result

    def my_group(self) -> List[GroupFullInfo]:
        json = self._send_request('myGroup')

        return GroupFullInfo.parse(json)

    def personal_point(self, offset: int = 0, limit: int = 10) -> List[UserInfo]:
        json = self._send_request('personalPoint', {'offset': offset, 'limit': limit})
        result = []
        for x in json:
            result.append(
                UserInfo.parse(x)
            )

        return result

    def get_names(self, user_ids: List[int], html_parse = False) -> List[UserInfo]:
        return self._send_request('getNames', {'userIds': user_ids, 'htmlParse': html_parse})

    topGroups = top_groups
    usersCount = users_count
    isUser = is_user
    getUser = get_user
    getUsers = get_users
    myGroup = my_group
    personalPoint = personal_point
    getNames = get_names