#encoding:utf-8
from bs4 import BeautifulSoup
import re
import urlparse
import pymongo
class HtmlParser(object):
	def parse(self,page_url,html_cont):
		if page_url is None or html_cont is None:
			return
		soup = BeautifulSoup(html_cont,'html.parser',from_encoding="utf-8")
		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls,new_data

	def _get_new_urls(self,page_url,soup):
		new_urls = []
		links = soup.find_all('a',href=re.compile(r"/f\?kw="))
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url,new_url)
			new_urls.append(new_full_url)
		return new_urls

	def _get_new_data(self,page_url,soup):
		client = pymongo.MongoClient('localhost',27017)
		db = client.tieba_db
		data_db = db['data']	
		title_node =soup.find('a',class_="card_title_fname")
		p_num = soup.find('span',class_='card_menNum')
		t_num = soup.find('span',class_='card_infoNum')
		if not title_node is None:
			if data_db.find_one({'title_node':title_node.get_text().strip()}) is None:
				res_data = {}
				res_data['url'] = page_url
				res_data['title_node']=title_node.get_text().strip()
				res_data['p_num']=p_num.get_text().strip()
				res_data['t_num']=t_num.get_text().strip()
		return res_data

