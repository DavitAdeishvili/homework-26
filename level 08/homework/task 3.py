num1= 5
num2= 2
num3=7
num4=10
num5=9
bool1 = True
bool2 = False

print (num2 != num1) #True because 2 does not equal to 5
print (num1 != num1) #False because 5 does equals to 5

print (num2 >= num1) #False because    1) 2 does not equal to 5    2) 2 is not greater then 5
print (num1 >= num2) #True because 5 is greater then 2
print (num1 >= num1) #True because 5 equals to 5

print (num2 <= num1) #True because 5 is greater then 2
print (num1 <= num2) #False because     1) 5 does not equal to 2     2) 2 isn't greater then 5
print (num1 <= num1) #True because 5 equals to 5

print (bool1 and bool2) #false because it conatains false
print (bool1 and bool1) #true beacause there arent any falses
print (bool2 and bool2) #false because it contains false

print (bool1 or bool2) #true because it contains true
print (bool1 or bool1) #true because it containd true
print (bool2 or bool2) #false because it does not contain any trues

print (num1<num2) #false because 5 is greater then 2
print (num1>num2) #true because 5 is greater then 2
print (num3>num1) #true because 7 is greater then 5
print (num3<num1) #false because 7 is greater then 5
print (num4==num4) #true because 10 equals 10
print (num5==num4) #false because 9 does not equals to 10