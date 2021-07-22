import random

adjectives = ["Blue", "Human", "Salty", "Big", "Sour", "Round", "Ugly", "Pretty", "Odd", "Long", "Fat"]
nouns = ["Human", "Ball", "Sky", "Remote", "Child", "Chips", "Youngster", "Bevarage", "Sidewalk", "Meat"]

two_r_adj = random.sample(adjectives, 2)

r_nou = random.choice(nouns)

print(f" Your name is: {two_r_adj[0]} {two_r_adj[1]} {r_nou}")