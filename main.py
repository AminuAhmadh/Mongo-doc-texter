import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
from pymongo import MongoClient
import os
import random
import time
from datetime import datetime
import requests
from dotenv import load_dotenv


# function to send a telegram message
def send_telegram(message):
	requests.post(
		'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=markdown'.format(token, chat_id, message))

# function to get a random doc from documents in your db
def get_random_doc():
	count = coll.estimated_document_count()
	return coll.find()[random.randrange(count)]

# load environmental variables
load_dotenv()

# get environmental variables
uri = os.getenv('URI')
client = MongoClient(uri, connect=False)
token = os.getenv('TOKEN')
chat_id = os.getenv('CHAT_ID')


while True:
	print('Connecting to database and collection')
	try:
		# connect to database and collection
		db = client.random
		coll = db.excerpts
		print ('Connected Successfully')
	except Exception as e: # if unable to connect
		print ('Unable to connect due to: ', e)
		client.close()
		time.sleep(10)
		continue
	print ('Getting a random doc...')
	item = get_random_doc()
	print('Doc Obtained')
	msg_type = item['type']
	msg_value = item['value']
	msg_source = item['source']
	msg = msg_type + msg_value + msg_source
	send_telegram (msg)
	print ('Sent telegram')
	print('Done for the day', str(datetime.now()))
	# wait 24 hours
	time.sleep(86400)