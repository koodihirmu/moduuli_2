
def main():
    hyttiluokat = {"LUX" : "LUX on parvekkeellinen hytti yläkannella.", 
                   "A" : "A on ikkunallinen hytti autokannen yläpuolella", 
                   "B" : "B on ikkunaton hytti autokannen yläpuolella", 
                   "C" : "C on ikkunaton hytti autokannen alapuolella"}

    u_input = input("Anna hyttiluokka: ")

    try:
        print(hyttiluokat[u_input.upper()])
    except:
        print("Virheellinen hyttiluokka.")

if __name__ == "__main__":
    main()