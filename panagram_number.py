panagram = input("What number do you want to use: ")
numbers = {
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
}
for character in panagram:
   if character in numbers :
      numbers[character] += 1 

panagram = True
for value in numbers.values():
   if value == 0:
      panagram = False

if panagram == True:
   print("This number is a panagram")
else:
   print("This number is not a panagram")
