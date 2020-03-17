from datetime import datetime
from datetime import timedelta


def is_it_possible_to_collect(days):
    collect_date = datetime.today() + timedelta(days=days)
    date = collect_date.strftime("%d.%m.%Y")
    weekday = collect_date.weekday()
    possible_to_collect = weekday != 2 and weekday != 4
    return date, possible_to_collect


if __name__ == '__main__':
    print(*is_it_possible_to_collect(2))


