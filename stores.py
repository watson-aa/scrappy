import urllib2
from lxml import html
import csv

#base_url = 'http://giantfood.com'
#base_url = 'http://giantfoodstores.com'
base_url = 'http://stopandshop.com'

#data = '_dyncharset=UTF-8&store-location=washington%2C+dc&_D%3Astore-location=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Arefine-distance=+&refine-distance=999&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.opco=GNTL&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.opco=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.storeType=GROCERY&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.storeType=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.previousSearchAddress=washington%2C+dc&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.previousSearchAddress=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.latitude=38.9071923&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.latitude=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.longitude=-77.0368707&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.longitude=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.successUrl=&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.successUrl=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.errorUrl=&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.errorUrl=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.displayCount=999&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.displayCount=+&searchByAddressSubmit=modify+search&_D%3AsearchByAddressSubmit=+&_DARGS=%2FWEB-INF%2Fjsp%2Fstore%2Flocator%2Fstore-locator-form.jsp.refine-search-results'
#data = '_dyncharset=UTF-8&store-location=carlisle%2C+pa&_D%3Astore-location=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Arefine-distance=+&refine-distance=999&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.opco=GNTC&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.opco=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.storeType=GROCERY&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.storeType=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.previousSearchAddress=carlisle%2C+pa&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.previousSearchAddress=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.latitude=40.2010241&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.latitude=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.longitude=-77.20027449999999&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.longitude=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.successUrl=&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.successUrl=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.errorUrl=&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.errorUrl=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.displayCount=999&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.displayCount=+&searchByAddressSubmit=modify+search&_D%3AsearchByAddressSubmit=+&_DARGS=%2FWEB-INF%2Fjsp%2Fstore%2Flocator%2Fstore-locator-form.jsp.refine-search-results'
data = '_dyncharset=UTF-8&store-location=quincy%2C+ma&_D%3Astore-location=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Afilters=+&_D%3Arefine-distance=+&refine-distance=999&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.opco=STSH&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.opco=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.storeType=GROCERY&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.storeType=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.previousSearchAddress=&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.previousSearchAddress=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.successUrl=&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.successUrl=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.errorUrl=&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.errorUrl=+&%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.displayCount=999&_D%3A%2Fahold%2Fstoreinformation%2Fformhandler%2FStoreSearchFormHandler.displayCount=+&searchByAddressSubmit=find&_D%3AsearchByAddressSubmit=+&_DARGS=%2FWEB-INF%2Fjsp%2Fstore%2Flocator%2Fstore-locator-form.jsp.refine-search-results'

url = base_url + '/store/locator/?_DARGS=/WEB-INF/jsp/store/locator/store-locator-form.jsp.refine-search-results'
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
result = response.read()

stores_tree = html.fromstring(result)
store_urls = stores_tree.xpath('//ul[@class="location-details"]/li/div[@class="location"]/div[@class="location-info"]/p[@class="view-store-details"]/a/@href')

store_data = []
rx_data = []
phone_data = []

for url in store_urls:
	req_detail = urllib2.Request(base_url + url, None)
	response = urllib2.urlopen(req_detail)
	result = response.read()

	detail_tree = html.fromstring(result)
	store_num = detail_tree.xpath('//div[@id="main-content"]/div[@class="store-details"]/h1/text()')[0]
	store_num = store_num[store_num.find('#')+1:]

	print store_num
	store_hours = detail_tree.xpath('//div[@class="hours tile sidebar outline"]/h3[text()="store hours"]/following-sibling::div[@class="tile-panel"]/ul/li')
	rx_hours = detail_tree.xpath('//div[@class="hours tile sidebar outline"]/h3[text()="pharmacy hours"]/following-sibling::div[@class="tile-panel"]/ul/li')

	store_phone = detail_tree.xpath('//div[@class="location-details"]/div[@class="location"]/ul/li/h3[text()="store phone"]/following-sibling::p/text()')
	if len(store_phone) > 0:
		store_phone = store_phone[0]
	else:
		store_phone = ''

	rx_phone = detail_tree.xpath('//div[@class="location-details"]/div[@class="location"]/ul/li/h3[text()="pharmacy phone"]/following-sibling::p/text()')
	if len(rx_phone) > 0:
		rx_phone = rx_phone[0]
	else:
		rx_phone = ''

	phone_data.append([store_num, store_phone, rx_phone])

	hour_data = [store_num]
	for hour in store_hours:		
		if len(hour.xpath('span[@class="time-span"]/text()')) > 0:
			store_data.append([store_num, hour.xpath('span[@class="time-span"]/text()')[0], hour.xpath('span[@class="time-open"]/text()')[0].replace('A', 'AM')])

	for hour in rx_hours:
		if len(hour.xpath('span[@class="time-span"]/text()')) > 0:
			rx_data.append([store_num, hour.xpath('span[@class="time-span"]/text()')[0], hour.xpath('span[@class="time-open"]/text()')[0].replace('A', 'AM')])

	#break


f = open('store_phone.csv', 'wt')
writer = csv.writer(f)
writer.writerow( ['store', 'phone', 'rx phone'] )
for row in phone_data:
	writer.writerow(row)
f.close()

f = open('store_hours.csv', 'wt')
writer = csv.writer(f)
writer.writerow( ['store', 'day', 'hours'] )
for row in store_data:
	writer.writerow(row)
f.close()

f = open('rx_hours.csv', 'wt')
writer = csv.writer(f)
writer.writerow( ['store', 'day', 'hours'] )
for row in rx_data:
	writer.writerow(row)
f.close()