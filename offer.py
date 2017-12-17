import requests
import time
import json
import getpass
from lxml import html
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# disable certificate warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

count = 0
session = requests.session()
print "Coupons Loader beta"

def getMultipleOption(question, valid_input):
	is_valid = False
	while not is_valid:
		answer = raw_input(question + ' ' + str(valid_input) + ': ')
		is_valid = answer in valid_input
		if not is_valid:
			print 'Invalid selection'
	return answer

def buildBaseUrl(brand, environ, qa_server):
	url = ''
	if environ == 'QA':
		if qa_server == '11':
			url = 'https://' + 'wc-' + brand.lower() + 'qa' + qa_server + '.aholdusa.com'
		else:
			url = 'https://' + brand.lower() + 'qa' + qa_server + '.test.peapod.com'
	else:
		url = { 
			'SNS': 'https://stopandshop.com',
			'GC': 'https://giantfoodstores.com',
			'MRTN': 'https://martinsfoods.com',
			'MRTR': 'https://richmond.martinsfoods.com',
			'GNTL': 'https://giantfood.com'
		}[brand]
	return url + '/'
			
brand = getMultipleOption('Select brand', ['SNS','GNTC','MRTN', 'MRTR', 'GNTL'])
environ = getMultipleOption('Select environment', ['QA', 'Prod'])
qa_server = '0'
if environ == 'QA':
	qa_server = getMultipleOption('Select QA server', ['1','2','3','6','9','10','11'])

base_url = buildBaseUrl(brand, environ, qa_server)
print 'Using ' + base_url + '...'

# get base URL.  Defaults to production (www.stopandshop.com)
#base_url = raw_input('Enter your base URL [\'https://stopandshop.com/\']:') or 'https://stopandshop.com/'

# get credentials
username = raw_input('Enter your username: ')
pwd = getpass.getpass('Enter your password: ')

"""
def computeMD5hash(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()
"""

#token_auth = 'MDJjMWM0YTctMmI5MC00NjZjLThlMjEtMWFiMTdjZDg4YmU4OjAzMGU3ZGU4YTA2YzY2YWM2ZTYwYTE1NDBjMDUwMWE0ZmQxNzI4ZTU0ZDU0MGJhNjIyOTM3NTIxZTVhNDQ5NjA='
token_auth =  {
	'SNS': 'MDJjMWM0YTctMmI5MC00NjZjLThlMjEtMWFiMTdjZDg4YmU4OjAzMGU3ZGU4YTA2YzY2YWM2ZTYwYTE1NDBjMDUwMWE0ZmQxNzI4ZTU0ZDU0MGJhNjIyOTM3NTIxZTVhNDQ5NjA=',
	'GNTC': 'ZWVkNDdkZTUtNjFmNC00ZmJiLTg4YjItNzUwYTEwNzhiZjkwOmYxOTgxN2U4N2Y2OTJhODY1NTE3ZTM2MzhlNjJjMDhhNGVjODRhM2ZiZjI2NmRkMTFhYjk2ZmNkM2Y5YTg1ODI=',
	'MRTN': 'N2U3Zjg3ZTktZDY3MS00MzY5LTkyMTItZDI3ZTkzYTI4MTU3OmY2ZmMwMWNlMTIzNzIzNTY2NzE0MWJmOGQ3OTIyZjA0MjhlN2U4MDlmMWU4YWE3OTEyNDRkOWU2OWM4OTZmMzQ=',
	'MRTR': 'N2U3Zjg3ZTktZDY3MS00MzY5LTkyMTItZDI3ZTkzYTI4MTU3OmY2ZmMwMWNlMTIzNzIzNTY2NzE0MWJmOGQ3OTIyZjA0MjhlN2U4MDlmMWU4YWE3OTEyNDRkOWU2OWM4OTZmMzQ=',
	'GNTL': 'NzJkNTBhZDctNjk4MC00OTQxLWFiNGQtNThkYzM0NjVmMDY5OjczMGUyNzgwMDMxNTkwNWMwYThiYzE0ODRmYTUzM2I2NWM0YWI5Mjc4NzdjZTdiZDYyMzUxODcwMWQ0MDY1ODA='
}[brand]

token_post = session.post(base_url + 'auth/oauth/token', { 'grant_type': 'password', 'username': username,'password': pwd,'client_id':'02c1c4a7-2b90-466c-8e21-1ab17cd88be8' }, headers = { 'Authorization': 'Basic ' + token_auth}, verify=False)

access_token = json.loads(token_post.text)['access_token']
auth_header = { 'Authorization': 'Bearer ' + access_token, 'Content-Type':'application/json' }

print "User Access Token " +access_token


# get user profile for fetching card number  for loading coupon.
profile_url = base_url + 'auth/profile/SNS'
profile_get = session.get(profile_url, headers= auth_header, verify=False)
user_card_number =  json.loads(profile_get.text)['cardNumber']

#Fetch all coupons for user
offers = session.get(base_url + 'auth/api/private/synergy/coupons/offers/'+user_card_number +'?&numRecords=1000', headers=auth_header, verify=False)
#print offers.text
offers_master_list = json.loads(offers.text)['offers']
print "Coupons Available: " + str(len(offers_master_list))

def load_offer(offer_id):
	put_offers = session.put(base_url + 'auth/api/private/synergy/coupons/offers/' +user_card_number,headers=auth_header,json={"offerNumber": offer_id}, verify=False)
	print put_offers.url

for offer in offers_master_list:
	print offer['title'] + ' ' + offer['description']
	load_offer(offer['id'])
	count += 1
	if((count % 10) == 0):
		print 'Sleeping for 2 seconds'
		time.sleep(2)
