# string operations🎈🎈

name = "khushmeet"
print(name[0])
print(name[-1])
print(len(name))          #length
print(name.upper())
print(name.lower())
print(name[::-1])         #reverse


#string slicing😊😊
string = "Data science"

print(string[ : 4])         #first 4 : data
print(string[3 : 6])       
print(string[ : : -1])       #reverse


#list operations👍👍
numbers = [5,8,3,20,16]

numbers.append(6)   #add elements

numbers.insert(2,50)     #insert elment
print(numbers)

numbers.remove(20)        #remove element
print(numbers)

numbers.pop()             #delete last element
print(numbers)

numbers.reverse()         #reverse list
print(numbers)

numbers.sort()            #sort list
print(numbers)

print(len(numbers))         #length

print(numbers.count(5))     #count occurence of 5


#tuple operations😁😁
subjects = ("math","science","english","hindi","computer")
print(subjects[0])
print(subjects[-1])
print(len(subjects))
print(subjects[1:4])

numbers = (10,20,30,40,50)
print(max(numbers))
print(min(numbers))
print(sum(numbers))


#tuple packing and unpacking👌👌
student = ("khushmeet",20,"B.Tech","jaipur")

name, age, course , city = student

print(name)
print(age)
print(course)
print(city)


#dictionary operations😉😉
student = {
    "name" : "khushmeet",
    "age" : 20,
    "course" : "course data science",
    "Address" : "jaipur"
}

print(student.keys())       #all keys 
print(student.values())     #all values
print(student.items())      #all items

student["Address"] = "Delhi"    #update address
print(student)

student["Branch"] = "cse"        #add new key
print(student)



#nested list access🤗🤗🤗
lst = [1,2,3,4,[2,5],7]
print(lst[4][0])

#-+=operator
number = int(input("enter a number :"))
number += 10
print("updated value :",number)


#type casting🚀🚀🚀
a = input("enter a first number : ")
b = input("enter a second number : ")

a = int(a)
b = int(b)

print("multiplacation :",a*b)


#dictionary methods💕💕
student = {
    "Name" : "khushmeet",
    "age" : 20,
    "Course" : "data science"

}

print(student.get("Name"))
print(student.keys())
print(student.values())
print(student.items())


#get() is safe - no error if key missing
print(student.get("phone","not found"))



