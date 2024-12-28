str="student "
str1='''should '''
str2='study'
str3=str+str1+str2
print(str3)
print(len(str3))
print(str3[7], str3[11])
print(str3[3:15])
print(str3[-10:-2])
str4="i am Nandani Singh want to be a programmer."
print(str4.endswith("mer."))
print(str4.capitalize())
print(str4)
print(str4.replace("programmer","coder"))
print(str4.find("t"))
print(str4.count("i"))
light=input("Enter r for red ,g for green, y for yellow: ")
if(light=="y"):
    print("ready")
elif(light=="g"):
    print("go")
elif(light=="r"):
    print("wait") 
else:
    print("NULL")           

