for x in range (50,100):
    print(x)
i=0
while i<20:
    i=i+1
    print(i)
for x in range (50,100,2):
    print(x)
for x in range (1500,2700):
   if x%7==0 and x%5==0:
       print(x)

a = [2,4,7,101,200]
for i in a:
    print(i)
z = len(a)
for i in range (z):
    print(a[i])

#Break and Continue in Loop
for x in range (10):
    if x>5:
        break
    print(x)
i=0
while i<10:
    print(i)
    if(i>5):
        break
    i+=1
for i in range(6):
    if i==2:
        continue
    print(i)


#name in Loop 
for i in range (5):
    for i in range (6):
        print("nitin  singh")
for i in range (5,6):
    for j in range (1,11):
        print(i,'*',j,'=',i*j)
for i in range (2,20):
    for j in range (1,11):
        print(i,'*',j,'=',i*j)

#Table in Loop
i=5
while i==5:
    j=1
    while j<11:
        print(i,'*',j,'=',i*j)
        j+=1
    i+=1
i=2
while i<11:
    j=1
    while j<11:
        print(i,'*',j,'=',i*j)
        j+=1
    i+=1

#Odd number Loop
for i in range(1,21,2):
    print(i)

#Name range in Loop
for i in range(0,21,2):
    print("Nitin Singh")

#Nested Loop
a=[20,30,40,[100,200,300]]
print(a[3])
print(a[3][1])
print()