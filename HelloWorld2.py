__author__ = "CasualTommyst"
# greeting = "Szia"
# name = input("Please enter your name here: ")
# print(greeting + " " + name + "!")
#
# splitString = "This string has been\nsplit over\nseveral\nlines"
# print(splitString)
#
# tabbedString = "1\t2\t3\t4\t5\t"
# print(tabbedString)

print("The pet shop owner said \"No, no, He\'s uh,... he\'s resting\"")
print('The pet shop owner said \"No, no, He\'s uh,... he\'s resting\"')

anotherSplitString = """This string has been
split over
several lines"""

print(anotherSplitString)

print("""The pet shop owner said "No, no, 'e's' uh,... he's resting" """)
#in this case a space is needed as Py doesn't handle """" so well
print('''The pet shop owner said "No, no, 'e's' uh,... he's resting"''')

#Printing tabs exercise
print("Number 1\tThe Larch\nNumber 2\tThe Horse Chestnut")


name = input("Please tell me your name: ")

if name == "Tamás":
    print("Helló gazdi")
elif (name == "Zoé") or (name == 'Ginger'):
    print("Tűnés lefelé a billentyűzetről!")
elif name == "Vivi":
    print("Szia szerelmem :3")
else:
    print("Hát te meg ki vagy?")
