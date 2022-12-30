'''
Get the Plex token from the token.yaml file
https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/
'''

from pathlib import Path
import sys
import yaml

INFO_FILE = Path(__file__).parent.parent / "plex_info.yaml"


def get_plex_info() -> dict:
    """Get the Plex info from the plex_info.yaml file

    Returns:
        dict: Plex info
    """
    data = None
    with open(INFO_FILE, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return data


def get_plex_token() -> str:
    """Get the Plex token from the token.yaml file

    Returns:
        str: Plex token
    """
    data = get_plex_info()
    return data['token']


def get_plex_server() -> str:
    """Get the Plex server from the token.yaml file 

    Returns:
        str: Plex server
    """
    data = get_plex_info()
    return data['server']
