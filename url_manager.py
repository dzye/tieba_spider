#encoding:utf-8
import pymongo
class UrlManager(object):
	def __init__(self):
		client = pymongo.MongoClient('localhost',27017)
		db = client.tieba_db
		self.new_urls = db['new']
		self.old_urls = db['old']

	def add_new_url(self,url):
		if url is None:
			return
		data_url_n = self.new_urls.find_one({'url':url})
		data_url_o = self.old_urls.find_one({'url':url})

		if not data_url_n and not data_url_o:
			self.new_urls.insert({'url':url})

	def has_new_url(self):
		return self.new_urls.find().count() != 0 

	def add_new_urls(self, urls):
		if urls is None or len(urls) == 0:
			return
		for url in urls:
			self.add_new_url(url)


	def get_new_url(self):
		new_url =self.new_urls.find_one()
		self.new_urls.remove({'url':new_url.get("url")})
		self.old_urls.insert({'url':new_url.get("url")})
		return new_url.get("url")
				