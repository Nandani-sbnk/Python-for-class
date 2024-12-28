marks=[34.6,78.2,89.0,23.4,63.1]
student=["Neeshu",19,"CSE-AI",8.2,"Varanasi"]
print(marks)
print(student)
print(student[1])
student[0]="Nandani"
print(len(student))
print(student)
print(marks[:3])
marks.append(54.9)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(4,49.3)
print(marks)
marks.pop(2)
print(marks)
tup=(6,7,3,5,2,9,3,5,1,5)
print(tup)
print(tup[1])
 # tup[3]=2 not possible
tup1=(90)
print(tup1)
print(tup[2:6])
tup.index(3)
tup.count(5)

list=[1,"abc","abc",1]
list1=list.copy()
list.reverse()
if(list==list1):
    print("palidrome")
else:
    print("not palidrome")    