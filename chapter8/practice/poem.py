with open("poem.txt", "r") as f:
    content = f.read()
    if "twinkle" in content.lower():
        print("the word 'twinkle' is present in the poem")
    else:
        print("the word 'twinkle' is not present in the poem")
