# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

def main():
    sum = 0
    # ota kaikki inputit ja käännä ne suoraan grammoiksi
    u_input = float(input("Anna leiviskät.\n"))
    sum += u_input * 20 * 32 * 13.3

    u_input = float(input("Anna naulat.\n"))
    sum += u_input * 32 * 13.3

    u_input = float(input("Anna luodit.\n"))
    sum += u_input * 13.3

    print(f"Massa nykymittojen mukaan:")
    print(f"{int(sum / 1000)} kilogrammaa ja \
          {round(sum % 1000, 2)} grammaa")

    
if __name__ == "__main__":
    main()