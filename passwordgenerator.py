import random
def generate_password(length=12):
    characters ="qwertyuiopasdfghjklzxcvbnm".upper() .lower()+ "0123456789" + "!@#$%^&*()_+"
    "".join(random.sample(characters, length))
    password = "".join(random.sample(characters, length))
    return password
if __name__ =="__main__":
    password = generate_password()
    print("Generated password:", password)
    
    
