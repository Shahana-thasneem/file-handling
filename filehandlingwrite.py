x=open("hello.txt","w")
x.write("india is my country")
x.close()
x=open("hello.txt","rt")
print(x.read())
x.close()
