from Modules.FestivalHandler import *


def launch():
    print("launching app")
    festivals = initialize_festivals()

    functions = {
        'Add': call_add,
        'Show festivals for a given season': call_show_all_for_season,
        'Show festivals played by a certain artist': call_show_all_for_artist
    }

    options = list(functions.keys())

    while True:
        user_choice = choose(options)
        chosen_function = functions[options[user_choice]]

        chosen_function(festivals)


def artists_as_string(artists):
    artists_string = ""

    for artist in artists:
        artists_string += '{} '.format(artist)

    return artists_string


def print_festival(festival):
    print("{} {} {}$, played by {}".format(get_name(festival), month_to_string(get_month(festival)), get_cost(festival), artists_as_string(get_artists(festival))))


def get_input_of_type(type, extra_message):
    while True:
        try:
            user_input = type(input(extra_message))
            return user_input
        except:
            continue


def choose(options):
    for index, option in enumerate(options):
        print("{}. {}".format(index + 1, option))

    while True:
        try:
            user_input = int(input('Choice: '))
            if user_input not in range(1, len(options) + 1):
                print('Input has to be in range {}-{}'.format(1, len(options)))
                continue
            return user_input - 1
        except ValueError:
            print('Please give valid input')


def call_add(festivals):
    name = get_input_of_type(str, 'Name: ')
    month = get_input_of_type(int, 'Month: ')
    cost = get_input_of_type(int, 'Cost: ')
    number_of_artists = get_input_of_type(int, 'How many artists will there be?')
    artists = []

    for index in range(number_of_artists):
        artist = input()
        artists.append(artist)

    try:
        add_festival(festivals, name, month, cost, artists)
    except ValidationError as error:
        print(error)


def call_show_all_for_season(festivals):
    season = get_input_of_type(str, 'Please input a season: ')

    try:
        festivals_in_season = get_all_for_season(festivals, season)
        for festival in festivals_in_season:
            print_festival(festival)
        # print(festivals_in_season)
    except ValidationError as error:
        print(error)


def call_show_all_for_artist(festivals):
    artist = get_input_of_type(str, 'Please give an artist: ')

    try:
        festivals_with_artist = get_all_for_artist(festivals, artist)
        for festival in festivals_with_artist:
            print_festival(festival)
        # print(festivals_with_artist)
    except ValidationError as error:
        print(error)