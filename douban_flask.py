#coding:utf-8
 
from flask import Flask, render_template, request
import sqlite3
import re

app=Flask(__name__)
 
@app.route("/")
def home():
	return render_template("index.html")

@app.route("/index")
def index():
	return home()

@app.route("/Doubantop250")
def db250():
	datalist = []
	con = sqlite3.connect("Douban250.db")
	cur = con.cursor()
	sql = "select * from Douban250"
	data = cur.execute(sql)
	for item in data:
		datalist.append(item)

	cur.close()
	con.close()
	return render_template("Doubantop250.html",datalist=datalist)

@app.route("/DataAnalyze")
def dataanalyze():
	score = []
	amount = []
	id = []
	comment = []
	con = sqlite3.connect("Douban250.db")
	cur = con.cursor()
	sql = "select rating,count(rating) from Douban250 group by rating"
	data = cur.execute(sql)
	for item in data:
		score.append(item[0])
		amount.append(item[1])

	sql2 = "select id,comment_amount from Douban250"
	data = cur.execute(sql2)
	for item in data:
		i = re.findall('\d+',item[1])
		id.append(item[0])
		comment.append(i[0])
	cur.close()
	con.close()
	return render_template("DataAnalyze.html",score=score,amount=amount,id=id,comment=comment)

@app.route("/WordCloud")
def wordcloud():
	return render_template("WordCloud.html")

@app.route("/Contect")
def contect():
	return render_template("Contect.html")

if __name__=="__main__":
	app.run(debug=True,host="127.0.0.1",port=8000) 