#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import math
# def product(*numbers):
# 	sum = 1
# 	for x in numbers:
# 		sum = sum*x
# 	return sum
 

# def trim(s):
# 	while s[:1] == ' ':
# 		s = s[1:]
# 	while s[-1:] == ' ':
# 		s = s[:-2]
# 	return s

# def findMinAndMax(L):
# 	if len(L) == 0:
# 		return (None, None)

# 	minn = L[0]
# 	maxn = L[0]
# 	for x in L:
# 		if minn > x:
# 			minn = x
# 		if maxn < x:
# 			maxn = x
# 	return minn,maxn


# # print(trim('     hello  '))
# # print(findMinAndMax([7,1]))
# # print([m + n for m in range(1,10) for n in range(1,10)])

# # L1 = ['Hello', 'World', 18, 'Apple', None]
# # l2 = [x.lower() for x in L1 if isinstance(x,str)]

# # print(l2)

# def triangles():
# 	L = [1]
# 	while True:
# 		yield L
# 		L.append(0)
# 		L = [L[i-1]+L[i] for i in range(len(L))]
# # n = 0
# # results = []
# # for t in triangles():
# #     print(t)
# #     results.append(t)
# #     n = n + 1
# #     if n == 10:
# #         break


# def normalize(name):
#     s = name[-1:1].lower()
#     s = name[1:].upper()
#     return s

# # L1 = ['adam', 'LISA', 'barT']
# # L2 = list(map(normalize, L1))
# # print(L2)  



# def is_palindrome(n):
# 	return str(n) == str(n)[::-1]


# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))



# def by_name(t):
#     return t[0]

# def by_score(t):
#     return t[1]

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L2 = sorted(L, key=by_score)
# print(L2)

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self._gender = gender
#     def set_gender(self,gender):
#     	self._gender = gender
#     def get_gender(self):
#     	return self._gender


# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')


# class Student(object):
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Student.count +=1
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')

# GUI
# from tkinter import *
# import tkinter.messagebox as messagebox

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Hello, world!')
#         self.helloLabel.pack()
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.quitButton = Button(self, text='Quit', command=self.hello)
#         self.quitButton.pack()

#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message','hello,%s%s'%(name,name))

# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()



import socket
# tcp
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('127.0.0.1',9999))
# # s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()

# udp

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()

# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)

# s.close()

# header,html = data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# with open('sina.html','wb') as f:
#     f.write(html)