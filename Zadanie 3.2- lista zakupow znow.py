print("Lista zakupów")
sklepy={}
sklepy["piekarnia"]=['chleb','pączek','bułki']
sklepy["warzywniak"]=['marchew','seler','rukola']

for sklep, produkty in sklepy.items():
    print(f"Idę do {sklep.capitalize()}, kupuję tam {produkty}.")