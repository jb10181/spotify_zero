import spotipy
import spotipy.util as util
import os.path
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import requests
from io import BytesIO
import ST7789


def text_params(name, font):
    size_x, size_y = d.textsize(name, font)
    text_x = disp.width
    text_y = (80 - size_y) // 2
    return size_x, size_y, text_x, text_y


def spotify_authorisation():
    if os.path.isfile(credentials_file):
        with open(credentials_file, "r") as f:
            lines = f.readlines()
            username = lines[0][:-1]
            CLIENT_ID = lines[1][:-1]
            CLIENT_SECRET = lines[2][:-1]
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


def get_spotify_data(token):
    sp = spotipy.Spotify(auth=token)
    currentsong = sp.currently_playing()

    name_artist = currentsong["item"]["artists"][0]["name"]
    name_album = currentsong["item"]["album"]["name"]
    name_song = currentsong["item"]["name"]
    url_album_art = currentsong["item"]["album"]["images"][0]["url"]

    # downloads image from spotify album art url
    response = requests.get(url_album_art)
    song_art = Image.open(BytesIO(response.content))

    # combines album art and decreases album art brightness
    img = song_art.resize((HEIGHT, WIDTH)).convert("RGBA")
    darken = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 155))
    ImageDraw.Draw(darken)
    album_image = Image.alpha_composite(img, darken)

    return name_artist, name_album, name_song, album_image


interval = 0.1  # rate display is updated at
speed_scaling = 8  # scales the speed that text scrolls at

# sets the fonts
font_artist_size = 30
font_album_size = 20
font_song_size = 45
font_path = "VioletSans-Regular.ttf"
font_song = ImageFont.truetype(font_path, size=font_song_size)
font_album = ImageFont.truetype(font_path, size=font_album_size)
font_artist = ImageFont.truetype(font_path, size=font_artist_size)

# spotify authentication parameters
credentials_file = ".credentials"
scope = "user-read-currently-playing"
redirect_uri = "http://localhost:8888/callback/"
token = spotify_authorisation()

# init display
disp = ST7789.ST7789(
    port=0,
    cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CSB_BACK or BG_SPI_CS_FRONT
    dc=9,
    rotation=90,
    spi_speed_hz=80 * 1000 * 1000)

# Initialize display.
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height

t_start = time.time()
while True:
    try:
        name_artist, name_album, name_song, album_image = get_spotify_data(
            token)
    except TypeError:
        name_artist = ""
        name_album = ""
        name_song = "Nothing playing"
        album_image = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 255))

    current_time = time.time()
    x_artist = (current_time - t_start
                ) * speed_scaling * font_artist_size / 15
    x_album = (current_time - t_start
               ) * speed_scaling * font_album_size / 15
    x_song = (current_time -
              t_start) * speed_scaling * font_song_size / 15

    txt = Image.new("RGBA", (WIDTH, HEIGHT), (255, 255, 255, 0))
    d = ImageDraw.Draw(txt)

    # artist
    size_x, size_y, text_x, text_y = text_params(name_artist, font_artist)
    if size_x > 240:  # if text is too long to fit on the display
        x_artist %= (size_x + disp.width) * size_x / 240
        d.text((int(text_x - x_artist), 10),
               name_artist,
               font=font_artist,
               fill=(255, 255, 255, 255))
    else:
        d.text((int((240 - size_x) / 2), 10),
               name_artist,
               font=font_artist,
               fill=(255, 255, 255, 255))

    # album
    size_x, size_y, text_x, text_y = text_params(name_album, font_album)
    if size_x > 240:  # if text is too long to fit on the display
        x_album %= (size_x + disp.width)
        d.text((int(text_x - x_album), 60),
               name_album,
               font=font_album,
               fill=(255, 255, 255, 255))
    else:
        d.text((int((240 - size_x) / 2), 60),
               name_album,
               font=font_album,
               fill=(255, 255, 255, 255))

    # song
    size_x, size_y, text_x, text_y = text_params(name_song, font_song)
    if size_x > 240:  # if text is too long to fit on the display
        x_song %= (size_x + disp.width)
        d.text((int(text_x - x_song), 100),
               name_song,
               font=font_song,
               fill=(255, 255, 255, 255))
    else:
        d.text((int((240 - size_x) / 2), 100),
               name_song,
               font=font_song,
               fill=(255, 255, 255, 255))

    out = Image.alpha_composite(album_image, txt)

    disp.display(out)
    time.sleep(interval - ((time.time() - t_start) % interval))
