name = "manju purum";

print(len(name));

print(name.startswith("ma"));      #functions are case sensitive
print(name.endswith("ju"));
print(name.capitalize());


print(name[::-1]);              #reverse a string

print(name.upper());
print(name.lower());

print(name.title())            # capitalises each first letter of the word


sentense = "I am a good good boy";
print(sentense.replace("good", "bad"));          #replaces all the occurances of string

text = "   python is cool    ";
print(len(text.strip()));
ans = text.strip();
print(ans);
print(len(ans));



text = "manju is \"coding\" in macbook";
print(text);


# carriage return \r.      A carriage return (\r) moves the cursor back to the 
                            # beginning of the same line, without going to a new line.
import time;
for i in range(5):
    print(f"Loading {i}",end="\r");
    time.sleep(1);


print("Hello\rWorld")
print("Hello\rHi")