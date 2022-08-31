from holidays import Ostern, Karfreitag, TagDerArbeit, TagDerDeutschenEinheit, ErsterWeihnachtstag, \
    ZweiterWeihnachtstag, Reformationstag, Neujahrstag, Ostermontag, ChristiHimmelfahrt, Pfingstmontag, \
    HeiligeDreiKoenige, Fronleichnam, Allerheiligen, AugsburgerFriedensfest, Pfingsten, BussUndBettag, \
    Gruendonnerstag, MariaeHimmelfahrt, Frauentag, TagDerBefreiung, Weltkindertag, Staatsfeiertag, Nationalfeiertag, \
    MariaeEmpfaengnis, Christtag, Stefanitag, Josefitag, TagDerVolksabstimmung, Martinstag, Leopolditag, Florianitag, \
    Rupertitag, HolidayBase

COUNTRY_DE = "DE"
COUNTRY_AT = "AT"


def generate_holidays(country: str, state_abbr: str, year: int):
    holidays = create_holiday_list(year, country, state_abbr)
    return holidays


def generate_german_holidays(year) -> list[HolidayBase]:
    unique_german = [
        Karfreitag(year),
        TagDerArbeit(year),
        TagDerDeutschenEinheit(year),
        ErsterWeihnachtstag(year),
        ZweiterWeihnachtstag(year)
    ]
    if year == 2017:
        unique_german.append(Reformationstag(year))
    return unique_german


def generate_austrian_holidays(year: int) -> list[HolidayBase]:
    list_austrian_holidays: list[HolidayBase] = [
        HeiligeDreiKoenige(year),
        Staatsfeiertag(year),
        Fronleichnam(year),
        MariaeHimmelfahrt(year),
        Nationalfeiertag(year),
        Allerheiligen(year),
        MariaeEmpfaengnis(year),
        Christtag(year),
        Stefanitag(year)
    ]
    return list_austrian_holidays


def create_common_holiday_list(year) -> list[HolidayBase]:
    return [
        Neujahrstag(year),
        Ostermontag(year),
        ChristiHimmelfahrt(year),
        Pfingstmontag(year)
    ]


def Bayern(year: int) -> list[HolidayBase]:
    return [
        HeiligeDreiKoenige(year),
        Fronleichnam(year),
        Allerheiligen(year),
        AugsburgerFriedensfest(year, False),
        BussUndBettag(year, False),
        MariaeHimmelfahrt(year, False),
    ]


def BadenWuerttemberg(year: int) -> list[HolidayBase]:
    result = [
        HeiligeDreiKoenige(year),
        Fronleichnam(year),
        Allerheiligen(year),
        Gruendonnerstag(year, False),
    ]

    if year != 2017:
        result.append(Reformationstag(year, False))

    return result


def Berlin(year: int) -> list[HolidayBase]:
    result: list[HolidayBase] = []
    if year >= 2019:
        result.append(Frauentag(year))
    if year == 2020:
        result.append(TagDerBefreiung(year))
    return result


def Brandenburg(year: int) -> list[HolidayBase]:
    result: list[HolidayBase] = [
        Ostern(year),
        Pfingsten(year),
    ]
    if year >= 1990 and year != 2017:
        result.append(Reformationstag(year))
    return result


def Bremen(year: int) -> list[HolidayBase]:
    result: list[HolidayBase] = []
    if year >= 2018:
        result.append(Reformationstag(year))
    return result


def Hamburg(year: int) -> list[HolidayBase]:
    result: list[HolidayBase] = []
    if year >= 2018:
        result.append(Reformationstag(year))
    return result


def Hessen(year: int) -> list[HolidayBase]:
    return [
        Fronleichnam(year)
    ]


def MecklenburgVorpommern(year: int) -> list[HolidayBase]:
    return [Reformationstag(year)] if year >= 1990 and year != 2017 else []


def Niedersachsen(year: int) -> list[HolidayBase]:
    if year >= 2018:
        return [
            Reformationstag(year)
        ]
    return []


def NordrheinWestfalen(year: int) -> list[HolidayBase]:
    return [
        Fronleichnam(year),
        Allerheiligen(year),
    ]


def RheinlandPfalz(year: int) -> list[HolidayBase]:
    return [
        Fronleichnam(year),
        Allerheiligen(year),
    ]


