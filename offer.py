import requests
import time
import json
from lxml import html

session = requests.session()

# get login POST url
login_get = session.get('https://www.stopandshop.com/login/')
tree = html.fromstring(login_get.content)
login_url = tree.xpath('//form[@class="login-standalone"]/@action')[0]
print login_url

# expect to get an invalid token
session.get('https://stopandshop.com/auth/api/public/atg/properties?_=' + str(int(time.time()) * 1000))

token_auth = 'MDJjMWM0YTctMmI5MC00NjZjLThlMjEtMWFiMTdjZDg4YmU4OjAzMGU3ZGU4YTA2YzY2YWM2ZTYwYTE1NDBjMDUwMWE0ZmQxNzI4ZTU0ZDU0MGJhNjIyOTM3NTIxZTVhNDQ5NjA='
token_post = session.post('https://stopandshop.com/auth/oauth/token', { 'grant_type': 'client_credentials', 'scope': 'profile' }, headers = { 'Authorization': 'Basic ' + token_auth})

access_token = json.loads(token_post.text)['access_token']
auth_header = { 'Authorization': 'Bearer ' + access_token }

print access_token
auth_cookie = {
	'OAUTH_access_token': access_token
}

# expect to get BCC data
prop_get = session.get('https://stopandshop.com/auth/api/public/atg/properties?_=' + str(int(time.time()) * 1000), headers=auth_header, cookies=auth_cookie)
#print prop_get.content

#login_get = session.get('https://www.stopandshop.com/login/', headers=auth_header, cookies=auth_cookie)
#print login_get.headers

payload = {
			'username': 'aaron.watson@ahold.com',
		 	'password': 'not_my_password',
			'/atg/userprofiling/ProfileFormHandler.loginSuccessURL': 'https://stopandshop.com?cmPageId=login&cmLocation=standalone',
			'/atg/userprofiling/ProfileFormHandler.loginErrorURL': '/login/',
			'/atg/userprofiling/ProfileFormHandler.login': 'log in'
		  }
'''
login_header = {
	'Host': 'stopandshop.com',
	'Connection': 'keep-alive',
	'Pragma': 'no-cache',
	'Cache-Control': 'no-cache',
	'Referer': 'https://stopandshop.com/login/',
	'Origin': 'https://stopandshop.com',
	'Upgrade-Insecure-Requests': 1,
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.8'
}
'''
login_post = session.post(login_url, payload, cookies=auth_cookie)
#print login_post.request.headers
print login_post.status_code
print login_post.content

'''
response = session_requests.post('https://stopandshop.com/login.jsp?DARGS=/WEB-INF/jsp/common/blocks/form/login-form-standalone-block.jsp.loginBlock' + rando_login, data=form)
offers = session_requests.get('https://stopandshop.com/dashboard/coupons-deals/', cookies=response.cookies)
print offers.url
'''
