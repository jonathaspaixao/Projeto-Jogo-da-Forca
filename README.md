# Projeto-Jogo-da-Forca

# Documentação do Projeto

#Jogo da Forca

#Descrição do Jogo

O Jogo da Forca é um jogo clássico de adivinhação de palavras, onde o jogador tenta descobrir uma palavra secreta, adivinhando letras uma a uma. Com um limite de 6 tentativas, a cada erro, o jogador perde uma tentativa. Se acertar todas as letras antes de esgotar as tentativas, vence; caso contrário, perde. Este jogo usa conceitos de POO como classes, herança e encapsulamento.	

#Explicação Técnica

     Classes e Atributos

Jogo: Classe genérica que representa um jogo e possui atributos básicos como    nome e _estado_jogo. Inclui métodos para iniciar e finalizar o jogo.
JogoForca: Especialização de Jogo, possui atributos adicionais como palavras, _palavra_secreta, _tentativas, _letras_corretas, e _letras_erradas. É responsável pela lógica específica do jogo da Forca.

     Métodos 

iniciar_jogo(): Método que inicializa o jogo.
finalizar_jogo(): Método que finaliza o jogo.
get_tentativas() e set_tentativas(): Getters e setters para acessar e modificar o número de tentativas restantes.
     	
	
#Instruções de Uso

Python 3.6 ou superior instalado.
Salve o código em um arquivo chamado jogo_forca.py.
Execute o jogo no terminal usando o comando: “python jogo_forca.py”.
Siga as instruções do jogo para adivinhar a palavra.


#Testes

Vitória: O jogador acerta todas as letras da palavra antes de esgotar as tentativas.
Resultado esperado: Exibição da mensagem de vitória e término do jogo.

Derrota: O jogador esgota todas as tentativas sem adivinhar a palavra.
Resultado esperado: Exibição da mensagem de derrota com a palavra secreta.

Letra Repetida: O jogador tenta adivinhar uma letra que já foi utilizada.
Resultado esperado: Exibição de uma mensagem informando que a letra já foi   tentada.

Entrada Inválida: O jogador insere um caractere inválido.
Resultado esperado: Exibição de uma mensagem pedindo uma letra válida.
