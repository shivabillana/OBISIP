import random
def generate_password(length, include_uppercase, include_lowercase, include_symbols,include_numbers):
    #Generates a random password with the specified criteria.

    #Creating Empty List
    characters = []

    #Adding characters
    if include_uppercase=="YES":
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if include_numbers=="YES":
        characters.extend(list("0123456789"))
    if include_symbols=="YES":
        characters.extend(list("!@#$%^&*()_+-=[]{};:,./<>?"))
    if include_lowercase=="YES":
        characters.extend(list("abcdefghijklmnopqrstuvwxyz"))

    #Generating Password
    random.shuffle(characters)
    password = "".join(characters[:length])
    return password

# set preferences
length =  int(input("Enter Length of the Password : "))
if(length!=0):
    uppercase = input("Whether to include uppercase letters YES/NO : ")
    lowercase = input("Whether to include lowercase letters YES/NO : ")
    symbol = input("Whether to include symbol YES/NO : ")
    number = input("Whether to include number YES/NO : ")

    #Passing Arguments
    password = generate_password(length,uppercase,lowercase,symbol,number)

    #Displaying the results
    print("Your generated password is:",password)
else:
    print("Enter Vaild Length!!")
