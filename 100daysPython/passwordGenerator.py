import random
alphabets = [
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9'];
symbols = ['!','#','$','%','&','(',')','*','+','^'];


print("Welcome to pyPassword generator");
no_of_characters = int(input(("How many characters do you want: \n")));
no_of_numbers = int(input(("How many numbers do you want: \n")));
no_of_symbols = int(input(("How many symbols do you want: \n")));


#easy level
# password = "";
# for i in range(0,no_of_characters):
#     rand_alph = random.choice(alphabets);
#     password += rand_alph;
# for i in range(0,no_of_numbers):
#     rand_num = random.choice(numbers);
#     password += rand_num
# for i in range(0,no_of_symbols):
#     rand_symbol = random.choice(symbols);
#     password += rand_symbol
# print(password)


# hard

pass_list = []

for i in range(0,no_of_characters):
    pass_list.append(random.choice(alphabets))
for i in range(0,no_of_numbers):
    pass_list.append(random.choice(numbers))
for i in range(0,no_of_symbols):
    pass_list.append(random.choice(symbols))
    
print(pass_list);
random.shuffle(pass_list);
new_pass = "".join(pass_list)
print(f"Your strong password is: {new_pass}")

