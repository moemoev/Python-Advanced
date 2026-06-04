from project.pokemon import Pokemon
#note: does work when executing from main, needs to be done for the judge to load the module pokemn, still underlined
# red...as of now no fix for that


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        # pokemon_details returns exactly the info we need, so we use it
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        if not any(pokemon for pokemon in self.pokemons if pokemon_name == pokemon.name):
            return f"Pokemon is not caught"
        for i, pokemon in enumerate(self.pokemons):
            if pokemon.name == pokemon_name:
                del self.pokemons[i]
                return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            result += f"- {Pokemon.pokemon_details(pokemon)}\n"
        return result
