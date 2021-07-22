import random

adjectives = ["Blue", "Human", "Salty", "Big", "Sour", "Round", "Ugly", "Pretty", "Odd", "Long", "Fat"]
nouns = ["Human", "Ball", "Sky", "Remote", "Child", "Chips", "Youngster", "Beverage", "Sidewalk", "Meat" , "Yeeter"]

r_adj_x2 = random.sample(adjectives, 2)

r_nou = random.choice(nouns)

r_num = random.choice(range(10, 101))

print("Do you want numbers in your name? Type Y / N:")
reply = input()

if reply == "Y" or reply == "y":
  print(f" Your name is: {r_adj_x2[0]}{r_adj_x2[1]}{r_nou}{r_num}")
elif reply == "N" or reply == "n":  
  print(f" Your name is: {r_adj_x2[0]}{r_adj_x2[1]}{r_nou}")
else:
  print (f"You should really learn to read instructions... But here's your username without numbers: {r_adj_x2[0]}{r_adj_x2[1]}{r_nou}")

#Print are you ready for a name? we have len(adjectives) x len(nouns) unique combinations