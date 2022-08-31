from holiday_generator import generate_holidays
from holidays import HolidayBase

if __name__ == "__main__":
    country = input("Land (DE/AT): ")
    state = input("Bundesland: ")
    year = input("Jahr: ")
    holidays: list[HolidayBase] = generate_holidays(country=country, state_abbr=state, year=int(year))
    for holiday in holidays:
        print(holiday)
