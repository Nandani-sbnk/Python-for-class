punct='''!@#$%^&*()_+=-/[]{}'"~`<>,.?:;'''
str=input("enter your string:")
no_punctuations=""
for char in str:
    if char not in punct:
        no_punctuations=no_punctuations+char

print(no_punctuations)        