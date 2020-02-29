from Modules.FestivalHandler import *

def add_festival__good_values__no_error():
    festivals = []
    name = 'TestFestival'
    month = 11
    cost = 123
    artists = ['ArtistA', 'ArtistB']

    try:
        add_festival(festivals, name, month, cost, artists)
        assert True
    except:
        assert False


def add_festival__bad_values__error():
    festivals = []
    name = 'TestFestival'
    month = 14  # invalid month
    cost = 123
    artists = ['ArtistA', 'ArtistB']

    try:
        add_festival(festivals, name, month, cost, artists)
        assert False
    except:
        assert True

def get_all_for_artist__matching_values__no_error():
    artist = 'Johnny'
    festivals = []
    name = 'TestFestival'
    month = 1
    cost = 1
    artists = ['Johnny']

    add_festival(festivals, name, month, cost, artists)

    assert artist in get_artists(festivals[0])


def get_all_for_artist__mismatching_values__error():
    artist = 'Johnny'
    unknown_artist = 'Johnny The Evil'
    festivals = []
    name = 'TestFestival'
    month = 1
    cost = 1
    artists = ['Johnny']

    add_festival(festivals, name, month, cost, artists)

    assert unknown_artist not in get_artists(festivals[0])


def test_all():
    add_festival__good_values__no_error()
    add_festival__bad_values__error()
    get_all_for_artist__matching_values__no_error()
    get_all_for_artist__mismatching_values__error()