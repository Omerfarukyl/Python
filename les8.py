class CursistenRegister:
    def __init__(self, voornaam, achternaam, adres, email):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.adres = adres
        self.email = email

    def welkomstbericht(self):
        bericht = f"Welkom {self.voornaam} {self.achternaam}. Uw boekenpakket is verstuurd naar {self.adres}." \
                  f" U krijgt hiervan een bevestiging op het door u opgegeven e-mailadres: {self.email}."
        return bericht

voornaam = "Tom"
achternaam = "Tomassen"
adres = "Giraffestraat 4 in Amsterdam"
email = "tom@python123.nl"

cursist = CursistenRegister(voornaam, achternaam, adres, email)

print(cursist.welkomstbericht())
