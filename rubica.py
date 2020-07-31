def saludo():
    print("""BIENVENIDO A LA TABLA RUBICA""")


def rubica():
    numero = float(input("¿Que puntaje desea calcular?\n"))
    base = int(input("¿En base a?\n"))
    resultado = numero/base * 4 + 1
    resultado = (round(resultado, 1))
    print(f'El puntaje de ' + str(numero) +
          '\nSu calificacion es = ' + str(resultado))


if __name__ == "__main__":
    saludo()
    rubica()
