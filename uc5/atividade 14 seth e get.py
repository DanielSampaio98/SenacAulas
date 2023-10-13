class Pokemon:
    def __init__(self, nome, hp, iv, tipos, ataqueRapido, ataquesCarregados):
        self.__nome = nome
        self.__hp = hp
        self.__iv = iv
        self.__tipos = tipos
        self.__ataqueRapido = ataqueRapido
        self.__energiaAcumulada = 0
        self.__ataquesCarregados = ataquesCarregados

    def __str__(self):
        return f"{self.__nome} HP: {self.__hp} IV: {self.__iv} Tipos: {self.__tipos} Ataque Rápido: {self.__ataqueRapido} Ataques Carregados: {self.__ataquesCarregados}"

    def atacar(self, pokemon_inimigo):
        dano = (self.__ataqueRapido.get_dano() * self.__iv) / 65
        pokemon_inimigo.set_hp(pokemon_inimigo.get_hp() - dano)
        self.__energiaAcumulada = self.__ataqueRapido.get_gera_energia() + self.__energiaAcumulada
        print(f"{self.get_nome()} causou {dano} de dano a {pokemon_inimigo.get_nome()}")
        print(f"Energia acumulada por {self.get_nome()}: {self.__energiaAcumulada}")

    def get_hp(self):
        return self.__hp

    def set_hp(self, valor):
        self.__hp = valor

    def get_nome(self):
        return self.__nome

    def set_nome(self, valor):
        self.__nome = valor


class Ataque:
    def __init__(self, nome, dano, tipo, geraEnergia):
        self.__nome = nome
        self.__dano = dano
        self.__tipo = tipo
        self.__geraEnergia = geraEnergia

    def __str__(self):
        return f"Nome: {self.__nome}, Dano: {self.__dano}, Tipo: {self.__tipo}, Energia Gerada: {self.__geraEnergia}"

    def get_nome(self):
        return self.__nome

    def get_dano(self):
        return self.__dano

    def get_tipo(self):
        return self.__tipo

    def get_gera_energia(self):
        return self.__geraEnergia


class BatalhaPokemon:
    def __init__(self, pokemon1, pokemon2):
        self.__pokemon1 = pokemon1
        self.__pokemon2 = pokemon2

    def simular_batalha(self):
        while self.__pokemon1.get_hp() > 0 and self.__pokemon2.get_hp() > 0:
            self.__pokemon1.atacar(self.__pokemon2)
            if self.__pokemon2.get_hp() <= 0:
                print(f"{self.__pokemon2.get_nome()} foi derrotado!")
                break
            self.__pokemon2.atacar(self.__pokemon1)
            if self.__pokemon1.get_hp() <= 0:
                print(f"{self.__pokemon1.get_nome()} foi derrotado!")
                break


# Manipulando a classe Ataque
caudaDeDragao = Ataque("Cauda de Dragão", 13, "Dragão", 9)
cachoeira = Ataque("Cachoeira", 16, "Água", 8)

kyogre = Pokemon("Kyogre", 174, 45, ["Água"], cachoeira, ["Surfar", "Nevasca"])
dragonite = Pokemon("Dragonite", 177, 44, ["Dragão", "Voador"], caudaDeDragao, ["Meteoro do Dragão", "Garra de Dragão"])

# Testando get e set
# Escrevi o valor do hp do Dragonite
valor = dragonite.get_hp()
print(f"HP de Dragonite: {valor}")

# Fiz o Kyogre atacar 2x
kyogre.atacar(dragonite)
kyogre.atacar(dragonite)

# Escrevi o valor do hp do Dragonite
valor = dragonite.get_hp()
print(f"HP de Dragonite após ataques do Kyogre: {valor}")

# Utilizando a classe BatalhaPokemon
batalha = BatalhaPokemon(kyogre, dragonite)
batalha.simular_batalha()
