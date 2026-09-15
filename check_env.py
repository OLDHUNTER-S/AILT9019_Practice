import os

name = input("输入一个环境变量名：")
print(name in os.environ)