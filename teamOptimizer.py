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


allAttack = {
	'bug': {
		'bug': 2,
		'dark': 2,
		'fairy': 0.5,
		'fighting': 0.5,
		'fire': 0.5,
		'flying': 0.5,
		'ghost': 0.5,
		'grass': 2,
		'poison': 0.5,
		'steel': 0.5},
	'dark': {
		'dark': 0.5,
		'fairy': 0.5,
		'fighting': 0.5,
		'ghost': 2,
		'psychic': 2},
	'dragon': {
		'dragon': 2,
		'fairy': 0,
		'steel': 0.5},
	'electric': {
		'dragon': 0.5,
		'electric': 0.5,
		'flying': 2,
		'grass': 0.5,
		'ground': 0,
		'water': 2},
	'fairy': {
		'dark': 2,
		'dragon': 2,
		'fighting': 2,
		'fire': 0.5,
		'poison': 0.5,
		'steel': 0.5},
	'fighting': {
		'bug': 0.5,
		'dark': 2,
		'fairy': 0.5,
		'flying': 0.5,
		'ghost': 0,
		'ice': 2,
		'normal': 2,
		'poison': 0.5,
		'psychic': 0.5,
		'rock': 2,
		'steel': 2},
	'fire': {
		'bug': 2,
		'dragon': 0.5,
		'fire': 0.5,
		'grass': 2,
		'ice': 2,
		'rock': 0.5,
		'steel': 2,
		'water': 0.5},
	'flying': {
		'bug': 2,	
		'electric': 0.5,
		'fighting': 2,
		'grass': 2,
		'rock': 0.5,
		'steel': 0.5},
	'ghost': {
		'dark': 0.5,
		'ghost': 2,
		'normal': 0,
		'psychic': 2},
	'grass': {
		'bug': 0.5,
		'dragon': 0.5,
		'fire': 0.5,
		'flying': 0.5,
		'grass': 0.5,
		'ground': 2,
		'poison': 0.5,
		'rock': 2,
		'steel': 0.5,
		'water': 2},
	'ground': {
		'bug': 0.5,
		'electric': 2,
		'fire': 2,
		'flying': 0,
		'grass': 0.5,
		'poison': 2,
		'rock': 2,
		'steel': 2}, 
	'ice': {
		'dragon': 2,
		'fire': 0.5,
		'flying': 2,
		'grass': 2,
		'ground': 2,
		'ice': 0.5,
		'steel': 0.5,
		'water': 0.5},
	'normal': {
		'ghost': 0,
		'rock': 0.5,
		'steel': 0.5},
	'poison': {
		'fairy': 2,
		'ghost': 0.5,
		'grass': 2,
		'ground': 0.5,
		'poison': 0.5,
		'rock': 0.5,
		'steel': 0},
	'psychic': {
		'dark': 0,
		'fighting': 2,
		'poison': 2,
		'psychic': 0.5,
		'steel': 0.5},
	'rock': {
		'bug': 2,
		'fighting': 0.5,
		'fire': 2,
		'flying': 2,
		'ground': 0.5,
		'ice': 2,
		'steel': 0.5},
	'steel': {
		'electric': 0.5,
		'fairy': 2,
		'fire': 0.5,
		'ice': 2,
		'rock': 2,
		'steel': 0.5,
		'water': 0.5},
	'water': {
		'dragon': 0.5,
		'fire': 2,
		'grass': 0.5,
		'ground': 2,
		'rock': 2,
		'water': 0.5}}

allDefense = dict()
for attackType, defenseTypes in allAttack.items():
	for defenseType, attackMod in defenseTypes.items():
		if defenseType not in allDefense.keys():
			allDefense[defenseType] = dict()
		allDefense[defenseType][attackType] = attackMod

teamAttackList = []
teamAttackStrengths = dict()
teamAttackWeaknesses = dict()
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
		# Offense
		for vsPokeType, attackMod in allAttack[myPokeType].items():
			if attackMod < 1:
				if vsPokeType in teamAttackWeaknesses.keys():
					teamAttackWeaknesses[vsPokeType] += 1
				else:
					teamAttackWeaknesses[vsPokeType] = 1
			elif attackMod > 1:
				if vsPokeType in teamAttackStrengths.keys():
					teamAttackStrengths[vsPokeType] += 1
				else:
					teamAttackStrengths[vsPokeType] = 1

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

print('Attack Strengths:')
for pokeType, numStrengths in teamAttackStrengths.items():
	print('{}: {}'.format(pokeType, numStrengths))

print ('\nMissing Attack Strengths:')
print('{}'.format(set(types).difference(teamAttackStrengths.keys())))

print('\n------------------------------------------------\n')

print('Attack Weaknesses:')
for pokeType, numWeaknesses in teamAttackWeaknesses.items():
	print('{}: {}'.format(pokeType, numWeaknesses))

print ('\nMissing Attack Weaknesses:')
print('{}'.format(set(types).difference(teamAttackWeaknesses.keys())))

print('\n------------------------------------------------\n')

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