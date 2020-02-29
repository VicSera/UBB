from Modules.Festival import create_festival, get_cost, get_month, get_name, get_artists
from Modules.Exceptions import InvalidMonth, ValidationError


def check_unique(candidate_festival, festivals):
    for festival in festivals:
        if get_name(festival) == get_name(candidate_festival):
            raise ValidationError('Name already used')


def add_festival(festivals, name, month, cost, artists):
    """
    Add a festival to the festival list, being given a name, a month, a cost, and a list of artists
    :param festivals: The festival list
    :param name: The name of the new festival
    :param month: The month of the new festival
    :param cost: The cost of the new festival
    :param artists: The artists performing at the new festival
    """
    try:
        festival = create_festival(name, month, cost, artists)

        festivals.append(festival)
    except InvalidMonth as error:
        raise ValidationError('Month has to be in range 1-12')


def month_to_string(month_number):
    months = {month_number: month for month_number, month in zip(
        range(1, 13),
        ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December'])}

    return months[month_number]


def sort_festivals(festivals):
    festivals.sort(key=lambda festival: get_name(festival))
    festivals.sort(key=lambda festival: get_month(festival))


def get_all_for_season(festivals, season):
    months_per_season = {
        'Summer': ['June', 'July', 'August'],
        'Autumn': ['September', 'October', 'November'],
        'Winter': ['December', 'January', 'February'],
        'Spring': ['March', 'April', 'May']
    }

    if season not in months_per_season.keys():
        raise ValidationError('Season {} doesn\'t exist'.format(season))

    festivals_in_season = []

    for festival in festivals:
        if month_to_string(get_month(festival)) in months_per_season[season]:
            festivals_in_season.append(festival)
            # print('{} {} {}, played by: {}'.format(get_name(festival), get_month(festival), get_cost(festival), get_artists(festival)))

    sort_festivals(festivals_in_season)
    return festivals_in_season
    # print(months)


def get_all_for_artist(festivals, artist):
    festivals_with_given_artist = []

    for festival in festivals:
        if artist in get_artists(festival):
            festivals_with_given_artist.append(festival)

    if len(festivals_with_given_artist) == 0:
        raise ValidationError('Artist {} not found.'.format(artist))

    return festivals_with_given_artist


def initialize_festivals():
    festivals = []
    names = ['Untold', 'EC', 'Woodstock', 'ArtMania', 'Unnamed']
    months = [1, 6, 6, 2, 9]
    costs = [100, 150, 75, 100, 95]
    artists = [
        ['John', 'Johnny', 'Sam'],
        ['Michael', 'Johnny', 'Lawrence'],
        ['Anna', 'Duke', 'Patrick'],
        ['Sam', 'Michael', 'Bobby'],
        ['Bobby', 'Anna', 'Sam']
    ]

    for index in range(len(names)):
        festival = create_festival(names[index], months[index], costs[index], artists[index])
        festivals.append(festival)

    return festivals