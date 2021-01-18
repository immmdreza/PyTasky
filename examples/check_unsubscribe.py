from PyTasky import TaskSystem

delay_between_requests_by_seconds = 60 * 15
_type = 'sleep'  # or 'job'

client = TaskSystem('API_TOKEN')
users = client.getUsers()


def print_unsubscribed_users():
    global users
    _users = client.getUsers()
    unsubscribed_users = [user for user in users if user not in _users]
    users = _users
    print(unsubscribed_users)
    return unsubscribed_users


if _type == 'sleep':
    from time import sleep

    while True:
        sleep(delay_between_requests_by_seconds)
        print_unsubscribed_users()

elif _type == 'job':
    from apscheduler.schedulers.background import BackgroundScheduler

    scheduler = BackgroundScheduler()
    scheduler.add_job(print_unsubscribed_users, 'interval', seconds=delay_between_requests_by_seconds)
    scheduler.start()
    while True:
        pass
