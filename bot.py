import telebot 
from telebot import types
import textdistance
from emoji import emojize
import emoji
import re 
import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', '8443'))

TOKEN="1248191854:AAEh41zv8eG2F6RpxAp431pQNHHUja9SYjc"

APP_NAME="kecbot"

bot = telebot.TeleBot(TOKEN)

def main():
    updater = Updater(TOKEN, use_context=True)
    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",port=PORT,url_path=TOKEN)
    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    updater.bot.set_webhook(APP_NAME + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

company={
    "AMAZON":{"2020":"https://www.geeksforgeeks.org/amazon-sde-1-interview-experience-amazon-wow-2020/?ref=leftbar-rightbar",
	 "2019":"https://www.geeksforgeeks.org/amazon-interview-set-19/?ref=lbp",
	 "2018":"https://www.geeksforgeeks.org/amazon-recruitment-process/"},

    "ACCENTURE":{"2020":"https://www.geeksforgeeks.org/accenture-on-campus-2020-placement-drive/",
	 "2019":"https://www.geeksforgeeks.org/accenture-interview-experience-on-campus-2019/?ref=rp"},
    
    "CODA GLOBAL":{"2020":"https://www.geeksforgeeks.org/coda-global-interview-experience/"},
	 
    "CTS":{"2020":"https://www.geeksforgeeks.org/cognizant-interview-experience-for-2020-passout-batch/",
	 "2019":"https://www.geeksforgeeks.org/cognizant-interview-experience-on-campus/",
	 "2018":"https://www.geeksforgeeks.org/cognizant-technology-solutions-interview-experience-on-campus-2018/?ref=rp"},

    "CODINGMART":{"2020":"https://www.geeksforgeeks.org/coding-mart-technology-interview-experience/",
	 "2019":"https://www.geeksforgeeks.org/coding-mart-technology-interview-experience/",
	 "2018":"https://www.geeksforgeeks.org/coding-mart-interview-experience/?ref=lbp"},

    "CODE BRAHMA":{"2020":"https://www.glassdoor.co.in/Interview/Codebrahma-Interview-Questions-E1082922.htm",
	 "2019":"https://www.glassdoor.co.in/Interview/Codebrahma-Interview-Questions-E1082922.htm",
	 "2018":"https://www.glassdoor.co.in/Interview/Codebrahma-Interview-Questions-E1082922.htm"},
    
    "FINANCIAL SOFTWARE SYSTEM":{"2020":"https://www.geeksforgeeks.org/financial-software-systems-pvt-ltd-interview-experience/?ref=rp"},

    "HEXAWARE":{"2020":"https://prepinsta.com/hexaware/recruitment-process/"},
	 
    "HCL":{"2020":"https://www.geeksforgeeks.org/hcl-recruitment-process/"},
	 
    "HONEYWELL":{"2020":"https://www.geeksforgeeks.org/honeywell-interview-experience-on-campus-2020/?ref=lbp",
	 "2019":"https://www.geeksforgeeks.org/honeywell-interview-experience-set-2-campus/?ref=lbp",
	 "2018":"https://www.geeksforgeeks.org/honeywell-interview-experience-set-3-campus/?ref=lbp"},

    "INFOSYS":{"2020":"https://www.geeksforgeeks.org/infosys-recruitment-process/",
	 "2019":"https://www.geeksforgeeks.org/infosys-interview-experience-on-campus-2019-for-the-role-of-system-engineer/?ref=rp",
	 "2018":"https://www.geeksforgeeks.org/infosys-campus-placement-experience/"},

    "IVTL INFOVIEW":{"2020":"https://www.geeksforgeeks.org/ivtl-infoview-interview-experience-how-i-got-selected-be-2020-batch/?ref=lbp",
	 "2019":"https://www.geeksforgeeks.org/ivtl-infoview-technologies-pooled-off-campus-drive-2019-passed-outs/?ref=lbp",
	 "2018":"https://www.geeksforgeeks.org/infoview-technologies-ivtl-interview-experience-set-1-pool-drive/?ref=lbp"},

    "KAAR TECHNOLOGIES":{"2020":"https://www.geeksforgeeks.org/kaar-technologies-interview-experience-on-campus-2021/"},
  
    "L&T INFOTECH":{"2020":"https://www.geeksforgeeks.org/lt-infotech-interview-experience-on-campus-2020-virtual/",
	 "2019":"https://prepinsta.com/lti-4__trashed/interview-questions/",
	 "2018":"https://www.geeksforgeeks.org/l-t-infotech-interview-experience-on-campus-sept-2018/?ref=rp"},

    "MALLOW TECHNOLOGIES":{"2020":"https://www.geeksforgeeks.org/mallow-technologies-interview-experience-set-1-on-campus/"},
	
    "ORACLE":{"2020":"https://www.geeksforgeeks.org/oracle-interview-experience-campus-placements-2020/",
	 "2019":"https://www.geeksforgeeks.org/oracle-recruitment-process/"},
	 
    "SIRIUS":{"2020":"https://www.skillrack.com/qn/418"},
	
    "SOLITON":{"2020":"https://prep.placementseason.com/companies/soliton/"},
	 
    "TCS":{"2020":"https://www.geeksforgeeks.org/tcs-digital-interview-experience-on-campus-2020/",
	 "2019":"https://www.geeksforgeeks.org/tcs-interview-experience-on-campus-2019/",
	 "2018":"https://www.geeksforgeeks.org/tcs-on-campus-interview-experience-2018/"},

    "TRIMBLE":{"2020":"https://www.geeksforgeeks.org/trimble-technology-interview-experience-on-campus/?ref=rp",
	 "2019":"https://www.geeksforgeeks.org/trimble-interview-experience/?ref=lbp"},
	
    "VINAYAK INFOTECH":{"2018":"https://nehruplacements.com/index.php/2018/10/08/vinayak-infotech-campus-placement-drive-for-2018-2019-passing-out-batch-mca-arts-students-on-17102018-at-ngi/"},
	
    "VURAM TECHNOLOGY":{"2020":"https://www.geeksforgeeks.org/vuram-technology-solutions-interview-experience-on-campus-2020/",
	 "2019":"https://www.geeksforgeeks.org/vuram-technology-solutions-interview-experience/?ref=rp"},
	
    "WIPRO":{"2020":"https://www.geeksforgeeks.org/wipro-interview-experience-on-campus-3/?ref=lbp",
	 "2019":"https://www.geeksforgeeks.org/wipro-interview-experience-set-2-on-campus/?ref=rp",
	 "2018":"https://www.geeksforgeeks.org/wipro-interview-experience-on-campus-2018/"},

    "XORIANT":{"2020":"https://www.geeksforgeeks.org/xoriant-interview-experience-set-2-campus/?ref=lbp",
	 "2019":"https://www.geeksforgeeks.org/xoriant-interview-experience-on-campus/?ref=lbp",
	 "2018":"https://www.geeksforgeeks.org/xoriant-interview-experience-set-3-campus/?ref=lbp"},

    "ZOHO":{"2020":"https://www.geeksforgeeks.org/zoho-software-developer-interview-experience/?ref=lbp",
	 "2019":"https://www.geeksforgeeks.org/zoho-software-developer-interview-experience/",
	 "2018":"https://www.geeksforgeeks.org/zoho-interview-set-2-campus/"}
	 
}
placement={
"AMCAT":"https://drive.google.com/drive/folders/1XBH6xAqK-uFrR8dA709beDiOMlmNeW86",
 
"aptitude":"https://drive.google.com/drive/folders/1ucwDVE8ADFdCIGzPhVj5LEK_QD_1ydHF",

"backtobackswe(CODING)":"https://drive.google.com/drive/folders/1G4wSlEfQ8zTRvCecVp4seNZTUBy8C0Ca",

"coding interveiw books":"https://drive.google.com/drive/folders/1Ac1JDncC5fVLSu-AT9HT96o7mULmCIGi",

"Cse subjects":"https://drive.google.com/drive/folders/1-fXbz3NzdsUu07rGh1scvw0rpDfjMakI",

"Data structures and algorithms":"https://drive.google.com/drive/folders/1Eejr2aQVGki5OcjnO6bz7Pnh-FdYC8hX",

"Data structures and algorithms":"https://drive.google.com/drive/folders/1UomkVvR_t7RfXlyH0zXKG70IGdI2TcJ3",

"Data structures problems":"https://drive.google.com/drive/folders/1IrO6CQRjiWyafQzLUxmH4dNI7SN-h33V",

"dbms":"https://drive.google.com/drive/folders/1WTIDZr68KPMtnieF16wuuHLQJ4u80PEU",

"OS MITRA SLIDES":"https://drive.google.com/drive/folders/1pPD_D2IfPCS_85sML2XaaXi_XrjV9ptt",

"PSEUDOCODE PAPERS":"https://drive.google.com/drive/folders/1otG08ljZK5LJdalXf7Li7KM_DABJ0w4-",

"PUZZLES":"https://drive.google.com/drive/folders/1Ga4lSXXLGzytdD3-ms482pGcP39-xSji",

}
date = {
 "ACCENTURE":"",
 
 "Audi Time":"",

 "CAPGEMINI":"",

 "CISCO":"",

 "COCUBES":"",

 "Cognizant":"",

 "CTS":"",

 "Delloite":"",

 "COGNIZANT":"",

 "DEVSQUARE":"",

 "ELITMUS":"",

 "EPAM":"",

 "HCL":"",

 "HEXAWARE":"",

 "HUAWEITECH":"",

 "IBM":"",

 "INFOSYS":"",

 "INFOSYS":"",

 "ion idea":"",

 "L-T":"",

 "LG soft":"",

 "Lumen Data":"",

 "MINDTREE":"",

 "MPHASIS":"",

 "ROBERT BOSCH":"",

 "SECURE EYES":"",

 "SOPRA STERIA":"",

 "TCS":"",

 "TCS":"",

 "TECH MAHINDRA":"",

 "TEK SYSTEM":"",

 "UNISYS":"",

 "WIPRO":"",

 "ZENPACT":"",

 "ZENQ":"",

 "ZOHO":"",
 
}
stringList = {
 "ACCENTURE":"https://drive.google.com/drive/folders/1qX8d4oddHKwjvsyg1q85aYxG9URB-Sam",
 
 "Audi Time":"https://drive.google.com/drive/folders/1PQOf4bqUFCiBiDub4uW0k3FX1LllsPqA",

 "CAPGEMINI":"https://drive.google.com/drive/folders/1AHdnnAf0DtyLzdFBUUsffr8-LnVFnL2m",

 "CISCO":"https://drive.google.com/drive/folders/1-1SpYYrwsJ4XGxXMOPaRY_1r41P2T5pC",

 "COCUBES":"https://drive.google.com/drive/folders/1ZFJuvk9cBBADMlUHec0keI5nYUjnWeso",

 "Cognizant":"https://drive.google.com/drive/folders/17JkMwcJQ2VBFnu5dHw2_RPyXdb3F2pSX",

 "CTS":"https://drive.google.com/drive/folders/1VXOegby3helZv3ciMzZ0i4zXjh13V-ii",

 "Delloite":"https://drive.google.com/drive/folders/1gZW5k4AovleKIYiT5swHjpxlWI6P-L03",

 "COGNIZANT":"https://drive.google.com/drive/folders/1mxSiVWPJQSOjn0_4WN8KjZz5hNgflGPi",

 "DEVSQUARE":"https://drive.google.com/drive/folders/1_JInbdeYUNF_C5NqvdocRO7LGt-6fkgF",

 "ELITMUS":"https://drive.google.com/drive/folders/1lPhEUE1G-vzX2anqorhtlT3uavJ1hS6U",

 "EPAM":"https://drive.google.com/drive/folders/1VG6cin-eYetqSamWVav0IkQm4dNrmKoh",

 "HCL":"https://drive.google.com/drive/folders/1ebhf6rztI_Y0Gel4R_8vsty9teqK7Jdk",

 "HEXAWARE":"https://drive.google.com/drive/folders/1U1uY-MFKdXLohKQHzE3P7Q_H7Luet9Nd",

 "HUAWEITECH":"https://drive.google.com/drive/folders/1LUnNrLbazMTufQHlz7RT_Ez8jPcGzWpM",

 "IBM":"https://drive.google.com/drive/folders/15Ilutodp8D3xlqDa7_kOf3gb_qjRGGQN",

 "INFOSYS":"https://drive.google.com/drive/folders/1Zma-zvgkZOMFbLJIm2uTwUWR57zPUGtw",

 "INFOSYS":"https://drive.google.com/drive/folders/1wIBHhXlozQkBfFIO1lWxRgztsSvj3NWf",

 "ion idea":"https://drive.google.com/drive/folders/17X1P-n4LuAXeGlZon-6Nn3cKbGI3RQfg",

 "L-T":"https://drive.google.com/drive/folders/1eNxCCeQTffomZgsP9kecNu0yk70rST0s",

 "LG soft":"https://drive.google.com/drive/folders/1JKQibJCQj2ceee3-qejwSmKdWUiak5rZ",

 "Lumen Data":"https://drive.google.com/drive/folders/1mWB5V-NH2BGPzZAlFHtF-HVhdNfPggH9",

 "MINDTREE":"https://drive.google.com/drive/folders/1TSaYiz8koVcRSAE-bFFVO_AgRcbmz67u",

 "MPHASIS":"https://drive.google.com/drive/folders/1R9ldTuw5XTJ4ZDhEzq_EJTCUfaCG4tSE",

 "ROBERT BOSCH":"https://drive.google.com/drive/folders/1Ep3rwCnHgY9Tek78lAU4kRmpb_pzWX6P",

 "SECURE EYES":"https://drive.google.com/drive/folders/1UwDLMyzXcX07-0401_5jjxIlmSdg6T9G",

 "SOPRA STERIA":"https://drive.google.com/drive/folders/19iiqPJ4OuvnRkph0B5hIuFl3ZGpAJ75J",

 "TCS":"https://drive.google.com/drive/folders/1z2etAZ6xLs25adO6jtZsfULGJQKiDjbE",

 "TCS":"https://drive.google.com/drive/folders/1ofk2s4i82s4MRX5u147Rqu1Gb9tZX7hv",

 "TECH MAHINDRA":"https://drive.google.com/drive/folders/1Dmw2Aq2YYGHJRAPkPmjxxRVk_xgQpzpp",

 "TEK SYSTEM":"https://drive.google.com/drive/folders/1i6UVWii27wrWmqifoNGZd2nz0PM64awe",

 "UNISYS":"https://drive.google.com/drive/folders/1dPivS8D2VvA9iG8OQes0uSt-X-rPUz-0",

 "WIPRO":"https://drive.google.com/drive/folders/145hMnepwGrowRXJDnjInEWtr1NbDzQUm",

 "ZENPACT":"https://drive.google.com/drive/folders/1YcBq6tA3BGTALRCA6zc0NATgnsgdvIXz",

 "ZENQ":"https://drive.google.com/drive/folders/1sclNf9n34-TcQH48AbYLn8IgnovE39z8",

 "ZOHO":"https://drive.google.com/drive/folders/1EtXkhhxviVc_orwQk78wAwav-cut63Yr",

}
@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "how are you doing?",reply_markup=makeKeyboard())
'''test = ["Company prep materials","Company Experience","Company Expected date"]
def makeKeyboard():
    markup = types.InlineKeyboardMarkup()
    row=[]
    for key,value in l.items():
    	if("infosys"==key):
    		for data,val in value.items():
        		row.append(types.InlineKeyboardButton(text=data,callback_data=data))
    markup.row(*row)
    return markup'''
