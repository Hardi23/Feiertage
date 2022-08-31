# Feiertage
Projekt zum Generieren der Feiertage in Deutschland und Österreich

## Verwendung
```python
from holiday_generator import generate_holidays
from holidays import HolidayBase

land: str = "DE"
bundesland: str = "BE"
jahr: int = 2022

holidays: list[HolidayBase] = generate_holidays(country=country, state_abbr=state, year=year)
```

Ländercodes:
 - Deutschland = "DE"
 - Österreich = "AT"
 
 Bundesländer Deutschland:
 ```python
 b_laender = {"BW": "BadenWuerttemberg",
             "BY": "Bayern",
             "BE": "Berlin",
             "BB": "Brandenburg",
             "HB": "Bremen",
             "HH": "Hamburg",
             "HE": "Hessen",
             "MV": "MecklenburgVorpommern",
             "NI": "Niedersachsen",
             "NW": "NordrheinWestfalen",
             "RP": "RheinlandPfalz",
             "SL": "Saarland",
             "SN": "Sachsen",
             "ST": "SachsenAnhalt",
             "SH": "SchleswigHolstein",
             "TH": "Thueringen",
             }
 ```
 
 Bundesländer Österreich:
 ```python
 b_laender_at = {"KTN": "Kaernten",
                "BGLD": "Burgenland",
                "NOE": "Niederoesterreich",
                "OOE": "Oberoesterreich",
                "SBG": "Salzburg",
                "STMK": "Steiermark",
                "T": "Tirol",
                "VBG": "Vorarlberg",
                "W": "Wien"
                }
 ```
 
