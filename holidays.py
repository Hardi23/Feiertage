import datetime


class HolidayBase:

    holiday_id: str
    name: str
    date: datetime.date
    year: int
    whole_state: bool

    def __init__(self, holiday_id: str, year: int, name: str, date: datetime.date, whole_state: bool):
        self.holiday_id = holiday_id
        self.name = name
        self.date = date
        self.year = year
        self.whole_state = whole_state

    def __str__(self):
        return f"HolidayBase(name={self.name}, id={self.holiday_id}," \
               f" date={self.date.isoformat()}, whole_state={self.whole_state})"


def Ostern(year: int = 2036, whole_state: bool = True) -> HolidayBase:
    k = year // 100
    m = 15 + (3 * k + 3) // 4 - (8 * k + 13) // 25
    s = 2 - (3 * k + 3) // 4
    a = year % 19
    d = (19 * a + m) % 30
    r = (d + a // 11) // 29
    og = 21 + d - r
    sz = 7 - (year + year // 4 + s) % 7
    oe = 7 - (og - sz) % 7
    os = og + oe

    day = os - 31 if os > 31 else os
    month = 4 if os > 31 else 3

    return HolidayBase(holiday_id="2a2091e0-bff2-448c-8481-80016f60cdc5",
                       year=year,
                       name="Ostersonntag",
                       date=datetime.datetime(year=year, month=int(month), day=int(day)).date(),
                       whole_state=whole_state)


def Karfreitag(year: int, whole_state: bool = True) -> HolidayBase:
    o = Ostern(year)
    return HolidayBase(year=year,
                       holiday_id="175dad3a-ffb2-4069-b08a-13e1796931b6",
                       name="Karfreitag", date=(o.date - datetime.timedelta(days=2)),
                       whole_state=whole_state)


def TagDerArbeit(year: int, whole_state: bool = True) -> HolidayBase:
    return HolidayBase(year=year,
                       holiday_id="d32d6cb3-3b7f-4ca4-8240-59228e63c958",
                       name="Tag der Arbeit", date=datetime.datetime(year=year, month=5, day=1).date(),
                       whole_state=whole_state)


def TagDerDeutschenEinheit(year: int, whole_state: bool = True) -> HolidayBase:
    return HolidayBase(year=year,
                       holiday_id="f91cecb5-3096-4675-95db-855ef17466b0",
                       name="Tag der Deutschen Einheit",
                       date=datetime.datetime(year=year, month=10, day=3).date(),
                       whole_state=whole_state)


def ErsterWeihnachtstag(year: int, whole_state: bool = True) -> HolidayBase:
    return HolidayBase(year=year,
                       holiday_id="004726c7-f08a-4d83-9ff1-969b57f017d7",
                       name="1. Weihnachtstag",
                       date=datetime.datetime(year=year, month=12, day=25).date(),
                       whole_state=whole_state)


def ZweiterWeihnachtstag(year: int, whole_state: bool = True) -> HolidayBase:
    return HolidayBase(year=year,
                       holiday_id="4b27857c-6c71-4be4-8bb6-ea314579ec9e",
                       name="2. Weihnachtstag",
                       date=datetime.datetime(year=year, month=12, day=26).date(),
                       whole_state=whole_state)


def Reformationstag(year: int, whole_state: bool = True) -> HolidayBase:
    return HolidayBase(year=year,
                       holiday_id="3116601c-64c3-44e2-b470-831bcb6234da",
                       name="Reformationstag", date=datetime.datetime(year=year, month=10, day=31).date(),
                       whole_state=whole_state)


def Neujahrstag(year: int, whole_state: bool = True) -> HolidayBase:
    return HolidayBase(year=year,
                       holiday_id="d3e1abbc-d328-4093-bbb4-0664fd5cbe7d",
                       name="Neujahrstag",
                       date=datetime.datetime(year=year, month=1, day=1).date(),
                       whole_state=whole_state)


def Ostermontag(year: int, whole_state: bool = True) -> HolidayBase:
    o = Ostern(year)
    return HolidayBase(year=year,
                       holiday_id="75a49216-c1f4-4c6f-9a01-61071ad28c90",
                       name="Ostermontag", date=(o.date + datetime.timedelta(days=1)),
                       whole_state=whole_state)


def ChristiHimmelfahrt(year: int, whole_state: bool = True) -> HolidayBase:
    o = Ostern(year)
    return HolidayBase(year=year,
                       holiday_id="563b1549-34fc-499c-9c12-d25842072bd6",
                       name="Christi Himmelfahrt", date=(o.date + datetime.timedelta(days=39)),
                       whole_state=whole_state)


def Pfingstmontag(year: int, whole_state: bool = True) -> HolidayBase:
    o = Ostern(year)
    return HolidayBase(year=year,
                       holiday_id="9ab7bd77-864a-4c64-a246-1fef1d954356",
                       name="Pfingstmontag", date=(o.date + datetime.timedelta(days=50)),
                       whole_state=whole_state)


def HeiligeDreiKoenige(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="ddfcf1e1-1a8e-4b81-8718-18d1b9f685cb",
                       name="Heilige Drei Könige", date=datetime.datetime(year=year, month=1, day=6).date(),
                       whole_state=whole_state)


def Fronleichnam(year: int, whole_state: bool = True):
    o = Ostern(year)
    return HolidayBase(year=year,
                       holiday_id="01812318-022e-4d63-82a1-ae6a46d79d72",
                       name="Fronleichnam", date=(o.date + datetime.timedelta(days=60)),
                       whole_state=whole_state)


def Allerheiligen(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="41965d49-a234-4d92-8a0e-99dad8d899f8",
                       name="Allerheiligen", date=datetime.datetime(year=year, month=11, day=1).date(),
                       whole_state=whole_state)


def AugsburgerFriedensfest(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="b7e3efe5-b953-419b-8281-bb2a7fa96ad3",
                       name="Augsburger Friedensfest",
                       date=datetime.datetime(year=year, month=8, day=8).date(),
                       whole_state=whole_state)


def Pfingsten(year: int, whole_state: bool = True):
    o = Ostern(year)
    return HolidayBase(year=year,
                       holiday_id="ae1beb50-b799-4d53-9c33-4bc542634f77",
                       name="Pfingstsonntag",
                       date=o.date + datetime.timedelta(days=49),
                       whole_state=whole_state)


def BussUndBettag(year: int, whole_state: bool = True):
    o = datetime.datetime(year=year, month=11, day=22).date()
    d = (4 + (int(o.weekday()) + 1)) % 7
    return HolidayBase(year=year,
                       holiday_id="e36edbd9-fce1-4e44-a8cd-3d212becd754",
                       name="Buß- und Bettag",
                       date=o + datetime.timedelta(days=d * -1),
                       whole_state=whole_state)


def Gruendonnerstag(year: int, whole_state: bool = True):
    o = Ostern(year)
    return HolidayBase(year=year,
                       holiday_id="144e229a-6144-4b3b-9f0f-2c947d6f5f45",
                       name="Gründonnerstag",
                       date=o.date - datetime.timedelta(days=3),
                       whole_state=whole_state)


def MariaeHimmelfahrt(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="ea3a2777-31ec-4ebe-be93-9edc48e276cd",
                       name="Mariä Himmelfahrt",
                       date=datetime.datetime(year=year, month=8, day=15).date(),
                       whole_state=whole_state)


def Frauentag(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="1365f874-9a75-49fb-b6ca-14f0717c945e",
                       name="Frauentag",
                       date=datetime.datetime(year=year, month=3, day=8).date(),
                       whole_state=whole_state)


def TagDerBefreiung(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="c1749e93-e307-4b94-bd8a-1eed3a6f3057",
                       name="Tag der Befreiung",
                       date=datetime.datetime(year=year, month=5, day=8).date(),
                       whole_state=whole_state)


def Weltkindertag(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="e26b7478-918b-41b7-9f0c-b845fabbed2c",
                       name="Weltkindertag",
                       date=datetime.datetime(year=year, month=9, day=20).date(),
                       whole_state=whole_state)


def Staatsfeiertag(year: int, whole_state: bool = True):
    d = TagDerArbeit(year)
    d.name = "Staatsfeiertag"
    d.holiday_id = "1adb699a-b9a0-477e-bc8b-9743ba32d10a"
    return d


def Nationalfeiertag(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="154657b4-477d-4a09-8049-ad5856ecf06d",
                       name="Nationalfeiertag",
                       date=datetime.datetime(year=year, month=10, day=26).date(),
                       whole_state=whole_state)


def MariaeEmpfaengnis(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="0c1359ce-8078-4b74-b4f6-9a2db0174f08",
                       name="Mariä Empfängnis",
                       date=datetime.datetime(year=year, month=12, day=8).date(),
                       whole_state=whole_state)


def Christtag(year: int, whole_state: bool = True):
    d = ErsterWeihnachtstag(year)
    d.name = "Christtag"
    d.holiday_id = "f34b9f52-5d4a-4521-87fd-9ee7f508be47"
    return d


def Stefanitag(year: int, whole_state: bool = True):
    d = ZweiterWeihnachtstag(year)
    d.name = "Setfanitag"
    d.holiday_id = "44da499d-7318-430a-992d-c6af9a1de042"
    return d


def Josefitag(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="26d1e43c-c2a6-4412-a175-366782090a7e",
                       name="Josefitag",
                       date=datetime.datetime(year=year, month=3, day=19).date(),
                       whole_state=whole_state)


def TagDerVolksabstimmung(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="1ed1f27a-098d-459d-aa6a-6833643313ef",
                       name="Tag der Volksabstimmung",
                       date=datetime.datetime(year=year, month=10, day=10).date(),
                       whole_state=whole_state)


def Martinstag(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="79a7c808-7976-4b1b-a30d-fa02e1d492f5",
                       name="Martinstag",
                       date=datetime.datetime(year=year, month=11, day=11).date(),
                       whole_state=whole_state)


def Leopolditag(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="9ef9dcdb-9bdf-465c-b6da-e15aa89b4d9d",
                       name="Leopolditag",
                       date=datetime.datetime(year=year, month=11, day=15).date(),
                       whole_state=whole_state)


def Florianitag(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="6b9242ce-a76e-4815-a53d-6df6217b4405",
                       name="Florianitag",
                       date=datetime.datetime(year=year, month=5, day=4).date(),
                       whole_state=whole_state)


def Rupertitag(year: int, whole_state: bool = True):
    return HolidayBase(year=year,
                       holiday_id="b58010f8-6afd-46fd-9560-d319a4e259db",
                       name="Rupertitag",
                       date=datetime.datetime(year=year, month=9, day=24).date(),
                       whole_state=whole_state)
