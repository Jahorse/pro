import json
import requests
import sys

sys.path.insert(0, 'pykemon')
import pykemon
import typeChart

pokemonTypeCache = {}
shouldSaveCache = 0

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

def loadPokemonCache():
	with open('../pokemonTypeCache.json', 'r') as f:
		cache = json.load(f)
	return cache

def savePokemonCache():
		with open('pokemonTypeCache.json', 'w') as f:
			json.dump(pokemonTypeCache, f, sort_keys=True, indent=4)

def getPokemonTypes():
	pokemonNames = sys.argv[1].lower().split(', ')
	print('Names: {}'.format(pokemonNames))
	for pokemonName in pokemonNames:
		if "mega " in pokemonName:
			pokemonName = pokemonName.replace('"', '').replace('mega ', '')
		print('Trying: {}'.format(pokemonName))
		if pokemonName in pokemonTypeCache.keys():
			print('Using cached {}'.format(pokemonName))
			team.append(pokemonTypeCache[pokemonName])
		else:
			pokemon = pykemon.get(pokemon=pokemonName)

			if pokemon:
				if pokemon.types:
					team.append(pokemon.types.keys())
					pokemonTypeCache[pokemonName] = pokemon.types.keys()
					shouldSaveCache = 1
				else:
					print('ERROR - Couldn\'t read types from pokemon {}'.format(pokemon))
			else:
				print('ERROR - Couldn\'t get pokemon {}'.format(pokemon))

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

def calcTeamDefense(myPokeType, monMods):
	for vsPokeType, defenseMod in typeChart.defense[myPokeType].items():
		if vsPokeType in defenseMonMods.keys():
			monMods[vsPokeType] *= defenseMod
		else:
			monMods[vsPokeType] = defenseMod
	return

pokemonTypeCache = loadPokemonCache()
getPokemonTypes()
savePokemonCache()

print('Team: {}'.format(team))

for mon in team:
	defenseMonMods = dict()
	#Iterate over each pokemon type in the team
	for myPokeType in mon: # Assumes pokeapi will only return valid type combos
		calcTeamAttack(myPokeType, teamAttackStrengths, teamAttackWeaknesses)

		# Defense
		calcTeamDefense(myPokeType, defenseMonMods)

	#Defense calc can be betwee 0 and 4, this separates the valid values into their own dicts
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
print('{}'.format(set(typeChart.types).difference(teamAttackStrengths.keys())))

print('\n------------------------------------------------\n')

print('Attack Weaknesses:')
for pokeType, numWeaknesses in teamAttackWeaknesses.items():
	print('{}: {}'.format(pokeType, numWeaknesses))

print ('\nMissing Attack Weaknesses:')
print('{}'.format(set(typeChart.types).difference(teamAttackWeaknesses.keys())))

print('\n------------------------------------------------\n')

print('Defense No Effect:')
for pokeType, numStrengths in teamDefenseNoEffect.items():
	print('{}: {}'.format(pokeType, numStrengths))

print ('\nMissing Defense No Effects:')
print('{}'.format(set(typeChart.types).difference(teamDefenseNoEffect.keys())))

print('\n------------------------------------------------\n')

print('Defense Super Strengths:')
for pokeType, numStrengths in teamDefenseSuperStrengths.items():
	print('{}: {}'.format(pokeType, numStrengths))

print ('\nMissing Defense Super Strengths:')
print('{}'.format(set(typeChart.types).difference(teamDefenseSuperStrengths.keys())))

print('\n------------------------------------------------\n')

print('Defense Strengths:')
for pokeType, numStrengths in teamDefenseStrengths.items():
	print('{}: {}'.format(pokeType, numStrengths))

print ('\nMissing Defense Strengths:')
print('{}'.format(set(typeChart.types).difference(teamDefenseStrengths.keys())))

print('\n------------------------------------------------\n')

print('Defense Weaknesses:')
for pokeType, numStrengths in teamDefenseWeaknesses.items():
	print('{}: {}'.format(pokeType, numStrengths))

print ('\nMissing Defense Weaknesses:')
print('{}'.format(set(typeChart.types).difference(teamDefenseWeaknesses.keys())))

print('\n------------------------------------------------\n')

print('Defense Super Weaknesses:')
for pokeType, numStrengths in teamDefenseSuperWeaknesses.items():
	print('{}: {}'.format(pokeType, numStrengths))

print ('\nMissing Defense Super Weaknesses:')
print('{}'.format(set(typeChart.types).difference(teamDefenseSuperWeaknesses.keys())))