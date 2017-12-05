from module import *
from moduleElement import *

class Student(object):
    modules = []
    grades={}

    def __init__(self, name):
        self.__name =name

    def add_module(self,title):
        modules.append(title)
        grades[title]=title.get_grade()

    def get_list_modules(self):
        for el in modules:
            print(el)


    def get_grades(self):
        for el in grades:
            print(el + ': '+grades[el])


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
