import random
import string

def generate_password(name, length=16):
    random_chars = string.ascii_letters + string.digits + string.punctuation
    name_part = ''.join(random.sample(name, min(len(name), 4)))  # Take up to 4 random letters from name
    random_part = ''.join(random.choices(random_chars, k=length - len(name_part)))
    password = list(name_part + random_part)
    random.shuffle(password)
    return ''.join(password)

counter = 1

while True:
    name = input("Enter your name: ")
    while True:
        social_app = input("Which social app are you going to use this password for? : ")
        password = generate_password(name, length=32)  # Increased length for stronger passwords

        with open("password.txt", "a") as file:  # Append mode to save multiple entries
            file.write(f"{counter}. {social_app}\n")
            file.write(f"   {password}\n\n")
        
        print(f"Generated Password: {password}\nSaved to password.txt")
        
        counter += 1
        
        another = input("Generate another password for a different social app? (y/n): ").strip().lower()
        if another != 'y':
            break
    
    again = input("Generate another password with a new name? (y/n): ").strip().lower()
    if again != 'y':
        break
