import requests
import time
import json
import getpass
from lxml import html

count = 0
session = requests.session()
print "Coupons Loader beta"
username = raw_input('Enter your username: ')
pwd = getpass.getpass('Enter your password: ')

"""
def computeMD5hash(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()
"""

token_auth = 'MDJjMWM0YTctMmI5MC00NjZjLThlMjEtMWFiMTdjZDg4YmU4OjAzMGU3ZGU4YTA2YzY2YWM2ZTYwYTE1NDBjMDUwMWE0ZmQxNzI4ZTU0ZDU0MGJhNjIyOTM3NTIxZTVhNDQ5NjA='
token_post = session.post('https://stopandshop.com/auth/oauth/token', { 'grant_type': 'password', 'username': username,'password': pwd,'client_id':'02c1c4a7-2b90-466c-8e21-1ab17cd88be8' }, headers = { 'Authorization': 'Basic ' + token_auth})

access_token = json.loads(token_post.text)['access_token']
auth_header = { 'Authorization': 'Bearer ' + access_token, 'Content-Type':'application/json' }

print "User Access Token " +access_token


# get user profile for fetching card number  for loading coupon.
profile_url = 'https://stopandshop.com/auth/profile/SNS'
profile_get = session.get(profile_url, headers= auth_header)
user_card_number =  json.loads(profile_get.text)['cardNumber']

#Fetch all coupons for user
offers = session.get('https://stopandshop.com/auth/api/private/synergy/coupons/offers/'+user_card_number +'?&numRecords=1000', headers=auth_header)
#print offers.text
offers_master_list = json.loads(offers.text)['offers']
print "Coupons Available: " + str(len(offers_master_list))

def load_offer(offer_id):
	put_offers = session.put('https://stopandshop.com/auth/api/private/synergy/coupons/offers/' +user_card_number,headers=auth_header,json={"offerNumber": offer_id})
	print put_offers.url

for offer in offers_master_list:
	print offer['title'] + ' ' + offer['description']
	load_offer(offer['id'])
	count += 1
	if((count % 10) == 0):
		print 'Sleeping for 2 seconds'
		time.sleep(2)
