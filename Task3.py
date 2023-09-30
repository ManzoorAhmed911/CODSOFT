import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
    
def main():
    try: 
        length = int(input("How much Long password You want: "))
        if length <=0:
            print("Password cannot be zero or less than zero")
            return
        password = generate_password(length)
        print("Generated Password: ", password)
    except ValueError:
        print("please enter the valid integer number in order to proceed!")

main()