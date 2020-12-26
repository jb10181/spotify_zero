<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo, twitter_handle, email
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!-- <a href="https://github.com/jb10181/spotify_zero">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">Spotify Connect With Display For Raspberry Pi With Pirate Audio</h3>

  <p align="center">
    Installs raspotify and displays cover art and song information for the currently playing song on a Pirate Audio display.
    <br />
    <!-- <a href="https://github.com/jb10181/spotify_zero"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jb10181/spotify_zero">View Demo</a>
    ·
    <a href="https://github.com/jb10181/spotify_zero/issues">Report Bug</a>
    ·
    <a href="https://github.com/jb10181/spotify_zero/issues">Request Feature</a> -->
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Ping Troubleshooting Tools Screen Shot][product-screenshot]](https://github.com/jb10181/spotify_zero/blob/master/images/image1.jpg)

[![Ping Troubleshooting Tools Screen Shot 2][product-screenshot2]](https://github.com/jb10181/spotify_zero/blob/master/images/image2.jpg)

<!-- [LinkedIn](https://github.com/jb10181/spotify_zero/blob/master/images/generator.png)
https://github.com/jb10181/spotify_zero/blob/master/images/viewer.png -->

<!-- [![Ping Troubleshooting Tools Screen Shot 2][product-screenshot]](https://github.com/jb10181/spotify_zero/blob/master/images/generator.png) -->

I wrote some code to display album cover art and song information for the currently playing song on a Pirate Audio display. This code is to be used in conjunction with raspotify (a project I have no affiliation with).
The key advantage of this over mopidy is that my solution is lightweight, which results in better performance, especially, on a raspberry pi zero.
Text that is too long to fit on the display scrolls, as can be seen in the two still images above.

<!-- Here's a blank template to get started:
**To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`github_username`, `repo`, `twitter_handle`, `email` -->


<!-- ### Built With

* []()
* []()
* []() -->



<!-- GETTING STARTED -->
<!-- ## Getting Started

To get a local copy up and running follow these simple steps. -->

### Prerequisites

The Python packages required to run
<!-- * Python packages -->
```sh
spotipy
```
```sh
os
```
```sh
time
```
```sh
Pillow
```
```sh
requests
```
```sh
io
```
```sh
ST7789
```


### Installation

1. Attach pirate audio to raspberry pi (I used pirate audio with headphone out and a raspberry pi zero)

2. Connect raspberry pi to internet and ssh onto it (or control with GUI)

3. Set a new password
```sh
passwd
```

4. Install all updates
```sh
sudo apt-get update
sudo apt-get upgrade
```

5. Install the required apt packages
```sh
sudo apt-get install python3-rpi.gpio python3-spidev python3-pip python3-pil python3-numpy
sudo apt install libopenjp2-7 libopenjp2-7-dev libopenjp2-tools libatlas-base-dev
```

6. Install the required Python packages
```sh
pip install st7789 numpy Pillow spotipy os time requests io
```

7. Set the following parameters at the bottom of the /boot/config.txt file
```sh
sudo vi /boot/config.txt
```
dtparam=audio=off

dtoverlay=hifiberry-dac
gpio=25=op,dh"

8. Install raspotify
```sh
curl -sL https://dtcooper.github.io/raspotify/install.sh | sh
```

9. Download this project and enter the project directory
```sh
git clone https://github.com/jb10181/spotify_zero
cd spotify_zero
```

10. Create your .credentials file
```sh
spotify_pirate_zero_create_credentials.py
```
If you are not using a GUI to control the raspberry pi, you should run this command on another computer that has a GUI and copy the .credentials file into the spotify_zero directory of the raspberry pi afterwards.


11. Set up the systemd service to run automatically and reboot
```sh
sudo cp spotify_pirate.service /lib/systemd/system/spotify_pirate.service
sudo systemctl daemon-reload
sudo systemctl enable spotify_pirate.service
sudo reboot now
```

<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_ -->



<!-- ROADMAP -->
<!-- ## Roadmap

See the [open issues](https://github.com/jb10181/spotify_zero/issues) for a list of proposed features (and known issues). -->



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

James Burch - [LinkedIn](https://www.linkedin.com/in/burchj/)

Project Link: [https://github.com/jb10181/spotify_zero](https://github.com/jb10181/spotify_zero)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [README template](https://github.com/othneildrew/Best-README-Template)
<!-- * []()
* []() -->





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jb10181/spotify_zero.svg?style=flat-square
[contributors-url]: https://github.com/jb10181/spotify_zero/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jb10181/spotify_zero.svg?style=flat-square
[forks-url]: https://github.com/jb10181/spotify_zero/network/members
[stars-shield]: https://img.shields.io/github/stars/jb10181/spotify_zero.svg?style=flat-square
[stars-url]: https://github.com/jb10181/spotify_zero/stargazers
[issues-shield]: https://img.shields.io/github/issues/jb10181/spotify_zero.svg?style=flat-square
[issues-url]: https://github.com/jb10181/spotify_zero/issues
[license-shield]: https://img.shields.io/github/license/jb10181/ping_troubleshooting.svg?style=flat-square
[license-url]: https://github.com/jb10181/spotify_zero/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/burchj/
[product-screenshot]: https://github.com/jb10181/spotify_zero/blob/master/images/image1.jpg
[product-screenshot2]: https://github.com/jb10181/spotify_zero/blob/master/images/image2.jpg
