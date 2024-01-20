weekmenu = {
    'maandag': 'Kebab',
    'dinsdag': 'Erwtensoep',
    'woensdag': 'Vegetarische lasagne',
    'donderdag': 'Spruitjes',
    'vrijdag': 'Boerenkool',
    'zaterdag': 'Hamburgers',
    'zondag': 'Kapsalon'
}

gekozen_dag = input("Schrijf hieronder een dag. En ontdek dan wat het gerecht van de dag is:").lower()

if gekozen_dag in weekmenu:
    gerecht = weekmenu[gekozen_dag]
    print(f"Op {gekozen_dag.capitalize()} staat op het menu: {gerecht}")
else:
    print("Ongeldige dag. Controleer je spelling en probeer opnieuw.")
