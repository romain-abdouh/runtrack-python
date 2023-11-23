def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60

    if heures == 0:
        print(f"{minutes} minutes")
    elif heures == 1 and minutes_restantes == 0:
        print("1 heure")
    elif heures == 1:
        print(f"1 heure et {minutes_restantes} minutes")
    elif minutes_restantes == 0:
        print(f"{heures} heures")
    else:
        print(f"{heures} heures et {minutes_restantes} minutes")


time_to_text(320)
time_to_text(65)
time_to_text(95)
