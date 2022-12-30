# Update Plex Playlists

Updates playlists based on folder names. Takes files in the Tutorials section and by folder names create actual playlists, which are more useful for playing back multiple video's.

## Requirements
- Python 3.10
- Poetry

add a `plex_info.yaml` in the root folder containing 2 keyval pairs

```
server: "http://yourserver:yourport"
token: "yourtokenhere"
```
https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/

## Installation
Run in VS Code
- Make sure requirements are met
- Run `poetry init`
- Run `poetry shell`
- Run pytest to check helpers
- Open `UpdatePlexPlaylists.ipynb` and run cells to start creating/updating playlists
