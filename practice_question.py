# import time
# print("what shall i remind you")
# text=str(input())
# print("in how many minutes")
# localtime=float(input())
# localtime=localtime*60
# time.sleep(localtime)
# print(text)
# import qrcode 
# from PIL import Image
# url="https://www.youtube.com"
# qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT=_H,box_size=10,border=4,
# qr.add_data(url)
# import pywhatkit as kit
# phone_number="+917906925782"
# message="hello from python!"
# kit.sendwhatmsg_instantly(phone_number,message)
# euclidean distance=(x2-x1)2+(y2-y1)2
# x1=float(input("enter the value of x1"))
# x2=float(input("enter the value of x2 "))
# y1=float(input("enter the value of y1"))
# y2=float(input("enter the value of y2"))
# d=(x2-x1)**2 + (y2-y1)**2
# print(d)
# a1=int(input("write the first angle: "))
# a2=int(input("write the second angle: "))
# a3=int(input("write the third angle: "))
# if a1+a2+a3 == 180 and a1!=0 and a2!=0 and a3!=0:
#     print("it can formed a triangle")
# else:
#     print("not formed")
# cp=int(input("enter the cost price: "))
# sp=int(input("enter the selling price: "))
# price=sp-cp
# if cp>sp:
#     print("loss:",price)
# else:
#     print("its profit",price)
# p=int(input("principle"))
# r=int(input("rate"))
# t=int(input("time period"))
# si=(p*r*t)/100
# print("simple interst is",si)
# def si(p,r,t):
#     return (p*r*t)/100
# SI=si(1000,2,3)
# print(SI)
#v=3.14*r2*h
# r=float(input("radius "))
# h=float(input("height "))
# v=3.14*r**2*h
# print("volume of cylinder",v)
# cost=(v/1000*40)
# print("cost is ",cost)
# num=int(input("enter number to check"))
# if num%3==0 and num%6==0:
#     print("num is sdivisible by 3 and 6")
# else:
#     print("not divisible")
# temp=int(input("enter current temperature "))
# hum=int(input("enter the current humidity "))
# if (temp>=30 and hum>=90):
#     print("weather is hot and humid")
# elif(temp>=30 and hum<90):
#     print("wether is hot ")
# elif(temp<30 and hum>=90):
#     print("weather is cold and humid")
# else:
#     print("weather is cold")
# num=int(input("enter three digit num"))
# a=num%10
# num=num//10
# b=num%10
# num=num//10
# c=num%10
# add=(a**2)+(b**2)+(c**2)
# print(add)
# armstrong number =153
# user_input=int(input("enter num of three digit "))
# num=user_input
# a=num%10
# num=num//10
# b=num%10
# num=num//10
# c=num%10
# num=num
# arm=(a**3+b**3+c**3)
# print(arm)
# if arm ==user_input:
#     print("this is armstrong number",num)
# else: 
#     print("this is not armstrong number",num)
# num=int(input("enter num of three digit "))
# deduction(3%) pf= HRA(10%),DA(5%),and tax(if salary is between 5-10 lakh-10%,,,,bw 11 to 20 lakh =-20% and if 20< -30% tax)
user_input=float(input("enter your annual salary"))
if user_input >500000 and user_input <1000000:
    tax=(10/100)*user_input
    temp_salary=user_input-tax
elif user_input >1000000 and user_input <2000000:
    tax=(20/100)*user_input
    temp_salary=user_input-tax
elif user_input >2000000:
    tax=(30/100)*user_input
    temp_salary=user_input-tax
else:
    tax=(3/100)*user_input
    temp_salary=user_input-tax
# print("after salary reduction(only tax):",temp_salary)
hra=(10/100)*temp_salary
da=(5/100)*temp_salary
pf=(3/100)*temp_salary
hra_da_pf=hra+da+pf
your_salary=(temp_salary-hra_da_pf)//12
print("your monthly in handsalary is ",your_salary)
if  your_salary<=999:
    print(your_salary,'Rs')
elif  your_salary>999 and your_salary <99999:
    print(your_salary/1000,'k')
elif  your_salary>=1000 and your_salary <=9999999:
    print(your_salary/100000,'lac')
else :
    print(your_salary/10000000,'crore')
# while True:
#     user_input=input('''welcome to menu drive program
#         1.cm to feet
#         2.kl to miles
#         3.usd to inr
#         4.exit
#         \n         ''')

#     if user_input == "1":
#         cm=float(input("enter the value in cm to change in feet:"))
#         feet=cm*0.0328
#         print(feet,"feet")
#     elif user_input =="2":
#         kl=float(input("enter the value in kl to change into miles"))
#         miles=kl*1.6
#         print(miles,"miles")
#     elif user_input =="3":
#         usd=float(input("enter the rupees in usd to change into inr"))
#         inr=usd*83.10
#         print(inr,"inr")
#     else :
#         break
# print("you exit")
# a=input("enter")
# print(a)

# for i in range(1,26):
#     if (i//2!=0):
#         print(i)
#     else:
#         print("2")
   



















    