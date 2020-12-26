import spotipy.util as util
import os.path


# spotify authentication
def spotify_authorisation():
    if os.path.isfile(credentials_file):
        with open(credentials_file, "r") as f:
            lines = f.readlines()
            username = lines[0][:-1]
            CLIENT_ID = lines[1][:-1]
            CLIENT_SECRET = lines[2][:-1]
            print("Reusing credentials")
    else:
        username = input(
            "Please input usename (from the Spotify account overview):" +
            "            ")
        CLIENT_ID = input(
            "Please input client ID (from the Spotify developer dashboard):" +
            "       ")
        CLIENT_SECRET = input(
            "Please input client secret (from the Spotify developer dashboard)"
            + "    ")

        with open(credentials_file, 'a', newline='\n') as f:
            f.write(username + "\n")
            f.write(CLIENT_ID + "\n")
            f.write(CLIENT_SECRET + "\n")

    token = util.prompt_for_user_token(username, scope, CLIENT_ID,
                                       CLIENT_SECRET, redirect_uri)

    return token


# spotify authentication parameters
credentials_file = ".credentials"
scope = "user-read-currently-playing"
redirect_uri = "http://localhost:8888/callback/"
token = spotify_authorisation()
