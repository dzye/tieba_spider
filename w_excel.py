#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pymongo
import xlwt
from datetime import datetime
import types 
style = xlwt.XFStyle()
# font = xlwt.Font()
# font.name = 'Times New Roman'
# font.bold = True
# style.font = font
# style.font.height = 10
client = pymongo.MongoClient('localhost',27017)
db = client.tieba_db
data_db = db['data']	
book = xlwt.Workbook(encoding = 'utf-8')
sheet1 = book.add_sheet('Sheet 1')
count = 0
for data in data_db.find():
	style.url = data.get("url").encode("utf-8")
	style.title_node = data.get("title_node").encode("utf-8")
	style.p_num = data.get("p_num").encode("utf-8")
	style.t_num = data.get("t_num").encode("utf-8")
	row = sheet1.row(count)
	# print type(url)
	row.write(0,style.url,style)
	row.write(1,style.title_node,style)
	row.write(2,style.p_num,style)
	row.write(3,style.t_num,style)
	count = count + 1
 
book.save('D://example.xls')