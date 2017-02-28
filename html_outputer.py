#encoding:utf-8
import pymongo
class HtmlOutputer(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        db = client.tieba_db
        self.datas = db['data']

    def collect_data(self, data):
        if data is None:
            return
        self.datas.insert(data)