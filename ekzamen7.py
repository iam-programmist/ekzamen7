# # EXAM FOR WEEK 6

# ## KEEP IN MIND: YOU ARE DOING THIS FOR YOUR BRIGHT FUTURE, SO GIVE YOUR 120%!
# ## ПОМНИТЕ: ВЫ ДЕЛАЕТЕ ЭТО ДЛЯ СВОЕГО СВЕТЛОГО БУДУЩЕГО, ПОЭТОМУ ВЫКЛАДЫВАЙТЕСЬ НА ВСЕ СВОИ 120%!

# ## RULES:
# > No interner, no help to each other!

# > Make one file and place all your work there (e.g. odina_kholiqov.py)

# > Send the file at 

# > You have 2 hours only

# ### 1 Question
# What is OOP and why is it important? Write about main principles of OOP.
# Чиро ООП мегуянд ва барои чӣ он лозим аст? Дар бораи принсипҳои асосии он нависед.

# OOP in yake az paradigmahoi barnomasozi meboshad va az class, object,atributho va metodho iborat ast.
# oop kori moro osontar mekunad, yane mo kodro kamtar va fahmotar menavisem
# oop az 4 princip iborat ast: incapsulyaciya,polimorfizm,nasledovanie,abstracsiya

# ### 2 Question
# What are getter and setter and how to use them? Write about properties in python.
# Getter ва setter чист ва чӣ тавр онҳоро истифода мебарем? Дар бораи хусусиятҳо(properties) дар python нависед.

# getter in metode meboshad ki tavasuti on mo ba objectho dastrasi paido mekunem, misol mo yak metod mesozem va yagonchizro return mekunem
# setter in metode meboshad ki tavasuti on mo objectro ivaz mekunem

# ### 3 Question
# Types of variables and methods in a class.
# Кадом намуди атрибутҳо ва методҳо дар клас мавҷуданд. 

# 2 namud atributho va 3 namud metodho:
# instance variable,class variable
# instance metod,class metod,static metod

# ### 4 Question
# Write about constructor and destructor.
# Дар бораи конструктор ва деструктор нависед.

# konstructor in metode meboshad baroi sokhtani object va inizializaziyai on - __init__
# destructor in metod baroi nest kardani object - __del__

# ### 5 Question
# Difference between global, local and nonlocal variables.
# Фарқият байни тағйирёбандаҳои global, local and nonlocal.

# global in tagiryobandahoi globalni yane inhoro mo metavonem dar kujoe khohem istifoda mebarem tavasuti global
# localro mo dar daruni yagonchis misol dar funcsiyai darungi istifoda burda metavonem tavasuti local
# tavasuti nonlocal mo metavonem localniro nonlocal kunem yane localniro dar yagon funciyai digar istifoda barem

# ### 1 
# Create a program that asks the user for a range of numbers (x, y) and displays the multiplication tables from x to y.
# Барномае созед ки аз консол 2 рақамро қабул мекунад. Барои ҳар як адади дар ин давр вуҷуддошта ҷадвали зарбашро нишон диҳад.
# ### EXAMPLE
# # INPUT
#     From = 2
#     To = 3
# # OUTPUT
#     2x1= 2
#     2x2= 4
#     2x3= 6
#     2x4= 8
#     2x5= 10
#     2x6= 12
#     2x7= 14
#     2x8= 16
#     2x9= 18
#     2x10= 20
    
#     3x1= 3
#     3x2= 6
#     3x3= 9
#     3x4= 12
#     3x5= 15
#     3x6= 18
#     3x7= 21
#     3x8= 24
#     3x9= 27
#     3x10= 30

# def test(a,b):
#     for i in range(1,11):
#         res=a*i
#         print(f"{a}x{i}={res}")
#     print()
#     for j in range(1,11):
#         res=b*j
#         print(f"{b}x{j}={res}")
# a=int(input())
# b=int(input())
# test(a,b)

# ### 2
# Create a class of Circle with instance variable like radius and class variable like PI(3.14). Then create a constructor which initializes the radius(radius comes as a parameter of constructor).
# Your class should have the following methods:
# Як класи Circle ки аз як тағйирёбандаи ба клас таалуқдошта PI = 3.14 ва як тағйирёбандаи ба обект тааллуқдошта radius ки қиммати он аз конструктор гузошта мешавад созед. Класи Шумо аз методҳои зерин бояд иборат бошад:

# 1. get_area();               // area = 2 * PI * R * R
# 2. get_diametr();           // diameter = 2 * R
# 3. get_circumference();      //  circumference  = 2 * PI * R
# 4. get_radius();             // radius  = R

# class Circle:
#     PI=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def get_area(self):
#         print(2*self.PI*self.radius*self.radius)
#     def get_diametr(self):
#         print(2*self.radius)
#     def get_circumference(self):
#         print(2*self.PI*self.radius)
#     def get_radius(self):
#         print(self.radius)
# obj1=Circle(int(input()))
# obj1.get_area()
# obj1.get_diametr()
# obj1.get_circumference()
# obj1.get_radius()

# ### 3
# Create a Calculator class with this static methods:
# Класи Калкуляторро бо методҳои статикии зерин созед:
# 1. factorial(n)
# 2. power(a, b)
# 3. sqrt(n)

