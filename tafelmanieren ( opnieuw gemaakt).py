tafels = int(input("welke tafel wilt u weten? "))
for x in range(1,11):
  print(f'{x} x {tafels} = {x*tafels}')

input("Press Enter to continue...") 

i = 30
while i >= 0:
  print(i)
  i -= 1
print("lancering\n")

input("Press Enter to continue...") 

print ("AM hours\n")
a = 0
while a <12:
  a+=1
  print (str(a) + "AM\n")

print ("PM hours\n")
b = 0
while a <12:
  b+=1
  print (str(b) + "PM\n")

input("Press Enter to continue...") 

j = 20
while j <= 50:
  print (j)
  j += 2