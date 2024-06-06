# MicroVisaoArtificial_24-25

# Parte 3


Miguel Riem Oliveira <mriem@ua.pt>

# Sumário

 - Equalização de histogramas
 - Deteção de arestas

## Exercício 1 - Dilatação

Quando aplicada a imagens binárias, a operação de dilatação morfológica expande os limites das regiões de primeiro plano. Dada a imagem em nível de cinza **wdg2.bmp**, crie um novo programa realizando a seguinte sequência de operações:

1. Conversão para imagem binária, com limite 120.
2. Inversão da imagem resultante (ou seja, obtenção da imagem negativa).
3. Dilatação da imagem negativa utilizando elemento estruturante circular, com diâmetro de 11 pixels.

O que acontece se você aplicar repetidamente a operação de dilatação usando o mesmo elemento estruturante?

## Exercício 2 - Erosão

Quando aplicada a imagens binárias, a operação de erosão morfológica essencialmente reduz os limites das regiões de primeiro plano. Dada a imagem em nível de cinza **wdg2.bmp**, execute a seguinte sequência de operações:

1. Conversão para imagem binária, com limite 120.
2. Inversão da imagem resultante (ou seja, obtenção da imagem negativa).
3. Erosão da imagem negativa utilizando elemento estruturante quadrado, com largura de 11 pixels.

O que acontece se você aplicar repetidamente a operação de erosão usando o mesmo elemento estruturante? 

## Exercício 3 - Segmentação

Uma erosão morfológica pode ser o primeiro passo antes de segmentar regiões contíguas da imagem.

Dada a imagem em nível de cinza **mon1.bmp**, execute a seguinte sequência de operações:

1. Conversão para imagem binária, com limite 90.
2. Inversão da imagem resultante (ou seja, obtenção da imagem negativa).
3. Erosão repetida (duas vezes) da imagem resultante utilizando um elemento estruturante quadrado, com diâmetro de 11 pixels.

O que acontece se você usar um elemento estruturante quadrado de tamanho 5×5?


## Exercício 4 - Abertura Morfológica

A operação de abertura morfológica corresponde à aplicação de uma operação de erosão seguida de uma operação de dilatação, utilizando o mesmo elemento estruturante.

Dada a imagem binária **art3.bmp**, queremos contar as regiões circulares. Realizar uma abertura morfológica utilizando um elemento estruturante circular, com diâmetro de 11 pixels.

Dada a imagem binária art2.bmp, queremos segmentar separadamente os segmentos de linha vertical e horizontal. Realizar uma abertura morfológica utilizando um elemento estruturante retangular de tamanho 3×9, e utilizando um elemento estruturante retangular de tamanho 9×3. O que acontece?

## Exercício 5 - Fechamento Morfológico

A operação de fecho morfológico corresponde à aplicação de uma operação de dilatação seguida de uma operação de erosão, utilizando o mesmo elemento estruturante.

Dada a imagem binária **art4.bmp**, queremos remover as regiões circulares de tamanho menor. Realize um fechamento morfológico utilizando um elemento estruturante circular, com diâmetro de 22 pixels. Utilize elementos estruturantes de diâmetro menor e maior. Analise as imagens resultantes.

## Exercício 6 - Segmentação de regiões usando Flood-Filling

Crie um novo exemplo que permite segmentar regiões de uma determinada imagem.

Começando a partir de um pixel inicial, a função FloodFill segmenta uma região espalhando o valor inicial para pixels vizinhos com (aproximadamente) o mesmo valor de intensidade.

Use a função

    retval, rect = cv2.floodFill(imagem, máscara, seedPoint, newVal[, loDiff[, upDiff[, flags]]])

Segmente a imagem lena.jpg, utilizando como seed o pixel (430, 30) e permitindo variações de intensidade de ±5 em relação ao valor de intensidade do pixel seed.

## Exercício 7 - Flood-filling interativo

Permita que o usuário selecione interativamente o pixel inicial para segmentação de região. Teste a segmentação de região interativa usando as imagens **wdg2.bmp**, **tools_2.png** e **lena.jpg**.



