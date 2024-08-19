import random
import string


def gen():
    n = int(input("Enter the length of your desired password: "))
    print("Select the complexity of the password\n1. Easy\n2. Medium\n3. Hard\n(Answer with 1, 2, or 3)")
    complexity = int(input("Enter here: "))

    if complexity == 1:
        char = string.ascii_lowercase + string.digits
    elif complexity == 2:
        char = string.ascii_uppercase + string.ascii_lowercase + string.digits
    elif complexity == 3:
        char = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    else:
        print("Invalid choice.")
        return  # Exit the function if an invalid complexity is selected

    # Generate the password
    p_word = ''.join(random.choices(char, k=n))

    # Ensure randomness by shuffling the characters
    p_word_list = list(p_word)
    random.shuffle(p_word_list)
    last = ''.join(p_word_list)

    print("Your password is ready!!")
    print(f"Password: {last}")


gen()

while True:
    feed = input("Are you satisfied?\nYes/No: ").lower().strip()
    if feed == "yes":
        break
    else:
        gen()

print("Thank you for visiting us :)")
