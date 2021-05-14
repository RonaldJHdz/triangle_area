def triangle_operation(triangle_base, triangle_height):
    triangle_area = (triangle_base * triangle_height) / 2
    print("El area del triangulo es de: {0}\n".format(str(triangle_area)))


def triangle_side_op(side1, side2, side3):
    if side1 == side2 and side2 == side3:
        print("El triangulo segun sus lados es Equilatero")
    elif side1 == side2 or side2 == side3:
        print("El triangulo segun sus lados es Isosceles")
    else:
        print("El triangulo segun sus lados es Escaleno")


def run():
    print("Reto 1 de Datacademy semana 1: Calcular el area de un triangulo\n")
    triangle_input_area = int(input("Escribe la base del triangulo: "))
    triangle_input_height = int(input("Escribe la altura del triangulo: "))

    triangle_operation(triangle_input_area, triangle_input_height)

    triangle_input_side = str(input("Deseas calcular el tipo de triangulo segun sus lados? (y/n): ")).lower()

    if triangle_input_side == "y":
        triangle_side1 = input("Ingresa el lado del triangulo 1: ")
        triangle_side2 = input("Ingresa el lado del triangulo 2: ")
        triangle_side3 = input("Ingresa el lado del triangulo 3: ")

        triangle_side_op(triangle_side1, triangle_side2, triangle_side3)
    elif triangle_input_side == "n":
        print("Gracias por usar este programa.")
    else:
        print("Selecciona una opcion valida!")


if __name__ == '__main__':
    run()
