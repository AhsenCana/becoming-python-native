# dictionary
words = {
    "사과" : "apple",
    "딸기" : "strawberry",
    "바나나" : "banana",
    "포도" : "grape",
    "수박" : "watermelon",
}

score = 0

print("This is a mini Korean test ^^ ")
print("\n Write the English meaning of each word.\n ")

for korean, english in words.items():
    answer = input (f"What does '{korean}' mean? ").strip().lower()

    # f => this string has variables inside

    if answer == english:
        print("Correct!\n")
        score +=1
    else:
        print(f"Wrong! The answer is '{english}' \n")

print(f"Your score is: {score}/5 \n")

if score == 5:
    print("Perfect!\n")
elif score > 3:
    print("Not bad!\n")
else:
    print("Study fruit names again..\n")