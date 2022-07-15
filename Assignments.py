# forloop using range
# for x in range(1,6):
#     print(x,end=" ")
# forloop using list
# cricketers =['M.S.Dhoni','Virat Kohli','Hardik Pandya']
# for x in cricketers:
#     print(x)
# forloop using tuple
# Numbers =(2,4,6,8,10)
# for x in Numbers:
#     print(x,end=" ")
# forloop using dictnory
# Family_info ={"Father":"Ram","Mother":"Sita","Sister":"Kartiki"}
# for x in Family_info:
#     print(x)
# for x in Family_info.items():
#     print(x)
# for x in Family_info.values():
#     print(x)
# for x in Family_info.keys():
#     print(x)
# forloop using string
# string="Good Morning"
# for x in string:
#     print(x,end=" ")
# Simple While loop
# i=1
# while i<10:
#     print(i,end=" ")
#     i=i+1;
# printing Multiplication table using nested while loop
# i=1
# while i<=10:
#     j=1
#     while j<=10:
#         print(i*j,end=" ")
#         j=j+1
#     i=i+1
#     print()
# printing prime Numbers using Nested while loop
# i=2
# while i<20:
#     j=2
#     while j<=(i/j):
#         if not (i%j):
#             break
#         j=j+1
#     if j>(i/j):
#         print(i," is prime Number")
#     i=i+1
# find Number is Prime or not
# number =int(input("Enter a Number:"))
# if number>1:
#     for i in range(2,int(number/2)+1):
#         if(number%i)==0:
#             print(number," is not prime Number")
#             break
#     else:
#        print(number," is prime number")
# else:
#     print(number," is less than 1")

# Fibonacci Series
# def fib(n):
#     a=0
#     b=1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
# fib(20)

# Linear search
# def lin_Search(arr,ele,length):
#     for i in range(0,length):
#         if arr[i]==ele:
#             return i+1
#     return -1
# length = int(input("Enter length of an array"))
# arr=[]
# print("Enter elements in an array")
# for i in range(length):
#     arr.append(int(input()))
# ele =int(input("Enter element to search"))
# res =lin_Search(arr,ele,length)
# if res==-1:
#     print("Element not found")
# else:
#     print("Element is present at index ",res)

# Binary Search(Simple)
# def Binary_Search(arr,low,high,ele):
#     mid=0
#     while low<=high:
#         mid=(low+high)//2
#         if arr[mid]<ele:
#             low=mid+1
#         elif arr[mid]>ele:
#             high=mid-1
#         else:
#             return mid+1
#     return -1
# arr=[2,3,4,10,40]
# ele=10
# low=0
# high=len(arr)-1
# res=Binary_Search(arr,low,high,ele)
# if res!=-1:
#     print("Element is present at Position ",str(res))
# else:
#     print("Element is not present in array")

# Binary Search (Recursive)
# def Binary_Search(arr,low,high,ele):
#     if high>=low:
#         mid=(high+low)//2
#         if arr[mid]==ele:
#             return mid+1
#         elif arr[mid]>ele:
#             return Binary_Search(arr,low,mid-1,ele)
#         else:
#             return Binary_Search(arr,mid+1,high,ele)
#     else:
#         return -1
# arr =[2,3,4,10,40]
# x=3
# res=Binary_Search(arr,0,len(arr)-1,x)
# if res!=-1:
#     print("Element is present at position ",str(res))
# else:
#     print("Element is not present in an array")

# Insertion Sort
# def Insertion_Sort(arr):
#     for i in range(1,len(arr)):
#         n=arr[i]
#         j=i-1
#         while j>=0 and n<arr[j]:
#             arr[j+1]=arr[j]
#             j=j-1
#         arr[j+1]=n
# arr =[33,12,8,42,10,5]
# Insertion_Sort(arr)
# print("Sorted array is:")
# for i in range(len(arr)):
#     print("%d"%arr[i],end=" ")

# Bubble Sort
# def Bubble_Sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 temp=arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=temp
# arr=[12,2,67,23,25,50]
# Bubble_Sort(arr)
# print("Sorted array is:")
# for i in range(len(arr)):
#     print("%d"%arr[i],end=" ")

#Palindrome Number
# num=int(input("Enter a value:"))
# temp=num
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# if temp==rev:
#     print(temp," is a Palindrome Number")
# else:
#     print(temp," is not a Palindrome Number")

# Exception Handing

# try:
#     file=open("abc.txt","r")
#     file.write("This is my test file for Exception Handling!!")
# except IOError:
#     print("Error: file not found")
# else:
#     print("Contents written in file successfully")
#     file.close()

# try:
#     file=open("abc.txt","w")
#     file.write("This is my test file for Exception Handling!!")
# except IOError:
#     print("Error: file not found")
# else:
#     print("Contents written in file successfully")
#     file.close()

# # 4 built-in functions of Dictionary
# student_data={
#     "Name":"Rajkumar",
#     "Roll No":78,
#     "City":"jalgaon"
# }
# print(student_data)
# #1: Values()
# x=student_data.values()
# print(x)
# # 2:Update()
# student_data.update({"Age":21})
# print(student_data)
# # 3:Keys()
# x=student_data.keys()
# print(x)
# # 4:get()
# x=student_data.get("Roll No")
# print(x)
# # 5: clear()
# student_data.clear()
# print(student_data)

# 4 Built-in functions of list
# color =["Red","Yellow","Blue","Pink"]
# print(color)
# # 1: append()
# color.append("White")
# print(color)
# # 2: len()
# print(len(color))
# # 3:remove()
# color.remove("Yellow")
# print(color)
# # 4: Slice()
# x=slice(2)
# print(color[x])
# # 5 : copy()
# x=color.copy()
# print(x)
# # 6: sort()
# x =color.sort()
# print(color)
# # 7: Insert()
# color.insert(5,"Grey")
# print(color)
# # 8: join list
# std_name=['Ram','Shyam','Ganesh']
# List_3=color+std_name
# print(List_3)

# # 4 Built-in functions of TUple
# flowers =("Rose","Lotus","Sunflower","Iris","Rose")
# # 1:len()
# print(len(flowers))
# # 2:count()
# x=flowers.count("Rose")
# print(x)
# # 3:index()
# x = flowers.index("Lotus")
# print(x)
# # Join two tuples
# fruits =("orange","apple","Mango","CusturedApple")
# tuple3=flowers+fruits
# print(tuple3)

# # Anonymous function Lambda
# square =lambda x:x*x
# print("Square of 4 is ",square(4))
# cube =lambda x:x*x*x
# print("Cube fo 5 is ",cube(5))
# addition =lambda a,b:a+b
# print("Addition is ",addition(5,6))
# substraction =lambda a,b:a-b
# print("Substraction is ",substraction(6,2))