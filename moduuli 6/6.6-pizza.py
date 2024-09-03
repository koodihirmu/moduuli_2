import math


def pizza() -> tuple:
    pizza_halkaisija = float(input("Pizzan halkaisija sentteinä: "))
    pizza_hinta = float(input("Pizzan hinta: "))

    pizza_ala = math.pi * pow((pizza_halkaisija/2), 2)
    yksikkohinta = pizza_hinta / pizza_ala

    return (pizza_ala, yksikkohinta)


def vertaa(pizza_1: tuple, pizza_2: tuple) -> str:
    if pizza_1[1] < pizza_2[1]:
        return f"Pizza 1 on parempi diili."
    elif pizza_1[1] == pizza_2[1]:
        return "Pizzat ovat saman hintaiset."
    else:
        return f"Pizza 2 on parempi diili."


def main() -> None:
    pizza_1 = pizza()
    pizza_2 = pizza()
    print(vertaa(pizza_1, pizza_2))


if __name__ == "__main__":
    main()
