
#coding:utf-8
 
from flask import Flask, render_template, request
import datetime

app=Flask(__name__)

## 字符串参数
 
@app.route("/index")
def index():
	return "<h1>Acceber's Website</h1>"
 
@app.route("/user/<name>")
def user(name):
	return "<h1>Hello,%s</h1>"%name

@app.route("/user/<int:id>")	#<float:id>
def id(id):
	return "<h1>Hello,%dUser</h1>"%id


## 路由途径不能重复，用户通过唯一路径访问不同函数

 
# @app.route("/")
# def index2():
# 	return render_template("index2.html") # 返回template的html


## 向页面传变量

@app.route("/")
def index3():
	date = datetime.date.today() #普通变量
	name = ["Alice","Bob","Candy"]	#列表
	game = {"game":"Overwatch","hero":"doomfist","HP":250,"skill":"rising uppercut"} #字典

	return render_template("index2.html", date=date, name=name, game=game)


## 表单提交

@app.route("/signup")
def signup():
	return render_template("signup.html")

@app.route("/result", methods=['POST','GET'])
def result():
	if request.method == 'POST':
		result = request.form

		return render_template("result.html",result=result)

if __name__=="__main__":
	app.run(debug=True,host="127.0.0.1",port=8000)