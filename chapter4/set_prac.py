# words = {
#     "resilient": "able to recover quickly from problems",
#     "meticulous": "very careful and detailed",
#     "ambiguous": "having more than one meaning; not clear",
# }

# # word = input("Enter word to know meaning: ");
# # wordToSearch = word.lower();

# # meaning = words[wordToSearch];
# # if meaning :
# #     print(meaning);
# # else: 
# #     print(f"{wordToSearch} not found");

# # above code throws err runtime err so 

# word = input("Enter word to know meaning: ").lower();
# meaning = words.get(word);
# if meaning:
#     print(meaning)
# else:
#     print(f"The word'{word}' not found in dictionary!");




# take 8  numbers from user and print unique values


# repeat = 8;
# uni_nums = set();
# for i in range(repeat):
#     user_input = int(input("Enter number: "));
#     uni_nums.add(user_input);

# print(uni_nums);


# take 4 friends name and languages and store in dictionary


# lang_dict = {};

# for i in range(4):
#     name = input("enter name: ");
#     lang = input("enter language: ");
#     lang_dict.update({name: lang});    


# print(lang_dict);


s = {1,2,"manju",(1,2,3)};
print(s[0]);