#n = lambda x,y:x + y
#print(n(1,2))
#print(n(2,3))

#mas = [i for i in range(10) if i%2==0 and i!=4]

#print(mas[:2])


with open("example.py", "r") as file:
    text = file.read()
    print(text)

file=open("example.py", "r")
text = file.read()
file.close()

print(text)

