# Tag
# NavigableString
# BeautifulSoup
# Comment

from bs4 import BeautifulSoup

file = open("douban.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")		#html,xml,json

# print(type(bs))			#  BeautifulSoup
# print(bs.name)
# print(bs)


# print(bs.title)
# print(type(bs.title)) 		#  Tag	标签及其内容

# print(bs.title.string)
# print(type(bs.title.string))	#  NavigableString	字符串形式返回标签里的内容

# print(bs.a.attrs)		#	字典形式返回标签内所有属性

###	Comment 是特殊的NavigatableString, 输出内容不包含注释符号

### 文档的遍历

# print(bs.head.contents)
# print("---")
# print(bs.head.contents[1])


#	子节点 children 	获取Tag所有子节点，返回一个生成器

# for child in bs.body.children:
# 	print(child)



### 文档的搜索

# t_list = bs.find_all("a")	 # 	列表形式



### 正则表达式搜索

# import re
# t_list = bs.find_all(re.compile("a"))	#	以列表方式输出标签里含有a的标签内所有内容


###	方法搜索, 根据函数的要求来搜索
# def name_is_exists(tag):
# 	return tag.has_attr("name")		#标签里有name属性的

# t_list = bs.find_all(name_is_exists)

# for item in t_list:
# 	print(item)
# print(t_list)


###	kwargs搜索   参数搜索
# t_list = bs.find_all(class_="info")	# id = "" , href = ""
# for item in t_list:
# 	print(item)


### text搜索  参数
# import re
# t_list = bs.find_all(text = re.compile("\d"))	#包含数字的

# t_list = bs.find_all(text=["Douban","db"])


###	limit参数
# t_list = bs.find_all("a", limit = 3)	#只输出特定个数的记录


### css选择器
# t_list = bs.select('title')	#通过标签查找
# t_list = bs.select(".mnav")		#通过类名查找		符号 .
# t_list = bs.select("#content")	#通过id查找		符号 #
# t_list = bs.select("a[class='']")	#标签里的属性
# t_list = bs.select("body > link")


# for item in t_list:
# 	print(item)