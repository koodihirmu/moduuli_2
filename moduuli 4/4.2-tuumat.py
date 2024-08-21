def main():
    while True:
        u_input = float(input("Muunna tuumat senttimetreiksi: "))
        if u_input < 0:
            break
        print(f"{u_input}\" sentteinä on: {u_input*2.54} cm")

if __name__ == "__main__":
    main()