import os
from translator import tarjimon

from aiogram import Bot,Dispatcher,types

from aiogram.utils import executor

from flask import Flask , request
TOKEN = os.environ.get('TOKEN')

app = Flask(__name__)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands='start')

async def start_com(message:types.Message):
    await message.answer('Welcome to the translator bot!')

@dp.message_handler(content_types='text')
async def send_message(message:types.Message):
    text  =  message.text
    tarjima = tarjimon(text=text)
    await message.answer(tarjima)

@app.route('/',methods=['GET','POST'])
def hallo_world():
    if request.method == 'GET':
        return 'webhook is working!'
    
    elif request.method == 'POST':
        dp = Dispatcher(bot, None, workers=0)
        return {'ok': True}
    
@app.route('/setwebhook')
def set_webhook():
    s = bot.set_webhook("https://bottranslator.pythonanywhere.com/")
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

if __name__=='__main__':
    executor.start_polling(dispatcher=dp)