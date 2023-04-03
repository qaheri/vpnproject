from telegram.ext import *
import telegram
from telegram import *
import os
import wget
import requests
import json

# stringReadFromFile = open("userdata.json", 'r').read()
# jsonDict = json.loads(stringReadFromFile)

proxy = 'http://127.0.0.1:1080'

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

TOKEN = ""
admins = ['130962237', '72395599']
project_name = "vpn project"

def start(update, context):
    main_keyboard = [[telegram.KeyboardButton("Wallet"),telegram.KeyboardButton("Subscription")],
                     [telegram.KeyboardButton("Proxies")],
                     [telegram.KeyboardButton("Downloads")],
                     [telegram.KeyboardButton("Help and Support")]
                     ]

    param = context.args[0] if context.args else "default"
    
    if param == "default":
        context.bot.send_message(chat_id=update.effective_chat.id, text=
        f"""Hello there, welcome to {project_name}\n Press /help for instructions""",
        reply_markup=telegram.ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True))
    else:
        pass

def help(update, context):
    helpnsupHandler()


def handle_message(update, context):
    if update.message:    
        text = str(update.message).lower()
        
        #print(f'user ({update.message.chat.id}) says: "{text} in: {message_type}"')
        if "hello" in text:
            context.bot.send_message(chat_id=update.effective_chat.id, text="kir")

        elif "Wallet" in text:
            walletHandler()            

        elif "Subscription" in text:
            subHandler()

        elif "Downloads" in text:
            downloads_menu()

        elif "Help and Support" in text:
            helpnsupHandler()

def downloads_menu():
    pass

def helpnsupHandler():
    pass

def walletHandler():
    pass

def subHandler():
    pass

def upHandler(update, context):
    if not hasattr(upHandler, "channel_id"):
         upHandler.channel_id = movies_channel_id
    channel_id = upHandler.channel_id

    if str(update.effective_chat.id) in admins:
        text = str(update.message.text).lower()
        if 'http' in text:
            message = context.bot.send_message(chat_id=update.effective_chat.id, text='Starting to download...')

            def download_progress(current, total , width=80 ):
                if not hasattr(download_progress, "current_percentage"):
                    download_progress.current_percentage = 0
                percentage = str(format((current/total)*100,".2f"))
                if percentage == download_progress.current_percentage:
                    return
                context.bot.edit_message_text(text=f"downloading {percentage}%" ,message_id=message.message_id,chat_id=message.chat.id)
                download_progress.current_percentage = percentage
            
            file_name = wget.download(update.message.text, bar=download_progress)

            context.bot.edit_message_text(text="uploading...",message_id=message.message_id,chat_id=message.chat.id)

            document = open(file_name, 'rb')
            # def upload_progress(current, total):
            #     context.bot.edit_message_text(text=f"uploading {str(int((current/total)*100))}%",message_id=message.message_id,chat_id=message.chat.id)

            final_doc = context.bot.send_document(chat_id=channel_id, document=document)
            # print(final_doc)

            context.bot.edit_message_text(text="uploaded succesfully!",message_id=message.message_id,chat_id=message.chat.id)
            context.bot.edit_message_caption(caption=f"id:{final_doc.message_id}",message_id=final_doc.message_id,chat_id=final_doc.chat.id)
        elif "hello" in text:
            context.bot.send_message(chat_id=update.effective_chat.id, text="kir")

        elif "upload movie" in text:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Download and Upload progress is not set on Movies")
            upHandler.channel_id = movies_channel_id

        elif "upload tvshow" in text:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Download and Upload progress is not set on TV Shows")
            upHandler.channel_id = tvshows_channel_id
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Fuck off")

def create_user():
    os.system("")

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

updater.start_polling()

print("started")

updater.idle()