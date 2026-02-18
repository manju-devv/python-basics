alphabets1 = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

direction = input("type 'decode' to decode or 'encode' to encode text ").lower()
user_msg = input("enter the message to decode: ");
shift = int(input("type the shift number: "));

if(shift <= 0):
    print("please enter number greater than zero!")

new_alphabets = []
encoded_msg = ""
decoded_msg = ""
if(direction == 'encode'):
    alphabets = alphabets1.copy()
    for i in range(shift):
        last_letter = alphabets.pop();
        # alphabets.insert(0,last_letter)
        new_alphabets.insert(0,last_letter)
    new_alphabets.extend(alphabets);
    print(new_alphabets)
    message = list(user_msg)
    print(message)
    for i in message:
        # print(alphabets.index(i))
        # print(new_alphabets[alphabets.index(i)])
        encoded_msg += new_alphabets[alphabets1.index(i)]
    print(encoded_msg)
elif(direction == 'decode'):
    alphabets = alphabets1.copy()
    for i in range(shift):
        first_letter = alphabets.pop()
        new_alphabets.insert(0,first_letter)
        print(new_alphabets)
    new_alphabets.extend(alphabets)
    print(new_alphabets)
    for i in user_msg:
        # print(alphabets.index(i))
        decoded_msg += alphabets1[new_alphabets.index(i)]
    print(decoded_msg)
else:
    print("Ivalid Input!");
    