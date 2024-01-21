fruit_string = "appel, banaan, watermeloen, sinaasappel, druif, kiwi, mango, ananas, perzik, aardbei"

fruit_list = fruit_string.split(", ")

print("fruitsoorten zijn:")
for fruit in fruit_list[:5]:
    print(fruit)