'''@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
	#for key, value in stringList.items():
	bot.send_message(call.message.chat.id, call.data)
	#if(call.data=="Company prep materials"):

	#bot.answer_callback_query(callback_query_id=call.id,text="heloooooooo" '''
@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_message(message.chat.id, 'Welcome '+str(message.from_user.first_name)+"😊\nEnter Your 🏫 kongu Mailid 👇")

# Here's a simple handler when user presses button with "Button 1" text
@bot.message_handler(content_types=["text"], func=lambda message:message.text=="Company Preparation Materials")
def func1(message):
	markup = types.InlineKeyboardMarkup()
    #row=[]
    #row.append(types.InlineKeyboardButton(text=data,callback_data=data))
	markup.row(*[types.InlineKeyboardButton(text="✳️ List",callback_data="lcm"),types.InlineKeyboardButton(text="⚛️ Type",callback_data="tcm")])
	bot.send_message(message.chat.id,"🏢Company Preparation Materials🏢\nDo You Want to ......\n✳️ Display list of companies\nOr\n⚛️ Type the company name\n✅Select the below button 👇",reply_markup=markup)
	'''keyboard = types.InlineKeyboardMarkup()
	for key, value in stringList.items():
	    button1 = types.InlineKeyboardButton(text=key.upper(),url=value)
	    keyboard.add(button1)
	bot.send_message(message.chat.id, 
"Select from the below listed companies\n----------------------------------------------------\nOtherwise\n----------------------------------------------------\nType the company name 🏢 as ➡️ cm.companyname\nFor Eg ➡️ cm.oracle ",reply_markup=keyboard) '''
@bot.message_handler(content_types=["text"], func=lambda message:message.text=="Company Experience")
def func1(message):
	markup = types.InlineKeyboardMarkup()
	markup.row(*[types.InlineKeyboardButton(text="✳️ List",callback_data="lce"),types.InlineKeyboardButton(text="⚛️ Type",callback_data="tce")])
	bot.send_message(message.chat.id,"🏢Company Experience🏢\nDo You Want to ......\n✳️ Display list of companies\nOr\n⚛️ Type the company name\n✅Select the below button 👇",reply_markup=markup)
	
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
	if(call.data=="lcm"):
		keyboard = types.InlineKeyboardMarkup()
		for key, value in stringList.items():
			button1 = types.InlineKeyboardButton(text=key.upper(),url=value)
			keyboard.add(button1)
		bot.send_message(call.message.chat.id, "🏢 LIST OF COMPANY 🏢",reply_markup=keyboard)
		bot.send_message(call.message.chat.id, "✅ Select from the above listed companies 👆👆👆")
	elif(call.data=="tcm"):
		bot.send_message(call.message.chat.id, "Type the company name 🏢 as \n👉 cm.companyname\nFor Example \n👉 cm.TCS") 
	elif(call.data=="lce"):
		keyboard = types.InlineKeyboardMarkup()
		for key, value in company.items():
			button1 = types.InlineKeyboardButton(text=key.upper(),callback_data="ce."+key)
			keyboard.add(button1)
		bot.send_message(call.message.chat.id, "🏢 LIST OF COMPANY 🏢",reply_markup=keyboard)
		bot.send_message(call.message.chat.id, "✅ Select from the above listed companies 👆👆👆")
	elif(call.data=="tce"):
		bot.send_message(call.message.chat.id, "Type the company name 🏢 as \n👉 ce.companyname\nFor Example \n👉 ce.TCS") 
	elif(call.data[:3]=="ce."):
		markup = types.InlineKeyboardMarkup()
		row=[]
		for key,value in company.items():
			if(call.data[3:]==key):
				for data,val in value.items():
					row.append(types.InlineKeyboardButton(text=data,url=val))
		markup.row(*row)
		bot.send_message(call.message.chat.id,call.data[3:]+" EXPERIENCE",reply_markup=markup)


