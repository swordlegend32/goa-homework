import random  
Cities = ["Seattle", "San Francisco", "Los Angeles", "Denver", "Salt Lake City", "Phoenix", "Chicago", "St. Louis", "Dallas", "Boston", "Washington D.C.", "Miami"]

print(Cities[2])
print(Cities[6])

print(Cities[len(Cities)//2 - 1:len(Cities)//2 + 1])
random.shuffle(Cities)
print(Cities)