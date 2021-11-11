#!/usr/bin/env python3

# class triangle(object):
#     def __init__(self, angle1, angle2, angle3):
#         self.angle1 = angle1
#         self.angle2 = angle2
#         self.angle3 = angle3
#         self.number_of_sides = 3

#     def check_angles(self):
#         assert type(self.angle1) == int
#         assert type(self.angle2) == int
#         assert type(self.angle3) == int

#         sumando = self.angle1 + self.angle2 + self.angle3
#         if sumando == 180:
#             return True
#         else:
#             return False

# my_triangle = triangle(90,30,60)
# print(my_triangle.check_angles())

# class songs(object):
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#     def getLyrics(self):
#         return self.lyrics

#     def sing_me_a_song(self):
#         x = iter(self.getLyrics())
#         return x

# happy_bday = songs(["May god bless you, ",
#                    "Have a sunshine on you,",
#                    "Happy Birthday to you !"])

# for x in happy_bday.getLyrics():
#     print(x)

# class lunch(object):
#     def __init__(self, menu):
#         self.menu = menu

#     def menu_price(self):
#         if self.menu == "menu 1":
#             return "Your choice",self.menu,"Price 12.00"
#         if self.menu == "menu 2":
#             return "Your choice",self.menu,"Price 13.40"
#         else:
#             return "Error in menu"

# Paul = lunch("mnu 1")
# print(Paul.menu_price())
# Pedro = lunch("menu 2")
# print(Pedro.menu_price())


# class point_3d(object):

#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __repr__(self):
#         return "(%s)" % (self.x)

# my_point = point_3d("names", 2, 3)
# print(my_point.__repr__())


# # 1. Write a Python program to import built-in array module and display the namespace of the said module.


# class to_import(object):
#     def __init__(self):
#         self.x = "import array"
#     def importing_modules(self):
#         y = self.x.split(' ')
#         return self.x, "(%s)" % (y[1])

# instancia = to_import()
# # print(instancia.importing_modules())
# print(instancia.__dict__)

# for i in instancia.__dict__:
#     print(str(i)+': '+str(instancia.__dict__[i]))

# from builtins import abs
# import builtins

# print(abs(-155))
# for i in abs.__doc__.split(' '):
#     print(i)
# print(abs.__doc__)

# # help(builtins.abs)
# for i in builtins.abs.split("\n"):
#     print(i)


# 2. Define a Python function student(). Using function attributes display the names of all arguments.
# 6. Write a Python function student_data () which will print the id of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.

# class myClass(object):

#     def student(self, arg0, *args):
#         self.arg0 = arg0
#         # self.arg1 = arg1
#         # self.arg2 = arg2
#         return str(arg0) + str(args)

# myInstance = myClass()
# print(myInstance.student(38234, 'hola', 'math'))

# def student_data(student_id, **kwargs):
#     print(f'\nStudent ID: {student_id}')
#     if 'student_name' in kwargs:
#         print(f"Student Name: $ {kwargs['student_name']}")

#     if 'student_name' and 'student_class' in kwargs:
#             print(f"\nStudent Name: $ {kwargs['student_name']}")
#             print(f"Student Class: $ {kwargs['student_class']}")


# student_data(student_id='SV12', student_name='Jean Garner')

# student_data(student_id='SV12', student_name='Jean Garner', student_class ='V')

# 7. Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.

# class student(object):
#     pass

# print(type(student))
# print(student.__dict__.keys())
# print(student.__module__)

# 8. Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.

# class student:

#     def __init__(self, student_name, marks):
#         self.student_name = student_name
#         self.marks = marks

# class marks():
#     pass

# instance1 = student('Natasha', 100)
# print(isinstance(instance1, student))
# instance2 = marks()
# print(isinstance(instance2, marks))

# print(issubclass(student, object))
# print(issubclass(marks, object))

# print(instance1.student_name, instance1.marks)
# instance1.student_name = 'Becky'
# instance1.marks = 200
# instance1.dots = 'testing'
# print(instance1.student_name, instance1.marks)


# class Student:
#     student_name = 'Terrance Morales'
#     marks = 93

