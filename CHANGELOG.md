## [1.0.3] - 2026-05-13 . . . . . . . . . . . . . . . . . .
### Adicionado
- 🧠 Novo Minigame: Implementação da lógica base para o "**Jogo da Probabilidade**".
- 🤖 IA Básica: Criado sistema de competição contra o computador baseado em geração de números aleatórios com **random**.
- 📐 Lógica de Proximidade: Desenvolvimento de algoritmo manual para calcular a diferença absoluta entre os palpites e o valor sorteado.
- 🎮 Menu de Navegação: Adicionado suporte para seleção de modos (Singleplayer e Multiplayer) via **match-case**.
- 🕹️ Modo Singleplayer: Implementação inicial das partidas contra o Computer.
### Experimental (Em desenvolvimento)
- 🏗️ Refatoração de Algoritmo: A lógica de cálculo de distância está em fase de prototipagem e será simplificada em versões futuras.
- 👥 Modo Multiplayer: Opção de menu criada, mas funcionalidade ainda não implementada.
## [1.0.2] - 2026-05-07 . . . . . . . . . . . . . . . . . .
### Adicionado
- 🎮 Implementação do Jogo da Velha (**JogoDaVelha**): Versão funcional para modo Multiplayer local. Game ja adicionado ao menu do **main** para jogar.
- ✨ Lógica de Verificação: Criado sistema de detecção de vitória para linhas, colunas e diagonais utilizando comparações encadeadas.
- 🏁 Sistema de Empate: Implementada contagem de jogadas para detectar "Velha".
- 🛡️ Validação de Entrada: Adicionado filtro para impedir jogadas em campos já ocupados ou valores inválidos.
- 🎨 UX/UI no Terminal: Uso de colorama para diferenciar os jogadores (X Azul / O Vermelho) e limpeza de tela dinâmica com os.
### Experimental (Fase de Testes)
- 🧪 O jogo ainda esta em fase de testes e esta sujeito a sofrer alterações de melhoria para um melhor desempenho.
### Alterado
- 🧹 Ajustes do nome da classe **Jogo_da_Velha** para **JogoDaVelha**.
## [1.0.1] - 2026-05-06 . . . . . . . . . . . . . . . . . .
### Adicionado
- 🎉 Criação da Classe **Jogo_da_Velha**.
- ✨ Implementação completa da opção "O melhor de 3" do jogo **Jokenpo**.
### Alterado
- 🧹 Ajustes de limpeza de tela na classe **Jokenpo** e **main** para melhor navegação.

## [1.0.0] - 2026-05-04 . . . . . . . . . . . . . . . . . .
### Adicionado
- 🎉 Estrutura inicial do projeto **Game Hub**.
- 📑 Menu principal com sistema de `match-case`.
- ✨ Implementação completa do jogo **Jokenpo**.
- 🧹 Sistema de limpeza de tela funcional no terminal do PyCharm.