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

attack = {
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

defense = {
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