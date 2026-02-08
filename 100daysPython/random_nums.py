import random


rand_num_float = random.random() * 10
print(rand_num_float)

rand_uni = random.uniform(1, 10)
print(rand_uni)


heads_or_tails = random.randint(1, 2)
print(heads_or_tails)

print("heads" if heads_or_tails == 1 else "tails")
