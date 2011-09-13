#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# 

CTCSS = 88.8
playCTCSS = False
CTCSSVolume = 0.1
serialPort     = '/dev/ttyS0'
serialBaudRate = 9600

from lib.cw import *

lang = "pl_google"

pygameBug = 1

helloMsg = ["tu_eksperymentalna_automatyczna_stacja_pogodowa",\
    "sp6yre",]#"lokator","jo81ld"]
goodbyeMsg = ["_","tu_sp6yre",]

modules = ["y_weather", "meteoalarm", "imgw_podest"]

class m:
    pass

y_weather = m()
y_weather.zipcode = 526363
# it would be nice to give one ability to parse it via template engine
# http://wiki.python.org/moin/Templating
y_weather.template = """stan_pogody_z_dnia {PUB_DATE_HOUR} _ temperatura 
    {CURR_TEMP} wilgotnosc {HUMIDITY} 
    {CURRENT_CONDITION} _ kierunek_wiatru {WIND_DIR_NEWS} 
    {WIN_DIR_DEG} predkosc_wiatru {WIND_SPEED} _
    cisnienie {PRESSURE} {PRESSURE_TENDENTION}
    temperatura_odczuwalna {TEMP_WIND_CHILL} _
    
    prognoza_na_nastepne piec godzin 
    {FORECAST0_CONDITION} temperatura_minimalna
    {FORECAST0_MIN_TEMP_SHORT} maksymalna {FORECAST0_MAX_TEMP} 
    
    _ nastepnie {FORECAST1_CONDITION} temperatura_minimalna
    {FORECAST1_MIN_TEMP_SHORT} maksymalna {FORECAST1_MAX_TEMP} _
    """


debug = m()
debug.writeLevel = None
debug.showLevel  = 0

# ----------
# meteoalarm
# ----------
meteoalarm = m()

# There are three things you should configure in meteoalarm module:
# region number, if module should show meteo awareness for today and
# and if it should show awareness for tommorow.
#
# Here is the list of region codes for Poland. You can find region
# numbers for other countries on www.meteoalarm.eu .
#
# PL011: Łódzkie                PL007: Śląskie
# PL010: Świętokrzyskie         PL005: Dolnośląskie 
# PL013: Kujawsko-pomorskie     PL015: Lubelskie
# PL002: Lubuskie               PL008: Małopolskie 
# PL001: Mazowieckie            PL007: Opolskie
# PL009: Podkarpackie           PL016: Podlaskie
# PL004: Pomorskie              PL014: Warmińsko-mazurskie 
# PL012: Wielkopolskie          PL003: Zachodniopomorskie 

meteoalarm.region = 'PL005'
meteoalarm.showToday = 1
meteoalarm.showTomorrow = 1

imgw_podest = m()

