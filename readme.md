[![link](https://img.shields.io/badge/Python-3.8.0-blue?style=flat-square&logo=python)](https://www.python.org/downloads/) [![link](https://img.shields.io/badge/Caffe-1.0.0-red?style=flat-square&logo=caffe)](https://caffe.berkeleyvision.org/)

This project uses a re-trained version of [Yahoo Open NSFW](https://github.com/yahoo/open_nsfw) to detect images that contain nsfw content(with 400GB of additional training on drawn NSFW pictures, such as hentai.). The docker image is based off the image used in [nsfw-docker](https://github.com/nikos-glikis/nsfw-docker)
=============

<p align="center">
  <img src="https://fuwafuwa.wtf/smug.jpeg">
</p>

api.json
=============
- REPLACE '__REPLACE WITH ACCESS TOKEN__' with your own API key from https://anilist.co/api/v2/oauth/authorize?client_id=2861&response_type=token

FUNCTIONAL
=============
- Scan through profile avatar and rate the avatar on a scale from 0-100% NSFW. (still need to automate page scanning, need to manually enter page number for now.)

- If done correctly it should display something like this. (User ID hidden for privacy.)
<p align="center">
  <img src="https://fuwafuwa.wtf/results.png">
 </p>
- Anything above a 70% is most likely NSFW and will show "^^IS MOST LIKELY NSFW AT %!!^^"
- Anything below a 70% is most likely not NSFW will show "^^IS % NSFW.^^"

WORK IN PROGRESS (TO SOME EXTENT FUNCTIONAL)
=============
- profile_about_name_swear.py pulls words from words.json and looks for them in profile name and about me. MUST ENTER PAGE NUMBER TO WORK.

TO DO
=============
- Scan activity for swear words.
- Scan through banner for NSFW images.
- Scan messages for swear words.
- Scan activity for nsfw images.
- Scan messages for nsfw images.
- Scan profile, messages, activity for illegal links/streaming links.
- Scan for bots.
- Port to discord bot when everything is finished.

GOOGLE COLABORATORY VERSION (to show all profile images on one page.) ( [link](https://colab.research.google.com/drive/1TbAelG8k6txJD_YR66h-_5XxXCuEcCJG) )
=============

*NOTE: MY CODE ISN'T OPTIMIZED. I PUT THIS TOGETHER WHILE HALF ASLEEP. DON'T JUDGE ME.

- Help is greatly appreciated.

