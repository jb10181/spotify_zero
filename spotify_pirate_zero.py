import spotipy
import spotipy.util as util
import os.path
# import sys
# import numpy as np
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import requests
from io import BytesIO
import ST7789

speed_scaling = 5

credentials_file = ".credentials"

font_artist_size = 30
font_album_size = 20
font_song_size = 45

font_path = "VioletSans-Regular.ttf"

scope = "user-read-currently-playing"
redirect_uri = "http://localhost:8888/callback/"

if os.path.isfile(credentials_file):
    print("Using saved credentials")

    with open(credentials_file, "r") as f:
        lines = f.readlines()
        username = lines[0][:-1]
        CLIENT_ID = lines[1][:-1]
        CLIENT_SECRET = lines[2][:-1]
else:
    print("Generating new credentials")
    username = input(
        "Please input usename (from the Spotify account overview):            "
    )
    CLIENT_ID = input(
        "Please input client ID (from the Spotify developer dashboard):       "
    )
    CLIENT_SECRET = input(
        "Please input client secret (from the Spotify developer dashboard)    "
    )

    with open(credentials_file, 'a', newline='\n') as f:
        f.write(username + "\n")
        f.write(CLIENT_ID + "\n")
        f.write(CLIENT_SECRET + "\n")

token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET,
                                   redirect_uri)

sp = spotipy.Spotify(auth=token)

currentsong = sp.currently_playing()

name_artist = currentsong["item"]["artists"][0]["name"]  # put in exception here
name_album = currentsong["item"]["album"]["name"]
name_song = currentsong["item"]["name"]
url_album_art = currentsong["item"]["album"]["images"][0]["url"]

print("Now playing {} by {}".format(name_song, name_artist))
print(name_album)
# print(url_album_art)
##############################################################################
response = requests.get(url_album_art)
song_art = Image.open(BytesIO(response.content))

###############################################################################
disp = ST7789.ST7789(
    port=0,
    cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CSB_BACK or BG_SPI_CS_FRONT
    dc=9,
    backlight=19,               # 18 for back BG slot, 19 for front BG slot.
    rotation=90,
    spi_speed_hz=80 * 1000 * 1000
)

# Initialize display.
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height

img = song_art.resize((HEIGHT, WIDTH))

draw = ImageDraw.Draw(img)

img = Image.new('RGBA', (WIDTH, HEIGHT), color=(0, 0, 0, 128))
draw = ImageDraw.Draw(img)

disp.display(img)

# font_song = ImageFont.truetype(font_path, size=font_song_size)
# font_album = ImageFont.truetype(font_path, size=font_album_size)
# font_artist = ImageFont.truetype(font_path, size=font_artist_size)
#
#
# def text_params(name, font):
#     size_x, size_y = draw.textsize(name, font)
#     text_x = disp.width
#     text_y = (80 - size_y) // 2
#     return size_x, size_y, text_x, text_y
#
#
# t_start = time.time()
# while True:
#     x_artist = (time.time() - t_start) * speed_scaling * font_artist_size * len(name_artist) / 240
#     x_album = (time.time() - t_start) * speed_scaling * font_album_size * len(name_album) / 240
#     x_song = (time.time() - t_start) * speed_scaling * font_song_size * len(name_song) / 240
#
#     img = song_art.resize((HEIGHT, WIDTH))
#     draw = ImageDraw.Draw(img)
#
#     # artist
#     size_x, size_y, text_x, text_y = text_params(name_artist, font_artist)
#     if size_x > 240:
#         x_artist %= (size_x + disp.width) * size_x / 240
#         draw.text((int(text_x - x_artist), 10), name_artist, font=font_artist, fill=(255, 255, 255))
#     else:
#         draw.text((int((240 - size_x)/2), 10), name_artist, font=font_artist, fill=(255, 255, 255))
#
#     # album
#     size_x, size_y, text_x, text_y = text_params(name_album, font_album)
#     if size_x > 240:
#         x_album %= (size_x + disp.width)
#         draw.text((int(text_x - x_album), 60), name_album, font=font_album, fill=(255, 255, 255))
#     else:
#         draw.text((int((240 - size_x)/2), 60), name_album, font=font_album, fill=(255, 255, 255))
#
#     # song
#     size_x, size_y, text_x, text_y = text_params(name_song, font_song)
#     if size_x > 240:
#         x_song %= (size_x + disp.width)
#         draw.text((int(text_x - x_song), 100), name_song, font=font_song, fill=(255, 255, 255))
#     else:
#         draw.text((int((240 - size_x)/2), 100), name_song, font=font_song, fill=(255, 255, 255))
#
#     disp.display(img)
