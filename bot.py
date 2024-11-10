# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "@YouTube_Jack_Download_robot",
    api_id=Config.20598977, 
    api_hash=Config.6fdd752f56a5715ea0819e970fb12e9d ,
    bot_token=Config.7342515934:AAEkGWHPMUsGAfXwce_WpJDJHAEBIusJFFw,
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
