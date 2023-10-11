class Pokemon:
    def __init__(self, nome, hp, iv, tipos, ataqueRapido, ataquesCarregados):
        self.nome = nome
        self.hp = hp
        self.iv = iv
        self.tipos = tipos
        self.ataqueRapido = ataqueRapido
        self.energiaAcumulada = 0
        self.ataquesCarregados = ataquesCarregados

    def __str__(self):
        ataques_carregados_str = [ataque.toString() for ataque in self.ataquesCarregados]
        return f"{self.nome} {self.hp} {self.iv} {self.tipos} [{self.ataqueRapido.nome}] {ataques_carregados_str}"

class Ataque: 
    def __init__(self, nome, dano, tipo, geraEnergia):
        self.nome = nome
        self.dano = dano
        self.tipo = tipo
        self.geraEnergia = geraEnergia

    def toString(self):
        return f"{self.nome} {self.dano} {self.tipo} {self.geraEnergia}"

class AtaqueCarregado:
    def __init__(self, nome, dano, energiaConsumida, tipo):
        self.nome = nome
        self.dano = dano
        self.energiaConsumida = energiaConsumida
        self.tipo = tipo
    
    def toString(self):
        return f"{self.nome} {self.dano} {self.energiaConsumida} {self.tipo}"

# Manipulando a classe Ataque
caudaDeDragao = Ataque("Cauda de Dragão", 13, "Dragão", 9)
cachoeira = Ataque("Cachoeira", 16, "Água", 8)

nevasca = AtaqueCarregado("nevasca", 140, 65, "Gelo")
jatoDeAgua = AtaqueCarregado("jatoDeÁgua", 130, 75, "Água")
meteoroDoDragao = AtaqueCarregado("meteoroDoDragão", 150, 65, "Dragão")
garraDoDragao = AtaqueCarregado("garraDoDragão", 50, 35, "Dragão")

# Manipulando a classe Pokemon
kyogre = Pokemon("Kyogre", 174, 45, ["Água"], cachoeira, [nevasca, jatoDeAgua])
dragonite = Pokemon("Dragonite", 177, 44, ["Dragão", "Voador"], caudaDeDragao, [meteoroDoDragao, garraDoDragao])

print(kyogre)
print(dragonite)
