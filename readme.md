[![link](https://img.shields.io/badge/Python-3.8.0-blue?style=flat-square&logo=python)](https://www.python.org/downloads/) [![link](https://img.shields.io/badge/Caffe-1.0.0-red?style=flat-square&logo=caffe)](https://caffe.berkeleyvision.org/)

A Discord bot used to make AniList mods' lives easier. 
=============

<p align="center">
  <img src="https://fuwafuwa.wtf/smug.jpeg">
</p>

api.json
=============
- REPLACE '__REPLACE WITH ACCESS TOKEN__' with your own API key from https://anilist.co/api/v2/oauth/authorize?client_id=2861&response_type=token
  - Note: Private profiles will not be visible to non-mod users.

.env
=============
- Add your discord bot token after '__DISCORD_TOKEN=__'

FUNCTIONAL
=============
- auto_profile_image.py
  - Scan through profile avatar and rate the avatar on a scale from 0-100% NSFW. (still need enter start page and end page.)

  - Anything above a 70% is most likely NSFW and will show "^^IS MOST LIKELY NSFW AT %!!^^"
  - Anything below a 70% is most likely not NSFW will show "^^Is % NSFW.^^"
  - Users that have not changed their avatars from the default one, will not be searched by the bot, and will not show up in the output either.
  - If done correctly it should display something like this. (User ID hidden for privacy.)
  <p align="center">
    <img src="https://fuwafuwa.wtf/results.png">
   </p>

WORK IN PROGRESS (TO SOME EXTENT FUNCTIONAL)
=============
- profile_about_name_swear.py pulls words from words.json and looks for them in profile name and about me. MUST ENTER PAGE NUMBER TO WORK.

-Porting to Discord, since instead of requests I need to use aiohttp and a few other async functions.

TO DO
=============
- Scan activity for swear words.
- Scan through banner for NSFW images.
- Scan messages for swear words.
- Scan activity for nsfw images.
- Scan messages for nsfw images.
- Scan profile, messages, activity for illegal links/streaming links.
- Scan for bots.


GOOGLE COLABORATORY VERSION (to show all profile images on one page.) ( [link](https://colab.research.google.com/drive/1TbAelG8k6txJD_YR66h-_5XxXCuEcCJG) )
=============

*I'm a n00b. Stop judging me.

- Help is greatly appreciated.
- I forgot about the json libary so I did all the parsing manually, using the replace function, and search functions. I'll update it to use json when I feel like it.
