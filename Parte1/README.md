# MicroVisaoArtificial_24-25

# Parte 1


Miguel Riem Oliveira <mriem@ua.pt>

# Sumário

 - Introdução
 - Apresentação
 - Objetivos
 - Avaliação
 - Editores e IDEs
 - Tutoriais de OpenCV

# Pressupostos para a realização dos exercícios
- Ter o Linux ou Windows instalado.
- Ter o acesso de rede configurado (_wireless_).
  *   Consultar as instruções do site dos 
http://www.ua.pt/stic/PageText.aspx?id=15224[sTIC].


# Apresentação da UC

Ver slides de apresentação da UC.

## Metodologia

Para melhor se desenvolver o trabalho nas aulas, deve-se
seguir uma metodologia de organização de ficheiros em diretórios
por aulas e por exercícios.

Dentro de cada aula, em especial nas primeiras, é também recomendado criar uma subpasta para cada exercício `Ex1`, `Ex2`, etc. Em certas aulas, ou aulas mais avançadas, os diversos exercícios serão feitos por acréscimo sucessivo sobre o código base dos exercícios anteriores; nessa altura serão dadas as instruções nesse sentido.

Os guiões para as aulas estarão a ser continuamente atualizados em:

https://github.com/miguelriemoliveira/MVA_24-25

Recomenda-se que, sempre que possível, usem a versão online ou façam o update frequentemente.

## Editor

A ferramenta principal para criar e modificar ficheiros é o editor, muitas
vezes integrado num ambiente de desenvolvimento (IDE). Há inúmeras opções
desde simples editores (`gedit`, `kate`, `kwrite`, etc.) até ambientes de
desenvolvimento muito sofisticados (`codeblocks`, `eclipse`, `vscode`,`pycharm` etc.).

Além das propriedades fundamentais dos editores, hoje em dia são excelentes
_add-ons_ a "automated completion" (preenchimento automático de palavras
e estruturas) , o "syntax highlight" (realce da sintaxe da linguagem),
o "intellissense" (apresentação de todas as opções de preenchimento
automático de campos e estruturas em variáveis, funções, etc.), ou a
inserção automática de fragmentos de código padrão ("code snippets").

O editor com mais tradição por excelência é o "vim" (ou "vi" improuved)
mas a sua utilização eficaz pode requerer anos de prática continuada e
permite todas as facilidades indicadas acima, mas a sua configuração,
por ser praticamente ilimitada, pode-se tornar complexa e, por isso,
contraproducente em utilizadores iniciados.

**Recomenda-se como IDE** o https://code.visualstudio.com/[vscode], que é gratuito.

## OpenCV

O https://opencv.org/[OpenCV] é a biblioteca de referência para processamento de imagem e visão por computador. É open source e gratuita. 

Para além disso tem imensas funcionalidades básicas e avançadas.

Para instalar o OpenCV:

Ubuntu

https://docs.opencv.org/4.x/d2/de6/tutorial_py_setup_in_ubuntu.html

Windows

https://gist.github.com/demid5111/6faa590e4fc5813550dd95cc1c538893


Instalar também python, git, matplotlib, vscode, powershell e opencv.


O OpenCV tem vários tutorials que são uma ajuda valiosa para começar.

https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

# Exercícios 

## Exercício 1 - Representação de imagens digitais

Carregue a imagem **imagens/grey_lake.jpg**. Mostre-a usando as funcionalidades do opencv. 

Veja o tipo de dados da imagem e mostre uma versão quantizada da imagem para 64, 32, 16 e 8 níveis de cinzento.

## Exercício 2 - Alteração de Pixeis

Percorra todos os pixeis da imagem **imagens/chessboard.jpg** e, para cada um, altere o seu valor para metade com uma probabilidade de 50%.


## Exercício 3 - Indexação de píxeis

Utilize as ferramentas do numpy para criar uma imagem de 200x300 toda preta.
Coloque um rectângulo horizontal branco de 50 píxeis de largura no seu interior.

Adicione um quadrado cinzento de 25x25 píxeis de largura no canto inferior direito da imagem.

## Exercício 4 - Indexação por máscaras

Crie um círculo branco de 40 píxeis de raio no centro da imagem?

## Exercício 5 - Criação de vários círculos de raio variável

Crie uma imagem con 25 círculos de raio variável e em posições aleatórias.

## Exercício 6 - Histogramas

Visualize o histograma da imagem **imagens/grey_lake.jpg** e escolha o valor adequado para isolar as montanhas.

Use a biblioteca matplotlib.

## Exercício 7 - Binarização

Binarize a imagem **grey_lake** com diferentes níveis de binarização.
Procure algoritmos de cálculo automático do limite de binarização.

## Exercício 8 - Redimensionamento e mosaicos de imagens

Faça o redimensionamento da imagem **grey_lake** para 200x400, e crie um mosaico de 2x2 com quatro imagens iguais.