# print(f"Student Name: {getattr(Student, 'student_name')}")
# print(f"Marks: {getattr(Student, 'marks')}")

# setattr(Student, 'student_name', 'Angel Brooks')
# setattr(Student, 'marks', 95)

# print(f"Student Name: {getattr(Student, 'student_name')}")
# print(f"Marks: {getattr(Student, 'marks')}")


# 9. Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and their values of the said class. Now remove the student_name attribute and display the entire attribute with values.

# class Student:
#     def __init__(self, student_id, student_name ):
#         self.student_id = student_id
#         self.student_name = student_name

#     # student_id = 93845
#     # student_name = 'Terrance Morales'

# laInstancia = Student(12423, 'Natasha')

# setattr(Student, 'student_class', 'Science')

# print(getattr(Student, 'student_id'))   # Can't access when this attributes are initialized with '__init__' method
# print(getattr(Student, 'student_name'))
# print(getattr(Student, 'student_class'))


# delattr(Student, 'student_name')

# print(getattr(Student, 'student_id'))
# # print(getattr(Student, 'student_name'))
# print(getattr(Student, 'student_class'))

# laInstancia.student_class = 'Math'
# setattr(Student, 'student_class', 'Science')

# print(laInstancia.__dict__)

# print(getattr(Student, 'student_id'))
# print(getattr(Student, 'student_name'))
# print(getattr(Student, 'student_class'))

# delattr(Student, 'student_name')

# print(getattr(Student, 'student_id'))
# # print(getattr(Student, 'student_name'))
# print(getattr(Student, 'student_class'))


# class Student:

#     student_id = 'V10'
#     student_name = 'Jacqueline Barnett'
# print("Original attributes and their values of the Student class:")
# for attr, value in Student.__dict__.items():
#     if not attr.startswith('_'):
#         print(f'{attr} -> {value}')
# print("\nAfter adding the student_class, attributes and their values with the said class:")
# Student.student_class  = 'V'
# for attr, value in Student.__dict__.items():
#     if not attr.startswith('_'):
#         print(f'{attr} -> {value}')
# print("\nAfter removing the student_name, attributes and their values from the said class:")
# del Student.student_name
# #delattr(Student, 'student_name')
# for attr, value in Student.__dict__.items():
#     if not attr.startswith('_'):
#         print(f'{attr} -> {value}')


# class Student:
#     school = 'Forward Thinking'
#     address = '2626/Z Overlook Drive, COLUMBUS'

# student1 = Student()
# student2 = Student()
# student1.student_id = "V12"
# student1.student_name = "Ernesto Mendez"
# student2.student_id = "V12"
# student2.marks_language = 85
# student2.marks_science = 93
# student2.marks_math = 95
# students = [student1, student2]
# for student in students:
#     print('\n')
#     for attr in student.__dict__:
##          print(f'{attr} -> {getattr(student, attr)}')
# class intToRoman(object):
# # https://www.geeksforgeeks.org/python-program-to-convert-integer-to-roman/#:~:text=Divide%20the%20given%20number%20into,the%20roman%20equivalent%20of%203000
#     theNumber = 0

#     def creatingDictionary(self):
#         self.theValues = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
#         self.theKeys = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
#         self.theDictionary = {}
#         self.count = 0

#         for i in self.theKeys:
#             self.theDictionary[i] = self.theValues[self.count]
#             self.count += 1

#         return self.theDictionary

#     # def getting(self):
#     #     return theNumber

#     def comparing(self, other):
# # Si tienes problemas, global other!!
#         self.baseNumber = 0
#         valores = self.theDictionary.keys()
#         storing = ''

#         for i in valores.__reversed__():
#             if i <= other:
#                 self.baseNumber = i
#                 break

#         quotient = other // self.baseNumber
#         remainder = other % self.baseNumber
#         print(self.baseNumber)
#         for j in range(quotient):
#             storing += self.theDictionary[self.baseNumber]

#         # storing = self.theDictionary[self.baseNumber]

#         print(remainder // quotient)
#         while remainder > 0:
#             baseNum = self.comparing(remainder)
#             quotient = remainder // baseNum
#             for k in range(quotient):
#                 storing += self.theDictionary[baseNum]
#             remainder = remainder % baseNum

