from Modules.Exceptions import InvalidMonth


def get_name(festival):
    return festival[0]


def get_month(festival):
    return festival[1]


def get_cost(festival):
    return festival[2]


def get_artists(festival):
    return festival[3]


def set_name(festival, name):
    festival[0] = name


def set_month(festival, month):
    if month not in range(1, 13):
        raise InvalidMonth

    festival[1] = month


def set_cost(festival, cost):
    festival[2] = cost


def set_artists(festival, artists):
    festival[3] = artists


def add_artist(festival, artist):
    festival[3].append(artist)


def create_festival(name, month, cost, artists):
    festival = [0, 0, 0, []]

    set_name(festival, name)
    set_month(festival, month)
    set_cost(festival, cost)
    set_artists(festival, artists)

    return festival

