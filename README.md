# Jogo da Forca - AP2

## Curso: Sistemas de Informação, 2º Semestre

### Descrição do Jogo

O **Jogo da Forca** é um clássico jogo de adivinhação de palavras, onde o jogador tenta descobrir uma palavra secreta, adivinhando letras uma a uma. O jogo possui um limite de 6 tentativas. A cada erro, o jogador perde uma tentativa. Se o jogador acertar todas as letras antes de esgotar as tentativas, vence; caso contrário, perde.

Este projeto utiliza conceitos de Programação Orientada a Objetos (POO), como classes, herança e encapsulamento.

### Diagrama de Classes

(O diagrama de classes pode ser inserido aqui como uma imagem ou descrição, caso você tenha um)

### Explicação Técnica

#### Classes e Atributos

- **Jogo**: Classe genérica que representa um jogo e possui atributos básicos, como `nome` e `_estado_jogo`. Inclui métodos para iniciar e finalizar o jogo.
  
- **JogoForca**: Especialização de `Jogo`, que possui atributos adicionais, como:
  - `palavras`
  - `_palavra_secreta`
  - `_tentativas`
  - `_letras_corretas`
  - `_letras_erradas`

  Esta classe é responsável pela lógica específica do jogo da Forca.

#### Métodos

- **iniciar_jogo()**: Método que inicializa o jogo.
- **finalizar_jogo()**: Método que finaliza o jogo.
- **get_tentativas() e set_tentativas()**: Métodos getters e setters para acessar e modificar o número de tentativas restantes.

### Instruções de Uso

1. **Requisitos**:
   - Python 3.6 ou superior instalado.

2. **Passos para executar**:
   - Salve o código em um arquivo chamado `jogo_forca.py`.
   - Execute o jogo no terminal com o comando:

     ```bash
     python jogo_forca.py
     ```

3. Siga as instruções exibidas no terminal para adivinhar a palavra.

### Testes

#### Vitória

- **Descrição**: O jogador acerta todas as letras da palavra antes de esgotar as tentativas.
- **Resultado Esperado**: Exibição da mensagem de vitória e término do jogo.

#### Derrota

- **Descrição**: O jogador esgota todas as tentativas sem adivinhar a palavra.
- **Resultado Esperado**: Exibição da mensagem de derrota, revelando a palavra secreta.

#### Letra Repetida

- **Descrição**: O jogador tenta adivinhar uma letra que já foi utilizada.
- **Resultado Esperado**: Exibição de uma mensagem informando que a letra já foi tentada.

#### Entrada Inválida

- **Descrição**: O jogador insere um caractere inválido (por exemplo, um número ou mais de uma letra).
- **Resultado Esperado**: Exibição de uma mensagem pedindo para inserir uma letra válida.

---

### Contribuição

1. Faça um fork deste repositório.
2. Crie uma branch para sua modificação (`git checkout -b minha-modificacao`).
3. Commit suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Envie para o repositório remoto (`git push origin minha-modificacao`).
5. Abra um Pull Request para revisão.

---
