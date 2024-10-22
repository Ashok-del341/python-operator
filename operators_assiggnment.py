p=10000
t=12
r=2
i=p*t*r/100
print("total interst:",i)
#
l=int(input("enter the length of the rectriangle:"))
w=int(input("enter the wedth of the rectriangle:"))
area=l*w
print("area of the rectriangle of length",l,"and wiedth",w,"is:",area)
perimeter=2*(l+w)
print("perimeter of the rectriangle of length",l,"and wiedth",w,"is:",perimeter)
#
celsius = float(input("enter the temperature in celsius:"))
fahrenheit = celsius * (9 / 5) + 32
print("after conversion of celsius to fahrenheit", fahrenheit)
#
def speed():
    u=float(input("enter the initial velocity:"))
    t=float(input("enter time in seconds:"))
    a=float(input("enter the acceleration:"))
    speed=u*t+(1/2)*a*t**2
    print("speed:",speed)
#
def BMI():
    weight=float(input("enter the weight in kgs:"))
    height=float(input("enter the height in feet:"))
    BMI=weight/height*2
    print("Body Mass Index is",BMI)