# 📇 Copy Bot 📇
A Simple Bot can copy any media to a destination chat provided!

## Working:
- Add The Bot to Your destination channel as admin
- You can add Bot as admin to any chat (Groups or Channels)
- Bot will copy any media content send in to the above chats to the destination Channel !
- For the above, You need to give a valid channel Id starting with '-100' in the var "Channel_ID"

## USAGE
```
#commmands
No Bot commands, just add bot as admin in your source and destination Chats

#vars
TG_BOT_TOKEN - Your Bot Token (Obtain it from @botfather)
APP_ID - Your APP ID (Obtain it from my.telegram.org)
API_HASH - Your API Hash (Obtain it from my.telegram.org)
CHANNEL_ID - Channel ID to copy medias (Don't forget to fix a prefix '-100')
```

### Deploying on Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/m4mallu/copybot)

### Legendary Way:
#### On Linux Or VPS:

- Make a ```config.py``` file with the above vars (Edit ```sample_config``` and rename it)
- Add Bot as admin in source and destination chats. (Even private chats will also copy)
- Finally, run the following (Don't run as sudo)

```
virtualenv -p python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 bot.py
```

### Credits:
[Dan](https://t.me/huskell) for his [Pyrogram](https://github.com/pyrogram/pyrogram) Library