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

print(allAttack)