#         print(storing)
#         return self.baseNumber

# laInstancia = intToRoman()
# print(laInstancia.creatingDictionary())
# print(laInstancia.comparing(3549))
# print(laInstancia.storing())




# theKeys = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
# theValues = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
# theDictionary = {}
# count = 0

# for i in theKeys:
#     theDictionary[i] = theValues[count]
#     count += 1

# print(theDictionary)




# def printRoman(number):
#     num = [1, 4, 5, 9, 10, 40, 50, 90,
#         100, 400, 500, 900, 1000]
#     sym = ["I", "IV", "V", "IX", "X", "XL",
#         "L", "XC", "C", "CD", "D", "CM", "M"]
#     i = 12

#     while number:
#         div = number // num[i]
#         number %= num[i]

#         while div:
#             print(sym[i], end = "")
#             div -= 1
#         i -= 1

#         # return i

# # # Driver code
# # if __name__ == "__main__":
# #     number = 12
# #     print("Roman value is:", end = " ")
# #     printRoman(number)

# printRoman(3549)


# In this method, we have to first observe the problem. The number given in the problem statement can be a maximum of 4 digits. The idea to solve this problem is:

# Divide the given number into digits at different places like one’s, two’s, hundred’s, or thousand’s.
# Starting from the thousand’s place print the corresponding roman value. For example, if the digit at thousand’s place is 3 then print the roman equivalent of 3000.
# Repeat the second step until we reach one’s place.
# Suppose the input number is 3549. So, starting from thousand’s place we will start printing the roman equivalent. In this case, we will print in the order as given below:

# The Roman equivalent of 3000
# The Roman equivalent of 500
# The Roman equivalent of 40
# The Roman equivalent of 9

# Function to calculate Roman values
# def intToRoman(num):

    # # Storing roman values of digits from 0-9
    # # when placed at different places
    # m = ["", "M", "MM", "MMM"]
    # c = ["", "C", "CC", "CCC", "CD", "D",
    #      "DC", "DCC", "DCCC", "CM "]
    # x = ["", "X", "XX", "XXX", "XL", "L",
    #      "LX", "LXX", "LXXX", "XC"]
    # i = ["", "I", "II", "III", "IV", "V",
    #      "VI", "VII", "VIII", "IX"]

    # # Converting to roman
    # print(num // 1000)
    # thousands = m[num // 1000]
    # print((num % 1000) // 100)
    # hundereds = c[(num % 1000) // 100]
    # print((num % 100) // 10)
    # tens = x[(num % 100) // 10]
    # print(num % 10)
    # ones = i[num % 10]

    # ans = (thousands + hundereds +
    #        tens + ones)

    # return ans

# Driver code
# if __name__ == "__main__":
# number = 16
# print(intToRoman(number))



# In this approach, we consider the main significant digit in the number. Ex: in 1234, the main significant digit is 1. Similarly, in 345 it is 3. In order to extract main significant digit out, we need to maintain a divisor (lets call it div) like 1000 for 1234 (since 1234 / 1000 = 1) and 100 for 345 (345 / 100 = 3). Also, let’s maintain a dictionary called roman numeral = {1 : ‘I’, 5: ‘V’, 10: ‘X’, 50: ‘L’, 100: ‘C’, 500: ‘D’, 1000: ‘M’}

# Python 3 program to convert integer number to Roman values
# import math

# def integerToRoman(A):
#     romansDict = \
#         {
#             1: "I",
#             5: "V",
#             10: "X",
#             50: "L",
#             100: "C",
#             500: "D",
#             1000: "M",
#             5000: "G",
#             10000: "H"
#         }

#     div = 1
#     while A >= div:
#         div *= 10

#     div /= 10

#     res = ""

#     while A:

#         # main significant digit extracted
#         # into lastNum
#         lastNum = int(A / div)

