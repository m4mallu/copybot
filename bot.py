import os
import pyrogram

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

if __name__ == "__main__":
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "copybot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.run()