# class Calculator:
#     @staticmethod
#     def factorial(n):
#         for i in range(1,n+1):
#             res=i*(i+1)
#             print(res)
#     def power(a,b):
#         print(a**b)
#     def sqrt(n):
#         print(n**0.5)
# obj1=Calculator()
# obj1.factorial(int(input()))
# obj1.power(int(input()),int(input()))
# obj1.sqrt(int(input()))

# ### 4
# Write a program in Python that asks the user for two numbers and one operation (+, -, *, /) then calculate the operation and display the result on the screen.
# You should to follow this steps:
# Як класи Calculator созед ки дар конструктор атрибутҳои зеринро дорост. Рақами якум, амал(+, -, *, /) ва рақами дуюм. Калкулятори Шумо баяд 4 амали математикиро иҷро кунад. Берун аз клас як даври беохир(infinite loop) созед. Объекти класи Калкуляторро созед ва рақамҳо ва аломати дохил кардаатонро ба он гузоред. match case - ро барои  даъват кардани методиҳои клас вобаста ба аломати дохилкарда истифода баред.

# 1.	Create class Calculator 
# 2.	Create a constructor which initializes the first number, operation(+, -, *, /) and second number(first num, second num, operation comes as parameter of constructor).
# 3.	Create four instance methods like: 
#     Sum()
#     Subtract()
#     Multiplication()
#     Division()
# 4.	Create infinite loop outside Calculator class 
# 5.	Use the math case block for calling methods
# ### EXAMPLE
# # input 
#     The first number is: 3
#     The operation is: +
#     The second number is: 1
# # output
#     3 + 1 = 4

# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def Sum(self):
#         print(self.a+self.b)
#     def Subtract(self):
#         print(self.a-self.b)
#     def Multiplication(self):
#         print(self.a*self.b)
#     def Division(self):
#         print(self.a//self.b)
# while True:
#     a=int(input())
#     b=input()
#     c=int(input())
#     if b=="+":
#         obj1=Calculator(a,c)
#         obj1.Sum()
#         break
#     if b=="-":
#         obj1=Calculator(a,c)
#         obj1.Subtract()
#         break
#     if b=="*":
#         obj1=Calculator(a,c)
#         obj1.Multiplication()
#         break
#     if b=="/":
#         obj1=Calculator(a,c)
#         obj1.Division()
#         break
        
# ### 5 Question
# Write a program to build a simple Student Management System using classes and containers (lists, dict). The system should perform the following operations:

#     1. Accept: Method to enter new student details
#     2. Display: Function to display student details
#     3. Search: search function for searching student by username
#     4. Delete: for deleting student by id
#     5. Update: update student by id

# Баронома Student Management System барои контроли донишҷуён созед бо истифодаи Класс ва Контейнерҳо(lists, dict). Баронома бояд вазифаҳои зеринро иҷро кунад.
#     1. Accept: Функсия барои сабт кардани донишҷуи нав ба базаи маълумотҳо
#     2. Display: Нишон додани маълумотҳои донишҷуён дар экран
#     3. Search: Барои кофтани донишҷу бо username
#     4. Delete: Барои нест кардани маълумотҳои донишҷуи додашуда аз база
#     5. Update: Барои иваз кардани маълумотҳои донишҷуи додашуда 


# ### 6 Question
# Write an access control in PYTHON that asks the user for the username and password. Both must be integers from user.
# You should to follow this steps:
# 1. Create a User class with attributes like First name, Last name, Username and Password. All atributes should init from constructor(__init__).
# 2. Create a UserManager class with this methods:
#     register() -> in this method you should create object of User, input user information from console and append to list_of_users.
    
#     login() -> this method should to check if user login and password both correct should print Login successful! or this user is not to list_of_user print User with this username not found and password incorrect print Password incorrect.
    
#     change_password() -> this method for changing password by username, old_password and new_password
	
#     GetUser() -> get all users from list_of_users

# Як барнома созед ки вазифаҳои зеринро иҷро кунад. Регирстратсия, логин, ивази парол, истифодабарандагон.
# Барои ҳалли ин масъала класи User бо атрибутҳои First name, Last name, Username ва Password созед. Ҳамаи атрибутҳо аз конструктор ворид карда шаванд. Класи дигар ки бояд созед ин UserManager ки аз методҳои register(), login(), change_password() ва GetUser() иборат аст.
#     register() -> дар ин метод обекти класи User - ро созед маълумотҳояшро аз консол дохил карда онро ба листи  list_of_users дохил кунед. 

#     login() -> дар ин метод бошад санҷед агар истифодабар бо ҳамин логир ва парол дар list_of_users бошад дар консол  Login successful! - ро нишон диҳед ва агар набошад User with this username not found, ё паролаш нодуруст бошад     Password incorrect!
    
#     change_password() -> дар ин метод истифодабар метавонад бо дохил кардани username, old_password ва new_password паролашро иваз кунад.
	
#     GetUser() -> ин метод бошад бо як формати хуб ҳамаи маълумотҳои истидабаронро дар консол нишон диҳад.

