# coding = utf-8
from bs4 import BeautifulSoup		# 网页解析，获取数据
import re 							# 正则表达式，进行文字匹配	
import urllib.request,urllib.error	# 给定网页，获取网页数据
import xlwt							# excel操作
import sqlite3						# SQLite操作

findLink = re.compile(r'<a href="(.*?)">')		#字符串规则
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findImage = re.compile(r'<img.*src="(.*?)".*/>',re.S)
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>',re.S)
findPeople = re.compile(r'<span>(\d*?.*)</span>')
findIntro = re.compile(r'<p class="">(.*?)</p>',re.S)
findInq = re.compile(r'<span class="inq">(.*?)</span>')

def main():
	aurl = "https://movie.douban.com/top250?start="
	datalist = getData(aurl)
	print (datalist)
	dbpath = "Douban250.db"
	# savepath = "DoubanTop250.xls"	#保存到本地excel
	# # askURL(aurl)
	# saveData(datalist,savepath)
	saveDataDB(datalist,dbpath)

def getData(aurl):
	datalist = []
	for i in range(0,10):
		url = aurl + str(i*25)
		html = askURL(url)		#保存获取到的网页源码
		# 解析数据
		soup = BeautifulSoup(html,"html.parser")
		
		for item in soup.find_all('div',class_="item"):	# 查找符合要求的字符串，形成列表
			data = []	#保存一部电影的所有信息
			item = str(item)
			# print(item)
			titles = re.findall(findTitle,item)
			if(len(titles)==2):
				ctitle = titles[0]
				data.append(ctitle)
				atitle = titles[1].replace("/","")
				atitle = re.sub("\xa0","",atitle)
				data.append(atitle)
			else:
				data.append (titles[0])
				data.append ("")

			image = re.findall(findImage,item)[0]
			data.append(image)

			intro = re.findall(findIntro,item)[0]
			intro = re.sub('<br(\s+)?/>(\s+)?',"",intro)	#去掉你个或多个<br/>
			intro = re.sub('/',"",intro)
			intro = re.sub("\xa0","",intro)
			data.append(intro.strip())		# 去除空格
			link = re.findall(findLink,item)[0] 
			data.append(link)

			rating = re.findall(findRating,item)[0]
			data.append(rating)

			people = re.findall(findPeople,item)[0]
			data.append(people)

			inq = re.findall(findInq,item)
			if len(inq) != 0:
				data.append(inq[0])
			else:
				data.append("")

			datalist.append(data)
	return datalist

def askURL(url):
	head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
	request = urllib.request.Request(url,headers=head)

	html = ""
	try:
		response = urllib.request.urlopen(request)
		html = response.read().decode("utf-8")
		# print(html)
	except urllib.error.URLError as e:
		if hasattr(e,"code"):
			print(e,code)
		if hasattr(e,"reason"):
			print(e,reason)
	return html

def saveData(datalist,savepath):
	book = xlwt.Workbook(encoding="utf-8",style_compression=0)
	sheet = book.add_sheet('DoubanTop250',cell_overwrite_ok=True)
	col = ("Chinese Title","Foreign Title","Image Link","Movie Introduction","Movie Detail Link","Rating","Comment Amount","Comment")
	for i in range(0,8):
		sheet.write(0,i,col[i])	#写入列名

	for i in range(0,250):
		print(i+1)
		data = datalist[i]
		for j in range(0,8):
			sheet.write(i+1,j,data[j])

	book.save(savepath)

def saveDataDB(datalist,dbpath):
	init_db(dbpath)
	conn = sqlite3.connect(dbpath)
	cur = conn.cursor()

	for data in datalist:
		for index in range(len(data)):
			data[index] = '"' + str(data[index]) + '"'
		sql = '''
			insert into Douban250(cname,aname,image_link,introduction,detail_link,rating,comment_amount,comment)

			values(%s)'''%",".join(data)

		cur.execute(sql)
		conn.commit()
	conn.close()

def init_db(dbpath):
	sql = '''
	create table Douban250
	(
	id integer primary key autoincrement,
	cname varchar,
	aname varchar,
	image_link text,
	introduction text,
	detail_link text,
	rating text,
	comment_amount text,
	comment text
	)
		'''	
	conn = sqlite3.connect(dbpath)
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.commit()
	conn.close()

if __name__ == '__main__':
	main()
