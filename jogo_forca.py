import random 

#classe génerica para jogo
class Jogo:
    def __init__(self, nome):
        self.nome = nome
        self.estado_jogo = "Em andamento"

    #inicia o jogo genérico
    def iniciar_jogo(self):
        print(f"Iniciando um jogo genérico: ")
    #finaliza o jogo
    def finalizar_jogo(self):
        print("O jogo terminou.")
        self.estado_jogo = "Finalizado"
        print('\n')

    #exibe o andamento do jogo    
    def exibir_estado(self):
        return self.estado_jogo

#classe herdada da classe Jogo(herança)
class JogoForca(Jogo):
    def __init__(self, palavras):
        super().__init__("Forca")
        self.palavras = palavras
        self.palavra_secreta = random.choice(self.palavras).upper() #palavra secreta é escolhida na lista de palavras disponiveis
        self._tentativas = 6
        self.letras_corretas = set()
        self.letras_erradas = set()

    #inicia o jogo da forca especificamente(herança)
    def iniciar_jogo(self):
        print(f"Iniciando o jogo da {self.nome}")
        self.jogar()

    #setter
    def set_tentativas(self, valor):
        if valor >= 0:
            self._tentativas = valor

    #getter
    def get_tentativas(self):
        return self._tentativas

    #inicio do jogo
    def jogar(self):
    
        while self._tentativas > 0:
            self.exibir_estado_forca()
            letra = input("Digite uma letra: ").upper()
            print('\n')

            #valida entrada
            if len(letra) != 1 or not letra.isalpha():
                print("Insira apenas uma letra.")
                print('\n')
                continue

            #valida se a letra foi tentada
            if letra in self.letras_corretas or letra in self.letras_erradas:
                print("Essa letra já foi tentada!")
                print('\n')
                continue

            #lógica de acerto ou erro
            if letra in self.palavra_secreta:
                self.letras_corretas.add(letra)
                if self.verificar_vitoria():
                    print(f"Parabéns! Você acertou a palavra: {self.palavra_secreta}")
                    self.finalizar_jogo()
                    break
            else:
                self.letras_erradas.add(letra)
                self.set_tentativas(self.get_tentativas() - 1)
                print(f"Letra incorreta! Tentativas restantes: {self.get_tentativas()}")
                print('\n')

        if self._tentativas == 0:
            print(f"Você perdeu. A palavra era: {self.palavra_secreta}")
            self.finalizar_jogo()

    #estado atual da palavra
    def exibir_estado_forca(self):
        estado = [letra if letra in self.letras_corretas else '_' for letra in self.palavra_secreta]
        print("Palavra: ", " ".join(estado))
        print("Letras erradas: ", " ".join(sorted(self.letras_erradas)))

    #verifica se o jogador venceu
    def verificar_vitoria(self):
        return set(self.palavra_secreta) == self.letras_corretas


if __name__ == "__main__":
    palavras = ["python", "sistemas de informacao", "rede", "linguagem", "desenvolvimento"]
    jogo = JogoForca(palavras)
    jogo.iniciar_jogo()