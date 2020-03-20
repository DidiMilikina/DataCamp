'''
Bringing it all together: Pokémon z-scores
A list of 720 Pokémon has been loaded into your session as names. Each Pokémon's corresponding Health Points is stored in a NumPy array called hps. You want to analyze the Health Points using the z-score to see how many standard deviations each Pokémon's HP is from the mean of all HPs.

The below code was written to calculate the HP z-score for each Pokémon and gather the Pokémon with the highest HPs based on their z-scores:

poke_zscores = []

for name,hp in zip(names, hps):
    hp_avg = hps.mean()
    hp_std = hps.std()
    z_score = (hp - hp_avg)/hp_std
    poke_zscores.append((name, hp, z_score))
high_hp_pokemon = []

for name,hp,zscore in poke_zscores:
    if zscore > 2:
        high_hp_pokemon.append((name, hp, zscore))
Instructions 1/3
35 XP
1
Use NumPy to eliminate the for loop used to create the z-scores.
Then, combine the names, hps, and z_scores objects together into a list called poke_zscores2.

2
Use list comprehension to replace the for loop used to collect Pokémon with the highest HPs based on their z-score.

'''
SOLUTION

1
# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

2
# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon = [(name, hp, z_scores) for name,hp,z_scores in poke_zscores2 if z_scores > 2]
print(*highest_hp_pokemon, sep='\n')