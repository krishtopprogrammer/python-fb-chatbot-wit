from wit import Wit
from gnewsclient import gnewsclient


wit_access_token = "23SUJUFV7CV35SX2Z6ZA4NNFRT4VJVIZ"

client = Wit(access_token = wit_access_token)


def wit_response(message_text):

	resp = client.message(message_text)

	categories = {'news_type':None, 'location':None}
	
	entities = list(resp['entities'])

	for entity in entities:
		categories[entity]= resp['entities'][entity][0]['value']

	return categories


def get_news_elements(categories):
	news_client = gnewsclient()
	news_client.query = ''

	if categories['news_type'] != None:
		news_client.query += categories['news_type'] + ' '

	if categories['location'] != None:
		news_client.query += categories['location']

	news_items = news_client.get_news()
	elements =[]

	for item in news_items:
		element = {
					 'title': item['title'],
					 'buttons': [
					 {
					 	'type': 'web_url',
					 	'title': 'Read More',
					 	'url': item['link']

					 }],
					 'image_url': item['img']
		}

		elements.append(element)

	return elements

#print(get_news_elements(wit_response("I want sport news from malaysia")))
