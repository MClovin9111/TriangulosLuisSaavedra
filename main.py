#  VERIFICADOR DE TRIÁNGULOS

def es_triangulo(a: float, b: float, c: float) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a)


def clasificar_triangulo(a: float, b: float, c: float) -> str:
    if a == b == c:
        return "EQUILATERO"
    elif a == b or b == c or a == c:
        return "ISOSCELES"
    else:
        return "ESCALENO"


def pedir_lado(nombre: str) -> float:
    while True:
        try:
            valor = float(input(f"INGRESE EL LADO {nombre} DEL TRIANGULO: "))
            if valor <= 0:
                print("El lado debe ser un número positivo. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Escriba un número, por favor.")


def main() -> None:
    print("╔══════════════════════════════════════════════╗")
    print("║        VERIFICADOR  DE  TRIÁNGULOS           ║")
    print("╚══════════════════════════════════════════════╝\n")

    while True:
        # 1. Pedir lados
        lado_a = pedir_lado("A")
        lado_b = pedir_lado("B")
        lado_c = pedir_lado("C")

        # 2. Verificar validez
        if not es_triangulo(lado_a, lado_b, lado_c):
            print("\nLos valores ingresados NO forman un triángulo válido.\n")
        else:
            tipo = clasificar_triangulo(lado_a, lado_b, lado_c)
            print(f"\nEL TRIANGULO ES {tipo}\n")

        # 3. Preguntar si se desea continuar
        otra = input("¿Desea verificar otro triángulo? (S / N): ").strip().lower()
        if otra != "s":
            print("\nPrograma finalizado. ¡Hasta luego!")
            break
        print()


if __name__ == "__main__":
    main()
