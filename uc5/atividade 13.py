class PersonagemMinecraft:
    def __init__(self, saude, nome, habito):
        self.saude = saude
        self.nome = nome
        self.habito = habito

    def __str__(self):
        return f"Nome: {self.nome}\nSaúde: {self.saude}\nHábito: {self.habito}"

class CreeperMinecraft(PersonagemMinecraft):
    def __init__(self, saude, raio_explosao, raio_perseguicao, velocidade, nome, habito, explosao_silenciosa):
        super().__init__(saude, nome, habito)
        self.raio_explosao = raio_explosao
        self.raio_perseguicao = raio_perseguicao
        self.velocidade = velocidade
        self.explosao_silenciosa = explosao_silenciosa

    def __str__(self):
        return super().__str__() + f"\nRaio de Explosão: {self.raio_explosao}\nRaio de Perseguição: {self.raio_perseguicao}\nVelocidade: {self.velocidade}\nExplosão Silenciosa: {self.explosao_silenciosa}"

class EsqueletoMinecraft(PersonagemMinecraft):
    def __init__(self, saude, arco, flechas, nome, habito, armadura, raio_perseguicao, ataque_distancia):
        super().__init__(saude, nome, habito)
        self.arco = arco
        self.flechas = flechas
        self.armadura = armadura
        self.ataque_distancia = ataque_distancia
        self.raio_perseguicao = raio_perseguicao

    def __str__(self):
        return super().__str__() + f"\nArco: {self.arco}\nFlechas: {self.flechas}\nArmadura: {self.armadura}\nRaio de Perseguição: {self.raio_perseguicao}\nPrecisão de Ataque à Distância: {self.ataque_distancia}"

class JogadorMinecraft(PersonagemMinecraft):
    def __init__(self, saude, nome, habito, posicao):
        super().__init__(saude, nome, habito)
        self.posicao = posicao

    def mover(self, nova_posicao):
        self.posicao = nova_posicao

    def __str__(self):
        return super().__str__() + f"\nPosição: {self.posicao}"

# Criando um Creeper do Minecraft
creeper = CreeperMinecraft(20, "3 blocos", "16 blocos", 2, "Creeper", "Dia, Noturno", False)

# Exibindo informações do Creeper
print(creeper)

# Criando um Esqueleto do Minecraft
esqueleto = EsqueletoMinecraft(20, "Arco de Ferro", 10, "Esqueleto", "Noturno", "Nenhuma", "15 blocos", "16 blocos")

# Exibindo informações do Esqueleto
print(esqueleto)

# Criando um Jogador do Minecraft com posição inicial
jogador = JogadorMinecraft(100, "Steve", "Dia, Noturno", (0, 0, 0))

# Exibindo informações do Jogador
print(jogador)

# Movendo o Jogador para uma nova posição
nova_posicao = (10, 20, 30)
jogador.mover(nova_posicao)

# Exibindo a nova posição do Jogador
print(f"Nova posição do Jogador: {jogador.posicao}")