#         if lastNum <= 3:
#             print(romansDict[div])
#             res += (romansDict[div] * lastNum)
#         elif lastNum == 4:
#             print(romansDict[div])
#             res += (romansDict[div] +
#                         romansDict[div * 5])
#         elif 5 <= lastNum <= 8:
#             print(romansDict[div])
#             print(romansDict[div*5])
#             res += (romansDict[div * 5] +
#             (romansDict[div] * (lastNum - 5)))
#         elif lastNum == 9:
#             print(romansDict[div])
#             res += (romansDict[div] +
#                         romansDict[div * 10])

#         A = math.floor(A % div)
#         div /= 10

#     return res

# # Driver code
# print("Roman value for the integer is:"
#                 + str(integerToRoman(16)))

# class py_solution:
#     def int_to_Roman(self, num):
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#             ]
#         syb = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#             ]
#         roman_num = ''
#         i = 0
#         while  num > 0:
#             for _ in range(num // val[i]):
#                 print(num // val[i])
#                 print(i)
#                 roman_num += syb[i]
#                 print(num, val[i])
#                 num -= val[i]
#             i += 1
#         return roman_num

# print(8%5)
# print(py_solution().int_to_Roman(8))
# # print(py_solution().int_to_Roman(4000))

# class py1_solution:
#     def roman_to_int(self, s):
#         rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         int_val = 0
#         for i in range(len(s)):
#             if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
#                 int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
#             else:
#                 int_val += rom_val[s[i]]
#         return int_val

# print(py1_solution().roman_to_int('MMMCMLXXXVI'))
# # print(py1_solution().roman_to_int('MMMM'))
# # print(py1_solution().roman_to_int('C'))


# class Validity(object):

    # def valid(self,other):
    #     x = other.find("()")
    #     y = other.find("[]")
    #     z = other.find("{}")
    #     if x != -1 or (y != -1 or z != -1):
    #         return True
    #     else:
    #         return False

# texto = str(())
# texto = "()"
# texto = "()[]{}"
# texto = "[)"
# texto = "({[)]"
# texto = "{{{"
# texto = "{}[{)}"
# print(Validity().valid(texto))


# class Subsets(object):
#     def sets(self, other):
#         theList = [[]]
#         assert type(other) == list

        # for i in range(1, len(other) + 1):
        #     theList.append(other[i-1:i])
        #     double = other[i-1:i+1]
        #     if double in theList:
        #         continue
        #     theList.append(double)

        # firstAndLast = other[0::len(other)-1]
        # theList.append(firstAndLast)
        # theList.append(other[:])

        # return theList

# laLista = [4, 5, 6, 7, 9]
# print(Subsets().sets(laLista))


# class py_solution:
#     def sub_sets(self, sset):
#         return self.subsetsRecur([], sorted(sset))

    # def subsetsRecur(self, current, sset):
    #     if sset:
    #         return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
    #     return [current]

# print(py_solution().sub_sets([4,5]))


# cuadrado = map(lambda x: x**2, enteros)
# class PairElements(object):

#     def pair(self, theList, theTarget):
#         # desdeDonde = 0
#         theListOrdered = sorted(theList)
#         count = 0
#         elementoActual = theListOrdered[count]
#         enumerate(theList)

#         while True:

#             count2 = 0
#             for i in theListOrdered[count:]:
#                 count2 += 1
#                 if elementoActual + i == theTarget:
#                     return f'{elementoActual} index: {count}, {i} index: {count2}'

#             count += 1
#             elementoActual = theListOrdered[count]


# numbers = [10,20,40,50,30,60,70]
# # numbersOrdered = sorted(numbers)
# target = 60
# print(PairElements().pair(numbers, target))






# class py_solution:
#   def twoSum(self, nums, target):
#        lookup = {}
#        for i, num in enumerate(nums):
#            print(lookup)
#            if target - num in lookup:
#                return (lookup[target - num], i )
#            lookup[num] = i
# print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))




# class BuscandoTresNumeros(object):

#     def pair(self, theList, theTarget):
#         theListOrdered = sorted(theList)
#         count = 0
#         elementoActual = theListOrdered[count]
#         while True:
#             count2 = 0
#             for i in theListOrdered[count:]:
#                 count2 += 1
#                 if abs(elementoActual) + abs(i) == abs(theTarget):
#                     return [elementoActual, i]
#             count += 1
#             if count == len(theListOrdered):
#                 break
#             elementoActual = theListOrdered[count]

