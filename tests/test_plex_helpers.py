import UpdatePlexPlaylists.plex_helpers as ph


def test_get_plex_server():
    assert "http" in ph.get_plex_server()


def test_get_plex_token():
    assert type(ph.get_plex_token()) == str
