"""MLZ BOTZ"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB Unlimited 
	Price 0
	
	**VIP 1 ** 
	Daily  Upload 4GB limit 40GB
	Price Rs 50  🇮🇳/🌎 0.61$  per Month
	
	**VIP 2 **
	Daily Upload 4GB limit Unlimited 
	Price Rs 80  🇮🇳/🌎 0.98$  per Month
	
	
	Pay Using Upi I'd ```?```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/TGxMATRIX")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "?"),
        			InlineKeyboardButton("Paytm",url = "?")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB Unlimited 
	Price 0
	
	**VIP 1 ** 
	Daily  Upload 4GB limit 40GB
	Price Rs 50  🇮🇳/🌎 0.61$  per Month
	
	**VIP 2 **
	Daily Upload 4GB limit Unlimited 
	Price Rs 80  🇮🇳/🌎 0.98$  per Month
	
	
	Pay Using Upi I'd ```?```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/TGxMATRIX")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "?"),
        			InlineKeyboardButton("Paytm",url = "?")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
