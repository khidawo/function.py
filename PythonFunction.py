
#Function is a block of code that works when callled upon
def my_function():
    print("Waya")

my_function()



#adding arguments to a function
def sum(x,y):
    a=x+y
    print("Answer is=",a)
sum(10,20)   
sum(50,70)
    
def multiplication(a,b):
     m=a*b
     print("Answer is=",m)
multiplication(7,5) 
multiplication(47,72)

def sum(a,b):
    x=a+b
    return x
print(sum(10,5))  

#arbitrary aerguments
def courses(*units):
    for subjects in units:
        print(subjects)
courses("data","cnn","oop2")  


def course(*units):
    for unit in units:
       print(unit)
course("oop2","web","python") 

#Arbitrary keyword arguments
def courses(**units):
    for key,value in units.items():
        print("{}:{}".format(key,value))
courses(first='data',second='python',third='ccn')



#default parameter value
def africa(country="kenya"):
    print("I'm from "+ country)
africa() 
africa("senegal")

#passing a list as an argument
def my_function(food):
    for x in food:
        print(x)
#fruits=["apple","banana","cherry"]
#my_function(fruits)
student={
    "name":"Caleb",
    "email":"caleb@gmail.com",
    "regNo":"BSCIT-05-0000/2010"
}
print(student)
#area of a rectangle
def area_of_rectangle(L,W):
    a=L*W
    return a
print(area_of_rectangle(3,7))

#area of a circle
def area_of_circle(r):
    pi=3.142
    a= pi*(r*r);
    print("Area of a circle is",a)
area_of_circle(7) 

#area of a sphere
def volume_of_spere(r):
    pi=3.142
    v=4/3*pi*(r*r*r);
    print("volume is",v)
volume_of_sphere(4)    




