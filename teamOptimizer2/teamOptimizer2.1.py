import sys

import typeChart

teamAttackList = []
teamAttackStrengths = dict()
teamAttackWeaknesses = dict()
teamTypes = []

def getPokemonTypes():
	attackTypes = sys.argv[1].lower().split(', ')
	print('Attack types: {}'.format(attackTypes))
	for pokemonType in attackTypes:
		if pokemonType in typeChart.types:
			teamTypes.append(pokemonType)
		else:
			print('ERROR - Invalid type {}'.format(pokemonType))

def calcTeamAttack(myPokeType, attackStrengths, attackWeaknesses):
	for vsPokeType, attackMod in typeChart.attack[myPokeType].items():
		if attackMod < 1:
			if vsPokeType in attackWeaknesses.keys():
				attackWeaknesses[vsPokeType] += 1
			else:
				attackWeaknesses[vsPokeType] = 1
		elif attackMod > 1:
			if vsPokeType in attackStrengths.keys():
				attackStrengths[vsPokeType] += 1
			else:
				attackStrengths[vsPokeType] = 1
	return

###################
getPokemonTypes() #
###################

print('Team types: {}'.format(teamTypes))

for myPokeType in teamTypes:
	calcTeamAttack(myPokeType, teamAttackStrengths, teamAttackWeaknesses)

print('Attack Strengths:')
for pokeType, numStrengths in teamAttackStrengths.items():
	print('{}: {}'.format(pokeType, numStrengths))

print ('\nMissing Attack Strengths:')
print('{}'.format(set(typeChart.types).difference(teamAttackStrengths.keys())))

print('\n------------------------------------------------\n')

print('Attack Weaknesses:')
for pokeType, numWeaknesses in teamAttackWeaknesses.items():
	print('{}: {}'.format(pokeType, numWeaknesses))

print ('\nMissing Attack Weaknesses:')
print('{}'.format(set(typeChart.types).difference(teamAttackWeaknesses.keys())))