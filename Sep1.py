print("Hello! Welcome to daily tracker!")

mood = input ("How do you feel?")
energy = int(input("How would you rate today 1-10"))
event = input("Best thing that happened today?")

print("\n -- Summary of today -- ")
print("your mood: ", mood)
print("your energy level: ", energy)
print("best event: ", event)

if energy <=5 :
    print ("You may take a rest now, 수고했어요!")
else:
    print ("Yay! Let's do one more thing before bed!")
