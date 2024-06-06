# MicroVisaoArtificial_24-25

# Parte 2


Miguel Riem Oliveira <mriem@ua.pt>

# Sumário

 - Modelos de cor
 - Segmentação de cor

## Exercício 1 - Ruído

Carregue a imagem **imagens/parrot.png** e adicione ruido do tipo "salt & pepper" com uma probabilidade de 20%.

## Exercício 2 - Filtro de média

Proceda à suavização da imagem anterior com um filtro de média.

## Exercício 3 - Filtro de Gaussiano

Proceda à suavização da imagem anterior com um filtro Gaussiano, e compare com o anterior.

## Exercício 4 - Filtro de Mediana

Proceda à suavização da imagem anterior com um filtro de Mediana, e compare com os anteriores.

## Exercício 5 - Filtro de pontos isolados

Crie um filtro de pontos isolados, fazendo a convolução diretamente com ciclos for para percorrer linhas e colunas.

## Exercício 6 - Deteção de arestas

Faça a deteção de arestas na imagem **imagens/castle_grey.png**. 

## Exercício 7 - Deteção de contornos

Crie uma imagem de 500x500 e coloque um rectângulo vertical de 70x40 píxeis no meio.
Utilize as ferramentas do Opencv para detetar os contornos do rectângulo.

## Exercício 8 - Aumento de contraste

Carregue a imagem **images/ireland-06-01.tif** e faça uma operação Contrast-Stretching. Deverão ser visualizadas a imagem original e a imagem resultante, bem como os respectivos histogramas. Para conseguir isso:

Use a função minMaxLoc para determinar os menores e maiores valores de intensidade da imagem.

Crie uma nova imagem que utilize toda a faixa de valores de intensidade (de 0 a 255). Para cada pixel da imagem, a intensidade do pixel correspondente na imagem resultante é dada por:

$ final(x,y) = {original(x,y)-min \over max-min} \times 255 $

Aplique a operação Contrast-Stretching às imagens predio.bmp e pouco_contraste.png. Visualize os histogramas das diferentes imagens. Que diferenças você percebe?

## Exercício 9 - Equalização de histogramas

Realize uma operação de equalização do histograma utilizando a função equalizeHist. Deverão ser visualizadas a imagem original e a imagem resultante, bem como os respectivos histogramas. Aplique a operação Histograma-Equalização à imagem TAC_PULMAO.bmp. Qual é a diferença entre os histogramas da imagem original e a imagem equalizada? O que a operação Histograma-Equalização permite?

