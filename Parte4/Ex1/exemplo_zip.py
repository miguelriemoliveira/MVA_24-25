import sys
from copy import deepcopy

import cv2
import numpy as np


def main():

    alturas = [1.75, 1.60, 1.80, 1.80, 1.72]
    pesos = [75, 50, 75, 95, 80]

    for altura in alturas:
        print('altura = ' + str(altura))

    for peso in pesos:
        print('peso = ' + str(peso))

    # IMC = peso / altura**2
    for i in range(0, len(alturas)):
        peso = pesos[i]
        altura = alturas[i]
        imc = peso / altura**2
        print('imc = ' + str(imc))

    for altura, peso in zip(alturas, pesos):
        imc = peso / altura**2
        print('imc = ' + str(imc))


if __name__ == "__main__":
    main()