#     def N_or_P_Numbers(self, other2):
#         other_Ordered = sorted(other2)
#         listOfNegatives = []
#         listOfPositives = []
#         for j in other_Ordered:
#             if j < 0:
#                 listOfNegatives.append(j)
#             else:
#                 listOfPositives.append(j)

#         return [listOfNegatives, listOfPositives]

#     def Sumando(self, other):
#         otherOrdered = sorted(other)
#         numeroActualPositivo = 0
#         numeroActualNegativo = 0
#         listaGeneral = []
#         for i in otherOrdered:
#             if i > 0:
#                 numeroActualPositivo = i
#                 sumandoNegativos = self.pair(self.N_or_P_Numbers(otherOrdered)[0], numeroActualPositivo)
#                 if sumandoNegativos != None:
#                     listaGeneral.append(sumandoNegativos + [numeroActualPositivo])
#             else:
#                 numeroActualNegativo = i
#                 sumandoPositivos = self.pair(self.N_or_P_Numbers(otherOrdered)[1], numeroActualNegativo)
#                 if sumandoPositivos != None:
#                     listaGeneral.append(sumandoPositivos + [numeroActualNegativo])
#         return listaGeneral


# listNumeros = [-25, -5, -10, -3, 0, 5, 8, 23]
# print(BuscandoTresNumeros().Sumando(listNumeros))


# class py_solution:
#  def threeSum(self, nums):
#         nums, result, i = sorted(nums), [], 0
#         while i < len(nums) - 2:
#             j, k = i + 1, len(nums) - 1
#             while j < k:
#                 if nums[i] + nums[j] + nums[k] < 0:
#                     j += 1
#                 elif nums[i] + nums[j] + nums[k] > 0:
#                     k -= 1
#                 else:
#                     result.append([nums[i], nums[j], nums[k]])
#                     j, k = j + 1, k - 1
#                     while j < k and nums[j] == nums[j - 1]:
#                         j += 1
#                     while j < k and nums[k] == nums[k + 1]:
#                         k -= 1
#             i += 1
#             while i < len(nums) - 2 and nums[i] == nums[i - 1]:
#                 i += 1
#         return result

# print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))


# class Potenciacion(object):
#     def funcion_potenciacion(self, base, power):
#         count = 0
#         operacion = 1
#         while count < power:
#             operacion *= base
#             count += 1
#         return operacion

# print(Potenciacion().funcion_potenciacion(2, 5))


# class Reversing(object):
#     def reversing_string(self, other):
#         assert type(other) == str
#         theList = other.split()
#         theList.reverse()
#         return ' '.join(theList)


theString = "hello .py este el es string"
# print(Reversing().reversing_string(theString))

# class py_solution:
#     def reverse_words(self, s):
#         return ' '.join(reversed(s.split()))


# print(py_solution().reverse_words('hello .py'))

# class MyClass():

#     def __init__(self):
#         self.string = ''

#     def get_str(self):
#         self.string = input()

#     def print_str(self):
#         # theString = ''
#         x = [i.capitalize() for i in self.string]
#         print(' '.join(x))

# myInstance = MyClass()
# myInstance.get_str()
# myInstance.print_str()


# class Calculus():
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def rectangle_area(self):
#         return ( self.length * self.width )


# print(Calculus(12, 10).rectangle_area())

# import math

# class Calculus():
#     def __init__(self, radius):
#         self.radius = radius

#     def circle_area(self):
#         return math.pi * self.radius ** 2

#     def circle_perimeter(self):
#         return 2 * math.pi * self.radius

# print(Calculus(8).circle_area())
# print(Calculus(8).circle_perimeter())


class Calculus():
    def __init__(self, radius):
        self.radius = radius

    # def circle_area(self):
    #     return math.pi * self.radius ** 2

x = Calculus(8)
print(type(x).__name__)

# import itertools
# x = itertools.cycle('ABCD')
# print(type(x).__name__)
