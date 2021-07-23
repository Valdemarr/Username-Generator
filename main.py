import random as random
import pandas

excelsheet = pandas.read_excel("Spreadsheet_with_words.xlsx")

adjectives = excelsheet['Adjectives'].tolist()
nouns = excelsheet['Nouns'].tolist()

len_adj = len(adjectives)
len_nou = len(nouns)

#Intro
print("Welcome to the username generator. There are exactly " + str(len_adj*len_adj*len_nou) + " unique combinations")

r_adj_x2 = random.sample(adjectives, 2)

r_nou = random.choice(nouns)

r_num = random.choice(range(10, 101))

#Number option
#print("Do you want numbers in your name? Type Y / N:")
#reply = input()

#Output
#if reply == "Y" or reply == "y":
#  print(f" Your name is: {r_adj_x2[0]}{r_adj_x2[1]}{r_nou}{r_num}")
#elif reply == "N" or reply == "n":  
#  print(f" Your name is: {r_adj_x2[0]}{r_adj_x2[1]}{r_nou}")
#else:
#  print (f"You should really learn to read instructions... But here's your username without numbers: {r_adj_x2[0]}{r_adj_x2[1]}{r_nou}")

#REMOVE IF ENABLING NUMBER OPTION
print(f" Your name is: {r_adj_x2[0]}{r_adj_x2[1]}{r_nou}")


#Users can cumulatively add new words and expand the database
#Filters to avoid slurs and racism in place
#Generate name based on user input
#Randomly choose x2 adj + nou / verb + adj + nou
#Remove already generated names
#Count how many names there can be with numbers
#Make interface