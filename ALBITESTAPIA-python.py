def cantidadCifras(numero):
    cantidadCifras = 0
    while numero > 0:
        cantidadCifras = cantidadCifras + 1
        numero = int(numero/10)
    return cantidadCifras


def par(cifras):
    if cifras % 2 == 0:
        return True
    else:
        return False


def nuevoNumero(numero1, numero2):

    valor = numero1 * numero2
    obtenido = True
    CIFRAS = cantidadCifras(numero1)
    PAR = par(CIFRAS)
    if PAR:
        criterio = int(CIFRAS/2)
    else:
        criterio = int((CIFRAS+1)/2)

    condicion = 0
    numero3 = ""
    while obtenido:
        cifra = valor % 10
        valor = int(valor / 10)
        condicion = condicion + 1
        if condicion > criterio:
            numero3 = str(numero3)+""+str(cifra)
        if condicion == (criterio+CIFRAS):
            obtenido = False
    numero3 = numero3[::-1]
    return numero3


def main():
    print("######## ALGORITMO DE PRODUCTOS MEDIOS #########")
    semilla01 = int(
        input("INGRESE LA PRIMERA SEMILLA 1 : "))
    semilla02 = int(
        input("INGRESE LA PRIMERA SEMILLA 2 : "))
    cantidad = int(
        input("INGRESE LA CANTIDAD DE NUMEROS ALEATORIOS : "))

    if cantidadCifras(semilla01) > 3 and cantidadCifras(semilla02) > 3:

        for i in range(0, cantidad):

            if i == 0:
                print("Numero Aleatorio : 0.",
                      nuevoNumero(semilla01, semilla02))
            else:
                aux = semilla02
                semilla02 = int(nuevoNumero(semilla01, semilla02))
                semilla01 = aux
                print("Numero Aleatorio : 0.",
                      nuevoNumero(semilla01, semilla02))


if __name__ == "__main__":
    main()
