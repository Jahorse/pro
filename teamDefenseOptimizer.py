import sys

types = [
	'bug',
	'dark',
	'dragon',
	'electric',
	'fairy',
	'fighting',
	'fire',
	'flying',
	'ghost',
	'grass',
	'ground',
	'ice',
	'normal',
	'poison',
	'psychic',
	'rock',
	'steel',
	'water']




allDefense = {
	'electric': {'electric': 0.5, 'ground': 2, 'steel': 0.5, 'flying': 0.5},
	'poison': {'poison': 0.5, 'grass': 0.5, 'ground': 2, 'psychic': 2, 'fairy': 0.5, 'bug': 0.5, 'fighting': 0.5},
	'grass': {'ice': 2, 'poison': 2, 'grass': 0.5, 'ground': 0.5, 'fire': 2, 'water': 0.5, 'electric': 0.5, 'bug': 2, 'flying': 2},
	'ground': {'ice': 2, 'poison': 0.5, 'grass': 2, 'water': 2, 'electric': 0, 'rock': 0.5},
	'fire': {'ice': 0.5, 'grass': 0.5, 'ground': 2, 'steel': 0.5, 'fire': 0.5, 'water': 2, 'rock': 2, 'bug': 0.5, 'fairy': 0.5},
	'rock': {'poison': 0.5, 'grass': 2, 'ground': 2, 'steel': 2, 'fire': 0.5, 'water': 2, 'normal': 0.5, 'flying': 0.5, 'fighting': 2},
	'normal': {'fighting': 2, 'ghost': 0},
	'bug': {'flying': 2, 'grass': 0.5, 'ground': 0.5, 'fire': 2, 'rock': 2, 'bug': 2, 'fighting': 0.5},
	'ice': {'ice': 0.5, 'rock': 2, 'steel': 2, 'fire': 2, 'fighting': 2},
	'psychic': {'fighting': 0.5, 'psychic': 0.5, 'dark': 2, 'ghost': 2},
	'steel': {'poison': 0, 'grass': 0.5, 'ground': 2, 'fire': 2, 'rock': 0.5, 'normal': 0.5, 'bug': 0.5, 'ice': 0.5, 'psychic': 0.5, 'steel': 0.5, 'dragon': 0.5, 'fairy': 0.5, 'flying': 0.5, 'fighting': 2},
	'water': {'ice': 0.5, 'grass': 2, 'steel': 0.5, 'fire': 0.5, 'water': 0.5, 'electric': 2},
	'dragon': {'ice': 2, 'grass': 0.5, 'fire': 0.5, 'water': 0.5, 'electric': 0.5, 'dragon': 2, 'fairy': 2},
	'ghost': {'ghost': 2, 'poison': 0.5, 'normal': 0, 'dark': 2, 'bug': 0.5, 'fighting': 0},
	'dark': {'psychic': 0, 'fairy': 2, 'ghost': 0.5, 'dark': 0.5, 'bug': 2, 'fighting': 2},
	'flying': {'ice': 2, 'grass': 0.5, 'ground': 0, 'electric': 2, 'bug': 0.5, 'rock': 2, 'fighting': 0.5},
	'fighting': {'psychic': 2, 'rock': 0.5, 'fairy': 2, 'dark': 0.5, 'bug': 0.5, 'flying': 2},
	'fairy': {'poison': 2, 'steel': 2, 'dragon': 0, 'dark': 0.5, 'bug': 0.5, 'fighting': 0.5}}

teamDefenseList = []
teamDefenseNoEffect = dict()
teamDefenseSuperStrengths = dict()
teamDefenseStrengths = dict()
teamDefenseWeaknesses = dict()
teamDefenseSuperWeaknesses = dict()
team = []

for argv in sys.argv[1:]:
	monTypeList = argv.split(',')
	if set(monTypeList).issubset(types):
		team.append(monTypeList)
	else:
		print('{} isn\'t a valid type'.format(monTypeList))

if len(team) > 6:
	print('Cannot have more than 6 mons on a team')
	exit(1)

print('Team: {}\n'.format(team))

for mon in team:
	defenseMonMods = dict()
	for myPokeType in mon: # Should only be 1 or 2 here, need to add a check when building the team that it isn't more than 2
		# Defense
		for vsPokeType, defenseMod in allDefense[myPokeType].items():
			if vsPokeType in defenseMonMods.keys():
				defenseMonMods[vsPokeType] *= defenseMod
			else:
				defenseMonMods[vsPokeType] = defenseMod


	for vsPokeType, defenseMod in defenseMonMods.items():
		if defenseMod == 0:
			if vsPokeType in teamDefenseNoEffect.keys():
				teamDefenseNoEffect[vsPokeType] += 1
			else:
				teamDefenseNoEffect[vsPokeType] = 1
		elif defenseMod == 0.25:
			if vsPokeType in teamDefenseSuperStrengths.keys():
				teamDefenseSuperStrengths[vsPokeType] += 1
			else:
				teamDefenseSuperStrengths[vsPokeType] = 1
		elif defenseMod == 0.5:
			if vsPokeType in teamDefenseStrengths.keys():
				teamDefenseStrengths[vsPokeType] += 1
			else:
				teamDefenseStrengths[vsPokeType] = 1
		elif defenseMod == 2:
			if vsPokeType in teamDefenseWeaknesses.keys():
				teamDefenseWeaknesses[vsPokeType] += 1
			else:
				teamDefenseWeaknesses[vsPokeType] = 1
		elif defenseMod == 4:
			if vsPokeType in teamDefenseSuperWeaknesses.keys():
				teamDefenseSuperWeaknesses[vsPokeType] += 1
			else:
				teamDefenseSuperWeaknesses[vsPokeType] = 1

print('Defense No Effect:')
for pokeType, numStrengths in teamDefenseNoEffect.items():
	print('{}: {}'.format(pokeType, numStrengths))

print ('\nMissing Defense No Effects:')
print('{}'.format(set(types).difference(teamDefenseNoEffect.keys())))

print('\n------------------------------------------------\n')

print('Defense Super Strengths:')
for pokeType, numStrengths in teamDefenseSuperStrengths.items():
	print('{}: {}'.format(pokeType, numStrengths))

print ('\nMissing Defense Super Strengths:')
print('{}'.format(set(types).difference(teamDefenseSuperStrengths.keys())))

print('\n------------------------------------------------\n')

print('Defense Strengths:')
for pokeType, numStrengths in teamDefenseStrengths.items():
	print('{}: {}'.format(pokeType, numStrengths))

print ('\nMissing Defense Strengths:')
print('{}'.format(set(types).difference(teamDefenseStrengths.keys())))

print('\n------------------------------------------------\n')

print('Defense Weaknesses:')
for pokeType, numStrengths in teamDefenseWeaknesses.items():
	print('{}: {}'.format(pokeType, numStrengths))

print ('\nMissing Defense Weaknesses:')
print('{}'.format(set(types).difference(teamDefenseWeaknesses.keys())))

print('\n------------------------------------------------\n')

print('Defense Super Weaknesses:')
for pokeType, numStrengths in teamDefenseSuperWeaknesses.items():
	print('{}: {}'.format(pokeType, numStrengths))

print ('\nMissing Defense Super Weaknesses:')
print('{}'.format(set(types).difference(teamDefenseSuperWeaknesses.keys())))