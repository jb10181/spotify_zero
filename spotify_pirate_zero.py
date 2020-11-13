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

font_song = ImageFont.truetype(font_path, size=font_song_size)
font_album = ImageFont.truetype(font_path, size=font_album_size)
font_artist = ImageFont.truetype(font_path, size=font_artist_size)


# # Define a function to create rotated text.  Unfortunately PIL doesn't have good
# # native support for rotated fonts, but this function can be used to make a
# # text image and rotate it so it's easy to paste in the buffer.
# def draw_rotated_text(image, text, position, angle, font, fill=(255, 255, 255)):
#     # Get rendered font width and height.
#     draw = ImageDraw.Draw(image)
#     width, height = draw.textsize(text, font=font)
#     # Create a new image with transparent background to store the text.
#     textimage = Image.new('RGBA', (width, height), (0, 0, 0, 0))
#     # Render the text.
#     textdraw = ImageDraw.Draw(textimage)
#     textdraw.text((0, 0), text, font=font, fill=fill)
#     # Rotate the text image.
#     rotated = textimage.rotate(angle, expand=1)
#     # Paste the text into the image, using it as a mask for transparency.
#     # print(image.size[0])
#     print(position)
#     print(width)
#     print(height)
#     if width < 240:
#         static_offset = (position[0] + int((240 - width) / 2), position[1])
#     else:
#         static_offset = position
#     print(static_offset)
#     image.paste(rotated, static_offset, rotated)
#
#
# # Write two lines of white text on the buffer, rotated 90 degrees counter clockwise.
# # im_artist = draw_rotated_text(img, name_artist, (0, 0), 0, font=font_artist, fill=(255, 255, 255))
# # im_album = draw_rotated_text(img, name_album, (0, 60), 0, font=font_album, fill=(255, 255, 255))
# # im_song = draw_rotated_text(img, name_song, (0, 100), 0, font=font_song, fill=(255, 255, 255))


def text_params(name, font):
    size_x, size_y = draw.textsize(name, font)
    text_x = disp.width
    text_y = (80 - size_y) // 2
    return size_x, size_y, text_x, text_y


t_start = time.time()
while True:
    x = (time.time() - t_start) * 1

    img = song_art.resize((HEIGHT, WIDTH))
    draw = ImageDraw.Draw(img)

    # artist
    size_x, size_y, text_x, text_y = text_params(name_artist, font_artist)
    if size_x > 240:
        x %= (size_x + disp.width)
        x = x * size_x
        draw.text((int(text_x - x), 10), name_artist, font=font_artist, fill=(255, 255, 255))
    else:
        draw.text((int((240 - size_x)/2), 10), name_artist, font=font_artist, fill=(255, 255, 255))
    # album
    size_x, size_y, text_x, text_y = text_params(name_album, font_album)
    if size_x > 240:
        x %= (size_x + disp.width)
        x = x * size_x
        draw.text((int(text_x - x), 60), name_album, font=font_album, fill=(255, 255, 255))
    else:
        draw.text((int((240 - size_x)/2), 60), name_album, font=font_album, fill=(255, 255, 255))
    # song
    size_x, size_y, text_x, text_y = text_params(name_song, font_song)
    if size_x > 240:
        x %= (size_x + disp.width)
        x = x * size_x
        draw.text((int(text_x - x), 100), name_song, font=font_song, fill=(255, 255, 255))
    else:
        draw.text((int((240 - size_x)/2), 100), name_song, font=font_song, fill=(255, 255, 255))
    print(size_x)
    print(size_y)
    print(text_x)
    print(text_y)

    disp.display(img)