imgw_podest.wodowskazy = [
'3.149180010',   # Nazwa: Krzyżanowice, rzeka: Odra
'3.149180020',   # Nazwa: Chałupki, rzeka: Odra
'3.149180030',   # Nazwa: Łaziska, rzeka: Olza
'3.149180060',   # Nazwa: Cieszyn, rzeka: Olza
'3.149180070',   # Nazwa: Cieszyn, rzeka: Olza-Młynówka
'3.149180130',   # Nazwa: Istebna, rzeka: Olza
'3.149180300',   # Nazwa: Olza, rzeka: Odra
'3.150150010',   # Nazwa: Mirsk, rzeka: Kwisa
'3.150150020',   # Nazwa: Mirsk, rzeka: Czarny Potok
'3.150150030',   # Nazwa: Jakuszyce, rzeka: Kamienna
'3.150150040',   # Nazwa: Barcinek, rzeka: Kamienica
'3.150150050',   # Nazwa: Piechowice, rzeka: Kamienna
'3.150150060',   # Nazwa: Pilchowice, rzeka: Bóbr
'3.150150070',   # Nazwa: Jelenia Góra, rzeka: Kamienna
'3.150150080',   # Nazwa: Jelenia Góra, rzeka: Bóbr
'3.150150090',   # Nazwa: Łomnica, rzeka: Łomnica
'3.150150100',   # Nazwa: Wojanów, rzeka: Bóbr
'3.150150110',   # Nazwa: Kowary, rzeka: Jedlica
'3.150150120',   # Nazwa: Bukówka, rzeka: Bóbr
'3.150150130',   # Nazwa: Błażkowa, rzeka: Bóbr
'3.150150190',   # Nazwa: Podgórzyn, rzeka: Podgórna
'3.150150200',   # Nazwa: Sosnówka, rzeka: Czerwonka
'3.150160010',   # Nazwa: Kamienna Góra, rzeka: Bóbr
'3.150160020',   # Nazwa: Świebodzice, rzeka: Pełcznica
'3.150160030',   # Nazwa: Chwaliszów, rzeka: Strzegomka
'3.150160040',   # Nazwa: Kudowa Zdrój - Zakrze, rzeka: Klikawa
'3.150160060',   # Nazwa: Jugowice, rzeka: Bystrzyca
'3.150160070',   # Nazwa: Lubachów, rzeka: Bystrzyca
'3.150160080',   # Nazwa: Tłumaczów, rzeka: Ścinawka
'3.150160090',   # Nazwa: Łazany, rzeka: Strzegomka
'3.150160100',   # Nazwa: Gorzuchów, rzeka: Ścinawka
'3.150160110',   # Nazwa: Szalejów Dolny, rzeka: Bystrzyca Dusznicka
'3.150160120',   # Nazwa: Krasków, rzeka: Bystrzyca
'3.150160130',   # Nazwa: Mościsko, rzeka: Piława
'3.150160140',   # Nazwa: Dzierżoniów, rzeka: Piława
'3.150160150',   # Nazwa: Bystrzyca Kłodzka , rzeka: Bystrzyca Łomnicka
'3.150160160',   # Nazwa: Mietków, rzeka: Bystrzyca
'3.150160170',   # Nazwa: Bystrzyca Kłodzka, rzeka: Nysa Kłodzka
'3.150160180',   # Nazwa: Kłodzko, rzeka: Nysa Kłodzka
'3.150160190',   # Nazwa: Międzylesie, rzeka: Nysa Kłodzka
'3.150160200',   # Nazwa: Żelazno, rzeka: Biała Lądecka
'3.150160210',   # Nazwa: Wilkanów, rzeka: Wilczka
'3.150160220',   # Nazwa: Bardo, rzeka: Nysa Kłodzka
'3.150160230',   # Nazwa: Lądek Zdrój, rzeka: Biała Lądecka
'3.150160250',   # Nazwa: Białobrzezie, rzeka: Ślęza
'3.150160270',   # Nazwa: Kamieniec Ząbkowicki, rzeka: Budzówka
'3.150160280',   # Nazwa: Borów, rzeka: Ślęza
'3.150160290',   # Nazwa: Gniechowice, rzeka: Czarna Woda
'3.150170010',   # Nazwa: Zborowice, rzeka: Oława
'3.150170030',   # Nazwa: Oława, rzeka: Oława
'3.150170040',   # Nazwa: Oława, rzeka: Odra
'3.150170050',   # Nazwa: Biała Nyska, rzeka: Biała Głuchołaska
'3.150170060',   # Nazwa: Nysa, rzeka: Nysa Kłodzka
'3.150170070',   # Nazwa: Głuchołazy, rzeka: Biała Głuchołaska
'3.150170090',   # Nazwa: Brzeg, rzeka: Odra
'3.150170100',   # Nazwa: Kopice, rzeka: Nysa Kłodzka
'3.150170110',   # Nazwa: Prudnik, rzeka: Prudnik
'3.150170120',   # Nazwa: Niemodlin, rzeka: Ścinawa Niemodlińska
'3.150170130',   # Nazwa: Ujście Nysy Kłodzkiej, rzeka: Odra
'3.150170140',   # Nazwa: Skorogoszcz, rzeka: Nysa Kłodzka
'3.150170150',   # Nazwa: Karłowice, rzeka: Stobrawa
'3.150170160',   # Nazwa: Branice, rzeka: Opawa
'3.150170170',   # Nazwa: Branice, rzeka: Opawa-Młynówka
'3.150170180',   # Nazwa: Racławice Śląskie, rzeka: Osobłoga
'3.150170220',   # Nazwa: Dobra, rzeka: Biała
'3.150170240',   # Nazwa: Krapkowice, rzeka: Odra
'3.150170290',   # Nazwa: Opole - Groszowice, rzeka: Odra
'3.150180020',   # Nazwa: Turawa, rzeka: Mała Panew
'3.150180030',   # Nazwa: Koźle, rzeka: Odra
'3.150180040',   # Nazwa: Bojanów, rzeka: Psina
'3.150180050',   # Nazwa: Ozimek, rzeka: Mała Panew
'3.150180060',   # Nazwa: Racibórz Miedonia, rzeka: Odra
'3.150180070',   # Nazwa: Lenartowice, rzeka: Kłodnica
'3.150180080',   # Nazwa: Grabówka, rzeka: Bierawka
'3.150180100',   # Nazwa: Staniszcze Wielkie, rzeka: Mała Panew
'3.150180110',   # Nazwa: Ruda Kozielska, rzeka: Ruda
'3.150180130',   # Nazwa: Rybnik Stodoły, rzeka: Ruda
'3.150180150',   # Nazwa: Pyskowice Dzierżno, rzeka: Kłodnica
'3.150180160',   # Nazwa: Pyskowice Dzierżno, rzeka: Drama
'3.150180170',   # Nazwa: Pyskowice, rzeka: Drama
'3.150180180',   # Nazwa: Gliwice-Łabędy, rzeka: Kłodnica
'3.150180190',   # Nazwa: Krupski Młyn, rzeka: Mała Panew
'3.150180220',   # Nazwa: Gliwice, rzeka: Kłodnica
'3.150180280',   # Nazwa: Gotartowice, rzeka: Ruda
'3.151150030',   # Nazwa: Iłowa, rzeka: Czerna Mała
'3.151150040',   # Nazwa: Nowogród Bobrzański, rzeka: Bóbr 
'3.151150050',   # Nazwa: Dobroszów Wielki, rzeka: Bóbr
'3.151150060',   # Nazwa: Leśna, rzeka: Kwisa
'3.151150070',   # Nazwa: Żagań , rzeka: Czerna Wielka
'3.151150080',   # Nazwa: Żagań, rzeka: Bóbr
'3.151150090',   # Nazwa: Łozy, rzeka: Kwisa
'3.151150100',   # Nazwa: Nowogrodziec, rzeka: Kwisa
'3.151150110',   # Nazwa: Gryfów Śląski, rzeka: Kwisa
'3.151150120',   # Nazwa: Szprotawa, rzeka: Bóbr
'3.151150130',   # Nazwa: Szprotawa, rzeka: Szprotawa
'3.151150140',   # Nazwa: Dąbrowa Bolesławiecka, rzeka: Bóbr
'3.151150150',   # Nazwa: Nowa Sól, rzeka: Odra
'3.151150160',   # Nazwa: Zagrodno, rzeka: Skora
'3.151150170',   # Nazwa: Świerzawa, rzeka: Kaczawa
'3.151150180',   # Nazwa: Chojnów, rzeka: Skora
'3.151160020',   # Nazwa: Rzymówka, rzeka: Kaczawa
'3.151160040',   # Nazwa: Bukowna, rzeka: Czarna Woda
'3.151160050',   # Nazwa: Dunino, rzeka: Kaczawa
'3.151160060',   # Nazwa: Głogów, rzeka: Odra
'3.151160070',   # Nazwa: Winnica, rzeka: Nysa Szalona
'3.151160080',   # Nazwa: Rzeszotary, rzeka: Czarna Woda
'3.151160090',   # Nazwa: Jawor, rzeka: Nysa Szalona
'3.151160100',   # Nazwa: Piątnica, rzeka: Kaczawa
'3.151160120',   # Nazwa: Prochowice, rzeka: Kaczawa
'3.151160130',   # Nazwa: Ścinawa, rzeka: Odra
'3.151160140',   # Nazwa: Osetno, rzeka: Barycz
'3.151160150',   # Nazwa: Malczyce, rzeka: Odra
'3.151160160',   # Nazwa: Rydzyna, rzeka: Polski Rów
'3.151160170',   # Nazwa: Brzeg Dolny, rzeka: Odra
'3.151160180',   # Nazwa: Bogdaszowice, rzeka: Strzegomka
'3.151160190',   # Nazwa: Jarnołtów, rzeka: Bystrzyca
'3.151160200',   # Nazwa: Korzeńsko, rzeka: Orla
'3.151160220',   # Nazwa: Kanclerzowice, rzeka: Sąsiecznica
'3.151160230',   # Nazwa: Ślęża, rzeka: Ślęza
'3.151170010',   # Nazwa: Krzyżanowice, rzeka: Widawa
'3.151170030',   # Nazwa: Trestno, rzeka: Odra
'3.151170040',   # Nazwa: Łąki, rzeka: Barycz
'3.151170050',   # Nazwa: Zbytowa, rzeka: Widawa
'3.151170060',   # Nazwa: Bogdaj, rzeka: Polska Woda
'3.151170070',   # Nazwa: Odolanów, rzeka: Barycz
'3.151170080',   # Nazwa: Odolanów, rzeka: Kuroch
'3.151170090',   # Nazwa: Namyslów, rzeka: Widawa
'3.152150020',   # Nazwa: Stary Raduszec, rzeka: Bóbr 
'3.152150050',   # Nazwa: Nietków, rzeka: Odra
'3.152150130',   # Nazwa: Cigacice, rzeka: Odra
]
