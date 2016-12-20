# -*- coding:utf-8 -*-

class Person(object):   #创建类，object-->基类
    def __init__(self,height,weight,age,sex):  #初始化
        self.height = height   #数据属性
        self.weight = weight
        self._age = age
        self._sex = sex
    def Sex(self):   #方法属性
        print u'性别：%s' % self._sex
    def Age(self):
        print u'年龄： %s' % self._age

class Leng_gui(Person):   #类的继承，可以单继承，可以多重继承（优先第一继承类），派生类
    def __init__(self,name,height,weight,hobby,age,sex):
        Person.__init__(self,height,weight,age,sex)  #继承父类的初始化，
        self.name = name
        self.hobby = hobby
    def My_birthday(self):  #重新定义方法
        print '1995-08-22'

class Lisa(Person):
    def __init__(self,name,height,weight,hobby,age,sex):
        super(Lisa,self).__init__(height,weight,age,sex)
        self._name = name
        self.hobby = hobby
        

#__init__  布局初始化,实现继承的的特有，如果继承全部基类，可不加__init__    
        
