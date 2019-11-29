[![link](https://img.shields.io/badge/Python-3.8.0-blue?style=flat-square&logo=python)](https://www.python.org/downloads/)

This project uses [Yahoo Open NSFW](https://github.com/yahoo/open_nsfw) to detect images that contain pornographic content. The docker image is from [nsfw-docker](https://github.com/nikos-glikis/nsfw-docker)
=============

api.json
=============
- REPLACE __REPLACE WITH ACCESS TOKEN__ with your own API key from https://anilist.co/api/v2/oauth/authorize?client_id=2861&response_type=token

FUNCTIONAL
=============
- Scan through profile avatar and rate the avatar on a scale from 0-100% NSFW. (still need to automate page scanning, need to manually enter page number for now.)

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

GOOGLE COLABORATORY (Image) VERSION ( [link](https://colab.research.google.com/drive/1TbAelG8k6txJD_YR66h-_5XxXCuEcCJG) )
=============

*NOTE: MY CODE ISN'T OPTIMIZED. I PUT THIS TOGETHER WHILE HALF ASLEEP. DON'T JUDGE ME.