def Saarland(year: int) -> list[HolidayBase]:
    return [
        Fronleichnam(year),
        MariaeHimmelfahrt(year),
        Allerheiligen(year),
    ]


def Sachsen(year: int) -> list[HolidayBase]:
    result = [
                Fronleichnam(year, False),
                BussUndBettag(year)
            ]
    if year >= 1990 and year != 2017:
        result.append(Reformationstag(year), )

    return result


def SachsenAnhalt(year: int) -> list[HolidayBase]:
    result = [
        HeiligeDreiKoenige(year),
    ]
    if year >= 1990 and year != 2017:
        result.append(Reformationstag(year))
    return result


def SchleswigHolstein(year: int) -> list[HolidayBase]:
    if year >= 2018:
        return [
            Reformationstag(year)
        ]
    return []


def Thueringen(year: int) -> list[HolidayBase]:
    result = [
        Fronleichnam(year, False),
    ]
    if year >= 1990 and year != 2017:
        result.append(Reformationstag(year))
    if year >= 2019:
        result.append(Weltkindertag(year))
    return result


def generate_state_holidays_de(year: int, state_abbr: str):
    if state_abbr == "BW":
        return BadenWuerttemberg(year)
    elif state_abbr == "BY":
        return Bayern(year)
    elif state_abbr == "BE":
        return Berlin(year)
    elif state_abbr == "BB":
        return Brandenburg(year)
    elif state_abbr == "HB":
        return Bremen(year)
    elif state_abbr == "HH":
        return Hamburg(year)
    elif state_abbr == "HE":
        return Hessen(year)
    elif state_abbr == "MV":
        return MecklenburgVorpommern(year)
    elif state_abbr == "NI":
        return Niedersachsen(year)
    elif state_abbr == "NW":
        return NordrheinWestfalen(year)
    elif state_abbr == "RP":
        return RheinlandPfalz(year)
    elif state_abbr == "SL":
        return Saarland(year)
    elif state_abbr == "SN":
        return Sachsen(year)
    elif state_abbr == "ST":
        return SachsenAnhalt(year)
    elif state_abbr == "SH":
        return SchleswigHolstein(year)
    elif state_abbr == "TH":
        return Thueringen(year)
    else:
        return []


def Kaernten(year: int) -> list[HolidayBase]:
    return [
        Josefitag(year, False),
        TagDerVolksabstimmung(year),
    ]


def Burgenland(year: int) -> list[HolidayBase]:
    return [
        Martinstag(year),
    ]


def Niederoesterreich(year: int) -> list[HolidayBase]:
    return [
        Leopolditag(year),
    ]


def Oberoesterreich(year: int) -> list[HolidayBase]:
    return [
        Florianitag(year, False),
    ]


def Salzburg(year: int) -> list[HolidayBase]:
    return [
        Rupertitag(year),
    ]


def Steiermark(year: int) -> list[HolidayBase]:
    return [
        Josefitag(year, False),
    ]


def Tirol(year: int) -> list[HolidayBase]:
    return [
        Josefitag(year, False),
    ]


def Vorarlberg(year: int) -> list[HolidayBase]:
    return [
        Josefitag(year, False),
    ]


def Wien(year: int) -> list[HolidayBase]:
    return [
        Leopolditag(year),
    ]


def generate_state_holidays_at(year: int, state_abbr: str):
    if state_abbr == "KTN":
        return Kaernten(year)
    elif state_abbr == "BGLD":
        return Burgenland(year)
    elif state_abbr == "NOE":
        return Niederoesterreich(year)
    elif state_abbr == "OOE":
        return Oberoesterreich(year)
    elif state_abbr == "SBG":
        return Salzburg(year)
    elif state_abbr == "STMK":
        return Steiermark(year)
    elif state_abbr == "T":
        return Tirol(year)
    elif state_abbr == "VBG":
        return Vorarlberg(year)
    elif state_abbr == "W":
        return Wien(year)


def create_holiday_list(year: int, country: str, state_abbr: str):
    generated_holidays: list[HolidayBase] = create_common_holiday_list(year)
    if country == COUNTRY_DE:
        generated_holidays += generate_german_holidays(year)
        if state_abbr:
            generated_holidays += generate_state_holidays_de(year, state_abbr.upper())
    elif country == COUNTRY_AT:
        generated_holidays += generate_austrian_holidays(year)
        if state_abbr:
            generated_holidays += generate_state_holidays_at(year, state_abbr.upper())
    return generated_holidays
