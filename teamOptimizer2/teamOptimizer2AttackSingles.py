import json
import requests
import sys

sys.path.insert(0, 'pykemon')
import pykemon
import typeChart

pokemonTypeCache = {}
shouldSaveCache = 0

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

def calcSingleMonAttackStrengths(myPokeType):
	singleMonAttackStrengths = []
	for vsPokeType, attackMod in typeChart.attack[myPokeType].items():
		if attackMod > 1:
			if vsPokeType not in singleMonAttackStrengths:
				singleMonAttackStrengths.append(vsPokeType)
			else:
				print('Not adding: {}'.format(vsPokeType))
	return singleMonAttackStrengths

def calcSingleMonAttackWeaknesses(myPokeType):
	singleMonAttackWeaknesses = []
	for vsPokeType, attackMod in typeChart.attack[myPokeType].items():
		if attackMod < 1:
			if vsPokeType not in singleMonAttackWeaknesses:
				singleMonAttackWeaknesses.append(vsPokeType)
			else:
				print('Not adding: {}'.format(vsPokeType))
	return singleMonAttackWeaknesses

def calcTeamAttack(myPokeType, attackStrengths, attackWeaknesses):
	for vsPokeType, attackMod in typeChart.attack[myPokeType].items():
		if attackMod < 1:
			if vsPokeType not in singleMonAttackWeaknesses:
				singleMonAttackWeaknesses.append(vsPokeType)
				if vsPokeType in attackWeaknesses.keys():
					attackWeaknesses[vsPokeType] += 1
				else:
					attackWeaknesses[vsPokeType] = 1
			else:
				print('Not adding: {}'.format(vsPokeType))
		elif attackMod > 1:
			if vsPokeType not in singleMonAttackStrengths:
				singleMonAttackStrengths.append(vsPokeType)
				if vsPokeType in attackStrengths.keys():
					attackStrengths[vsPokeType] += 1
				else:
					attackStrengths[vsPokeType] = 1
			else:
				print('Not adding: {}'.format(vsPokeType))
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
	singleMonAttackStrengths = []
	singleMonAttackWeaknesses = []
	singleMonDefenseSuperStrengths = []
	singleMonDefenseStrengths = []
	singleMonDefenseWeaknesses = []
	singleMonDefenseSuperWeaknesses = []

	#Iterate over each pokemon type in the team
	typeAttackStrengths = []
	typeAttackWeaknesses = []
	for myPokeType in mon: # Assumes pokeapi will only return valid type combos
		typeAttackStrengths.extend(calcSingleMonAttackStrengths(myPokeType))
		typeAttackWeaknesses.extend(calcSingleMonAttackWeaknesses(myPokeType))

		# Defense
		calcTeamDefense(myPokeType, defenseMonMods)

	# Offense
	for pokeType in typeAttackStrengths:
		if pokeType not in singleMonAttackStrengths:
			singleMonAttackStrengths.append(pokeType)
	print("{} Attack Strengths: {}".format(mon, singleMonAttackStrengths))

	for pokeType in typeAttackWeaknesses:
		if pokeType not in singleMonAttackWeaknesses:
			singleMonAttackWeaknesses.append(pokeType)
	print("{} Attack Weaknesses: {}".format(mon, singleMonAttackWeaknesses))

	#Defense calc can be betwee 0 and 4, this separates the valid values into their own dicts
	for vsPokeType, defenseMod in defenseMonMods.items():
		# if defenseMod == 0:
		# 	if vsPokeType in teamDefenseNoEffect.keys():
		# 		teamDefenseNoEffect[vsPokeType] += 1
		# 	else:
		# 		teamDefenseNoEffect[vsPokeType] = 1
		# elif defenseMod == 0.25:
		# 	if vsPokeType in teamDefenseSuperStrengths.keys():
		# 		teamDefenseSuperStrengths[vsPokeType] += 1
		# 	else:
		# 		teamDefenseSuperStrengths[vsPokeType] = 1
		# elif defenseMod == 0.5:
		# 	if vsPokeType in teamDefenseStrengths.keys():
		# 		teamDefenseStrengths[vsPokeType] += 1
		# 	else:
		# 		teamDefenseStrengths[vsPokeType] = 1
		if defenseMod == 2:
			singleMonDefenseWeaknesses.append(vsPokeType)
		elif defenseMod == 4:
			singleMonDefenseSuperWeaknesses.append(vsPokeType)
	print("{} Defense Weaknesses: {}".format(mon, singleMonDefenseWeaknesses))
	print("{} Defense Super Weaknesses: {}".format(mon, singleMonDefenseSuperWeaknesses))