@bot.message_handler(content_types=["text"], func=lambda message:True)
def func1(message):
	if(re.search("kongu.edu",message.text.lower())):
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
		button1 = types.KeyboardButton(text="Company Preparation Materials")
		button2 = types.KeyboardButton(text="Company Experience")
		button3 = types.KeyboardButton(text="Company Expected Date")
		keyboard.add(button1, button2, button3)
		bot.send_message(message.chat.id, "select option from below list", reply_markup=keyboard)
	if(message.text[:2]=='cm' or message.text[:2]=='CM'):
		message.text=message.text[3:]
		for key, value in stringList.items():
			message.text=message.text.lower()
			key=key.lower()
			if(message.text==key or textdistance.hamming.normalized_similarity(message.text,key)>0.60):
			    keyboard = types.InlineKeyboardMarkup()
			    url_btn = types.InlineKeyboardButton(url=value, text="Go to the link")
			    keyboard.add(url_btn)
			    bot.send_message(message.chat.id, key.upper() +" PLACEMENT MATERIALS", reply_markup=keyboard)
	elif(message.text[:2]=='ce' or message.text[:2]=='CE'):
		message.text=message.text[3:]
		markup = types.InlineKeyboardMarkup()
		row=[]
		for key,value in company.items():
			message.text=message.text.lower()
			key=key.lower()
			if(message.text==key or textdistance.hamming.normalized_similarity(message.text,key)>0.60):
				for data,val in value.items():
					row.append(types.InlineKeyboardButton(text=data,url=val))
		markup.row(*row)
		bot.send_message(message.chat.id,message.text.upper() +" EXPERIENCE",reply_markup=markup)

		#if(f==0):
		#	bot.send_message(message.chat.id,"SORRY IT'S NOT AVAILABLE")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()

   
   
 

