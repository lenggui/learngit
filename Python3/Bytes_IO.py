# -*-coding:utf-8-*-

from io import BytesIO
f = BytesIO()  #写入BytesIO
f.write('中文'.encode('utf-8'))
print(f.getvalue())


data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())


