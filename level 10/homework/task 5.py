# for loop

# first 

for i in range(1, 1001):
    print("I love GOA")
    print(str(i) + "%")

#second

for i in range(100, 1001, 10):
    print (i)

#third

for i in range(1000, 1, -1):
    print (i)

#fourth

for i in range (1, 1002, 1000):
    print (i)

#fifth

for i in range (1, 100, 1000):
    print((i))




#while loop

#first

i = 1
while i > 5:
    print (i)
    i +=1

#second

i = 5
while i > 0:
    print (i)
    i -=1

#third

total = 0
i = 1
while total <= 10:
    total += i
    i +=1

#fourth

total = 10
i = 1
while total <= 10:
    total += i
    i -=1

#fifth

correct_password = "12345"
password= ""
while password != correct_password:
    password = input ("enter the password: ")
print ("access granted")
