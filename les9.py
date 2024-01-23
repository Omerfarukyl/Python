def main():
    getal = int(input("Voer een getal in: "))

    if getal > 50:
        bestandsnaam = "boodschap.txt"
        boodschap = "Gefeliciteerd! Je getal is hoger dan 50."

        with open(bestandsnaam, "w") as bestand:
            bestand.write(boodschap)

        print(f"{boodschap}")
    else:
        print("Helaas niet geslaagd.")

if __name__ == "__main__":
    main()
