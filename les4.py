#!/usr/bin/env python3

def main():
    tekst_object = "Dit is een tekst"
    cijfer_object = 1000
    lijst_object = [1, 2, 3, 4, 5]

    toon_informatie(tekst_object)
    toon_informatie(cijfer_object)
    toon_informatie(lijst_object)

    eigen_functie(tekst_object, cijfer_object, lijst_object)

def toon_informatie(obj):
    print(f"Type: {type(obj)}")
    print(f"ID: {id(obj)}")
    
    if isinstance(obj, (str, list)):
        print(f"Lengte: {len(obj)}")
    elif isinstance(obj, int):
        print("Dit is een cijfer.")
    
    print("\n")

def eigen_functie(obj1, obj2, obj3):
    print(f"Dit is een bericht van de eigen functie!")
    print(f"Object 1: {obj1}")
    print(f"Object 2: {obj2}")
    print(f"Object 3: {obj3}")

if __name__ == "__main__":
    main()
