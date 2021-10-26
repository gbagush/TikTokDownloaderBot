import telebot
import requests
import json
import urllib
import gspread

api = '2039787121:AAG7eaKxNnwMJAtmFFCGGg2HTPSHnAPNQnc'
bot = telebot.TeleBot(api)

def cid(cid):
	try:
		cidlist = open('cid.txt','r')
		if cid in cidlist:
			cidlist.close()
		else:
			cidlist = open('cid.txt','a')
			cidlist.write('\n{}'.format(cid))
			cidlist.close()
	except:
		pass


@bot.message_handler(commands=['start'])
def send_welcome(message):
	try:
		cid(str(message.chat.id))
		text = '''
Halo!! Selamat datang di bot kami. Silahkan kirimkan link untuk mulai mendownload. 
Join @BagusBotChannel untuk mendapat info terbaru dari bot bot kami.

Dukung kami di https://saweria.co/gbagus
		'''
		bot.send_message(message.chat.id, text)
	except:
		pass

@bot.message_handler(content_types=["text"])
def download(message):
	try:
		chat_id = message.chat.id
		link = requests.get('https://godownloader.com/api/tiktok-no-watermark-free?url={}&key=godownloader.com'.format(message.text))
		link = link.json()
		desc = "{}\n\nDownloaded with @TTDownloaderNoWMbot".format(link["desc"].strip("@godownloader"))
		bot.send_video(chat_id, link["video_no_watermark"], caption=desc)
	except:
		pass

while True:
    try:
        print("bot running") 
        bot.polling()  
    except:
        print('bot restart')
        time.sleep(5)  