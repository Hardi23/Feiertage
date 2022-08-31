from holiday_generator import generate_holidays

if __name__ == "__main__":
    country = input("Land (DE/AT): ")
    state = input("Bundesland: ")
    year = input("Jahr: ")
    for holiday in generate_holidays(country=country, state_abbr=state, year=int(year)):
        print(holiday.__str__())
