
def main():
    kuha = int(input("Anna kuhan mitta: "))
    if kuha < 37:
        print(f"Palauta kala järveen mitasta puuttuu: {37 - kuha}")
    else:
        print(f"Hienoa kuha on täysimittainen, kuhan mitta: {kuha}")

if __name__ == "__main__":
    main()