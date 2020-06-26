
from bs4 import BeautifulSoup
import urllib.request,urllib.error

def main():
	aurl = "http://demo.qfpffmp.cn/cssthemes6/sleep-8-black/index.html"
	getData(aurl)

def getData(aurl):
	html = askURL(aurl)		#保存获取到的网页源码
		# 解析数据
	soup = BeautifulSoup(html,"html.parser")
	print (soup)

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

if __name__ == '__main__':
	main()