# -*- coding:utf-8 -*-

from io import StringIO
f = StringIO()  #写入StringIO
f.write('hello')
f.write(' ')
f.write('world')
f.write('!')
print(f.getvalue())


#从StringIO中读取
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())  #去掉\n
