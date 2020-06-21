import sqlite3

#1. 打开或创建数据库
# conn = sqlite3.connect("test.db")  

# print("Success!")

# #2. 创建数据表
# c = conn.cursor()

# sql = '''
# create table company
# 	(id int primary key not null,
# 	name int not null,
# 	age int not null,
# 	address char(50))
# '''

# c.execute(sql)
# conn.commit()
# conn.close()

#3. 插入数据

# conn = sqlite3.connect("test.db")
# c = conn.cursor()

# sql = '''
# insert into company	(id,name,age,address)
# values (1,'Alice',18,'London');

# '''
# sql2 = '''
# insert into company	(id,name,age,address)
# values (2,'Bob',23,'Nanjing');

# '''

# c.execute(sql)
# c.execute(sql2)
# conn.commit()
# conn.close()



#4. 查询数据


# conn = sqlite3.connect("test.db")
# c = conn.cursor()

# sql = "select id,name,age,address from company"
# cursor = c.execute(sql)
# for row in cursor:
# 	print('id = ',row[0])
# 	print('name = ',row[1])
# 	print('age = ',row[2])
# 	print('address = ',row[3],"\n")
# conn.close()