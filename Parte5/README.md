# MicroVisaoArtificial_24-25

# Parte 1


Miguel Riem Oliveira <mriem@ua.pt>

# Sumário

 - Imagens de côr
 - Segmentação de côr
 - Modelos RGB e HSV

# Exercícios 


## Exercício 1 - Cores puras

Crie uma imagem RGB toda preta, e depois acrescente-lhe um circulo de cor vermelho puro ([cv2.Circle](https://www.geeksforgeeks.org/python-opencv-cv2-circle-method/)), e um rectângulo de côr verde puro ([cv2.rectangle](https://www.geeksforgeeks.org/python-opencv-cv2-rectangle-method/?ref=lbp)).

## Exercício 2 - Combinações de cores puras

Adicione um circulo amarelo puro à imagem do círculo anterior.

## Exercício 3 - Cubo RGB

Com recurso à função **scatter3D** do matplotlib desenhe uma representação gráfica do cubo RGB para a imagem.

Experimente com a imagem **lake.jpg** e com a imagem **fruits3.png**. Que diferenças nota?


## Exercício 4 - Segmentação de cor em RGB

Carregue a imagem **imagens/castle.png** e faça o display da mesma.
Faça a segmentação da cor vermelha no espaço RGB na imagem e mostre a máscara segmentada.

Mostre também uma imagem alterada em que a fachada vermelha está mais destacada do resto da imagem (com mais intensidade).

## Exercício 5 - Segmentação de cor em HSV

Carregue a imagem **imagens/castle.png** e faça o display da mesma.
Faça a segmentação da cor vermelha no espaço RGB na imagem e mostre a máscara segmentada.

Mostre também uma imagem alterada em que a fachada vermelha está mais destacada do resto da imagem (com mais intensidade).


## Exercício 6 - Histogramas de imagens RGB

Crie um novo script que permita visualizar o histograma de cada componente de cor de uma imagem RGB, bem como o histograma da imagem em nível de cinza correspondente. Use a função **split** para obter as imagens de intensidade para cada um dos componentes de cor. Visualize as imagens resultantes e os respectivos histogramas.

## Exercício 7 - Anotação da cor em zonas da imagem

Crie uma ferramenta que permita desenhar um rectângulo na imagem indicando que os píxeis do seu interior pertencem a uma cor. O programa deve perguntar o nome da cor após a seleção do rectângulo.

Guarde num dicionário python informação estatística sobre a cor dos píxeis selecionados: mínimo, máximo, média e desvio padrão de cada canal de cor.
