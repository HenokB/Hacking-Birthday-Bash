import cohere
co = cohere.Client('{cohere api key}')
response = co.generate(
  model='xlarge',
  prompt='This is a birthday wish and gift generator.\n-\nWish: Happy birthday to you. From good friends and true, from old friends and new, may good luck go with you and happiness too!\nGift: Cake\n-\nWish: Happy birthday! You are only young once so enjoy it to the fullest. Time passes way too fast and you don’t get these years back.\nGift: Bracelet\n-\nWish: Thinking of you on your birthday, and wishing you all the best! I hope it is as fantastic as you are!\nGift: Books\n-',
  max_tokens=50,
  temperature=0.9,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=["-"],
  return_likelihoods='NONE')
g=str('Here you go: {}'.format(response.generations[0].text))
print(g)


from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("{telegram api key}",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello, Welcome to the Birthday Helper Bot.Please write\
		/help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/generate - To generate birthday wish and gifts
  /about - This bot is made by Henok for Happy Birthday Bash
	""")
 
def generated(update: Update, context: CallbackContext):
    update.message.reply_text(g) 

def about(update: Update, context: CallbackContext):
    update.message.reply_text("Hello I'm Henok check out my github https://github.com/HenokB")     

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('generate', generated))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('about', about))

updater.start_polling()
