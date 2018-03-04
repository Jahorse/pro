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
	'bug': {'bug': 2, 'ghost': 0.5, 'grass': 2, 'steel': 0.5, 'fire': 0.5, 'dark': 2, 'fighting': 0.5, 'flying': 0.5, 'poison': 0.5, 'fairy': 0.5},
	'psychic': {'fighting': 2, 'psychic': 0.5, 'steel': 0.5, 'poison': 2, 'dark': 0},
	'ghost': {'ghost': 2, 'psychic': 2, 'normal': 0, 'dark': 0.5},
	'dragon': {'dragon': 2, 'steel': 0.5, 'fairy': 0},
	'steel': {'electric': 0.5, 'steel': 0.5, 'fire': 0.5, 'water': 0.5, 'ice': 2, 'rock': 2, 'fairy': 2},
	'fire': {'bug': 2, 'dragon': 0.5, 'steel': 2, 'fire': 0.5, 'water': 0.5, 'grass': 2, 'ice': 2, 'rock': 0.5},
	'water': {'grass': 0.5, 'fire': 2, 'water': 0.5, 'dragon': 0.5, 'rock': 2, 'ground': 2},
	'ice': {'dragon': 2, 'steel': 0.5, 'fire': 0.5, 'water': 0.5, 'flying': 2, 'ice': 0.5, 'ground': 2, 'grass': 2},
	'poison': {'grass': 2, 'steel': 0, 'ghost': 0.5, 'rock': 0.5, 'ground': 0.5, 'fairy': 2, 'poison': 0.5},
	'fairy': {'dragon': 2, 'steel': 0.5, 'fire': 0.5, 'dark': 2, 'fighting': 2, 'poison': 0.5},
	'electric': {'electric': 0.5, 'grass': 0.5, 'flying': 2, 'water': 2, 'dragon': 0.5, 'ground': 0},
	'grass': {'bug': 0.5, 'dragon': 0.5, 'steel': 0.5, 'fire': 0.5, 'water': 2, 'poison': 0.5, 'flying': 0.5, 'rock': 2, 'ground': 2, 'grass': 0.5},
	'normal': {'ghost': 0, 'rock': 0.5, 'steel': 0.5},
	'dark': {'fighting': 0.5, 'ghost': 2, 'psychic': 2, 'fairy': 0.5, 'dark': 0.5},
	'fighting': {'bug': 0.5, 'normal': 2, 'steel': 2, 'dark': 2, 'ghost': 0, 'flying': 0.5, 'ice': 2, 'rock': 2, 'poison': 0.5, 'fairy': 0.5, 'psychic': 0.5},
	'flying': {'bug': 2, 'electric': 0.5, 'grass': 2, 'steel': 0.5, 'fighting': 2, 'rock': 0.5},
	'rock': {'bug': 2, 'steel': 0.5, 'fire': 2, 'fighting': 0.5, 'flying': 2, 'ice': 2, 'ground': 0.5},
	'ground': {'bug': 0.5, 'electric': 2, 'grass': 0.5, 'steel': 2, 'fire': 2, 'flying': 0, 'rock': 2, 'poison': 2}}

teamAttackList = []
teamAttackStrengths = dict()
teamAttackWeaknesses = dict()
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