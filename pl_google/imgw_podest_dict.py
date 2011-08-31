#!/usr/bin/python
# -*- coding: utf-8 -*-

# Caution! I am not responsible for using these samples. Use at your own risk
# Google, Inc. is the copyright holder of samples downloaded with this tool.

# Generated automatically by imgw_podest.py. Feel free to modify it SLIGHTLY.

LANGUAGE = 'pl'

START_MARKER = 'ę. '
END_MARKER = ' k'

CUT_START = 0.9
CUT_END=0.7

download_list = [ 
    ['ę. rzeka', 'rzeka'],
    ['ę. wodowskaz', 'wodowskaz'],
    ['ę. przekroczenia stanów alarmowych', 'przekroczenia_stanow_alarmowych'],
    ['ę. komunikat hydrologiczny i emgjewu', 'komunikat_hydrologiczny_imgw'],
    ['ę. przekroczenia stanów ostrzegawczych', 'przekroczenia_stanow_ostrzegawczych'],
    ['ę. Gniechowice', 'gniechowice'],
    ['ę. Kamienica', 'kamienica'],
    ['ę. Łazany', 'l_azany'],
    ['ę. Jugowice', 'jugowice'],
    ['ę. Gliwice-Łabędy', 'gliwice_l_abe_dy'],
    ['ę. Bojanów', 'bojano_w'],
    ['ę. Prudnik', 'prudnik'],
    ['ę. Szprotawa', 'szprotawa'],
    ['ę. Zborowice', 'zborowice'],
    ['ę. Opole - Groszowice', 'opole___groszowice'],
    ['ę. Karłowice', 'karl_owice'],
    ['ę. Międzylesie', 'mie_dzylesie'],
    ['ę. Krapkowice', 'krapkowice'],
    ['ę. Odra', 'odra'],
    ['ę. Kamienna Góra', 'kamienna_go_ra'],
    ['ę. Iłowa', 'il_owa'],
    ['ę. Pełcznica', 'pel_cznica'],
    ['ę. Opawa', 'opawa'],
    ['ę. Jarnołtów', 'jarnol_to_w'],
    ['ę. Sosnówka', 'sosno_wka'],
    ['ę. Zbytowa', 'zbytowa'],
    ['ę. Cigacice', 'cigacice'],
    ['ę. Orla', 'orla'],
    ['ę. Rzeszotary', 'rzeszotary'],
    ['ę. Łąki', 'l_a_ki'],
    ['ę. Brzeg Dolny', 'brzeg_dolny'],
    ['ę. Krasków', 'krasko_w'],
    ['ę. Bystrzyca Łomnicka', 'bystrzyca_l_omnicka'],
    ['ę. Gliwice', 'gliwice'],
    ['ę. Łaziska', 'l_aziska'],
    ['ę. Turawa', 'turawa'],
    ['ę. Kanclerzowice', 'kanclerzowice'],
    ['ę. Kowary', 'kowary'],
    ['ę. Cieszyn', 'cieszyn'],
    ['ę. Dąbrowa Bolesławiecka', 'da_browa_bolesl_awiecka'],
    ['ę. Dzierżoniów', 'dzierz_onio_w'],
    ['ę. Kaczawa', 'kaczawa'],
    ['ę. Jedlica', 'jedlica'],
    ['ę. Kopice', 'kopice'],
    ['ę. Widawa', 'widawa'],
    ['ę. Oława', 'ol_awa'],
    ['ę. Pyskowice Dzierżno', 'pyskowice_dzierz_no'],
    ['ę. Ścinawa', 's_cinawa'],
    ['ę. Nysa Kłodzka', 'nysa_kl_odzka'],
    ['ę. Gotartowice', 'gotartowice'],
    ['ę. Osetno', 'osetno'],
    ['ę. Koźle', 'kox_le'],
    ['ę. Szalejów Dolny', 'szalejo_w_dolny'],
    ['ę. Trestno', 'trestno'],
    ['ę. Czarny Potok', 'czarny_potok'],
    ['ę. Ścinawa Niemodlińska', 's_cinawa_niemodlin_ska'],
    ['ę. Strzegomka', 'strzegomka'],
    ['ę. Klikawa', 'klikawa'],
    ['ę. Jelenia Góra', 'jelenia_go_ra'],
    ['ę. Ujście Nysy Kłodzkiej', 'ujs_cie_nysy_kl_odzkiej'],
    ['ę. Mirsk', 'mirsk'],
    ['ę. Lądek Zdrój', 'la_dek_zdro_j'],
    ['ę. Branice', 'branice'],
    ['ę. Krupski Młyn', 'krupski_ml_yn'],
    ['ę. Bystrzyca', 'bystrzyca'],
    ['ę. Żelazno', 'z_elazno'],
    ['ę. Wilkanów', 'wilkano_w'],
    ['ę. Kudowa Zdrój - Zakrze', 'kudowa_zdro_j___zakrze'],
    ['ę. Leśna', 'les_na'],
    ['ę. Czarna Woda', 'czarna_woda'],
    ['ę. Bogdaszowice', 'bogdaszowice'],
    ['ę. Biała Lądecka', 'bial_a_la_decka'],
    ['ę. Błażkowa', 'bl_az_kowa'],
    ['ę. Podgórzyn', 'podgo_rzyn'],
    ['ę. Barycz', 'barycz'],
    ['ę. Czerwonka', 'czerwonka'],
    ['ę. Czerna Mała', 'czerna_mal_a'],
    ['ę. Olza', 'olza'],
    ['ę. Drama', 'drama'],
    ['ę. Piława', 'pil_awa'],
    ['ę. Malczyce', 'malczyce'],
    ['ę. Rzymówka', 'rzymo_wka'],
    ['ę. Bardo', 'bardo'],
    ['ę. Barcinek', 'barcinek'],
    ['ę. Lubachów', 'lubacho_w'],
    ['ę. Czerna Wielka', 'czerna_wielka'],
    ['ę. Łozy', 'l_ozy'],
    ['ę. Bystrzyca Kłodzka', 'bystrzyca_kl_odzka'],
    ['ę. Stary Raduszec', 'stary_raduszec'],
    ['ę. Prochowice', 'prochowice'],
    ['ę. Tłumaczów', 'tl_umaczo_w'],
    ['ę. Lenartowice', 'lenartowice'],
    ['ę. Mietków', 'mietko_w'],
    ['ę. Odolanów', 'odolano_w'],
    ['ę. Ślęza', 's_le_za'],
    ['ę. Młynówka', 'ml_yno_wka'],
    ['ę. Rów Polski', 'ro_w_polski'],
    ['ę. Świebodzice', 's_wiebodzice'],
    ['ę. Podgórna', 'podgo_rna'],
    ['ę. Bukowna', 'bukowna'],
    ['ę. Kłodzko', 'kl_odzko'],
    ['ę. Sąsiecznica', 'sa_siecznica'],
    ['ę. Gorzuchów', 'gorzucho_w'],
    ['ę. Jakuszyce', 'jakuszyce'],
    ['ę. Żagań', 'z_agan_'],
    ['ę. Ruda', 'ruda'],
    ['ę. Chojnów', 'chojno_w'],
    ['ę. Nysa Szalona', 'nysa_szalona'],
    ['ę. Nowogród Bobrzański', 'nowogro_d_bobrzan_ski'],
    ['ę. Kuroch', 'kuroch'],
    ['ę. Piechowice', 'piechowice'],
    ['ę. Głogów', 'gl_ogo_w'],
    ['ę. Biała Nyska', 'bial_a_nyska'],
    ['ę. Kwisa', 'kwisa'],
    ['ę. Bóbr ', 'bo_br_'],
    ['ę. Ścinawka', 's_cinawka'],
    ['ę. Kamienna', 'kamienna'],
    ['ę. Bogdaj', 'bogdaj'],
    ['ę. Korzeńsko', 'korzen_sko'],
    ['ę. Bierawka', 'bierawka'],
    ['ę. Staniszcze Wielkie', 'staniszcze_wielkie'],
    ['ę. Rybnik Stodoły', 'rybnik_stodol_y'],
    ['ę. Dobroszów Wielki', 'dobroszo_w_wielki'],
    ['ę. Biała Głuchołaska', 'bial_a_gl_uchol_aska'],
    ['ę. Skora', 'skora'],
    ['ę. Namyslów', 'namyslo_w'],
    ['ę. Stobrawa', 'stobrawa'],
    ['ę. Winnica', 'winnica'],
    ['ę. Głuchołazy', 'gl_uchol_azy'],
    ['ę. Jawor', 'jawor'],
    ['ę. Kłodnica', 'kl_odnica'],
    ['ę. Niemodlin', 'niemodlin'],
    ['ę. Kamieniec Ząbkowicki', 'kamieniec_za_bkowicki'],
    ['ę. Pyskowice', 'pyskowice'],
    ['ę. Krzyżanowice', 'krzyz_anowice'],
    ['ę. Świerzawa', 's_wierzawa'],
    ['ę. Łomnica', 'l_omnica'],
    ['ę. Piątnica', 'pia_tnica'],
    ['ę. Nysa', 'nysa'],
    ['ę. Gryfów Śląski', 'gryfo_w_s_la_ski'],
    ['ę. Borów', 'boro_w'],
    ['ę. Skorogoszcz', 'skorogoszcz'],
    ['ę. Mała Panew', 'mal_a_panew'],
    ['ę. Bystrzyca Dusznicka', 'bystrzyca_dusznicka'],
    ['ę. Grabówka', 'grabo_wka'],
    ['ę. Chałupki', 'chal_upki'],
    ['ę. Nowogrodziec', 'nowogrodziec'],
    ['ę. Chwaliszów', 'chwaliszo_w'],
    ['ę. Budzówka', 'budzo_wka'],
    ['ę. Wilczka', 'wilczka'],
    ['ę. Polska Woda', 'polska_woda'],
    ['ę. Bukówka', 'buko_wka'],
    ['ę. Racławice Śląskie', 'racl_awice_s_la_skie'],
    ['ę. Biała', 'bial_a'],
    ['ę. Brzeg', 'brzeg'],
    ['ę. Nowa Sól', 'nowa_so_l'],
    ['ę. Osobłoga', 'osobl_oga'],
    ['ę. Bóbr', 'bo_br'],
    ['ę. Ozimek', 'ozimek'],
    ['ę. Dunino', 'dunino'],
    ['ę. Białobrzezie', 'bial_obrzezie'],
    ['ę. Istebna', 'istebna'],
    ['ę. Zagrodno', 'zagrodno'],
    ['ę. Rydzyna', 'rydzyna'],
    ['ę. Pilchowice', 'pilchowice'],
    ['ę. Ruda Kozielska', 'ruda_kozielska'],
    ['ę. Psina', 'psina'],
    ['ę. Nietków', 'nietko_w'],
    ['ę. Ślęża', 's_le_z_a'],
    ['ę. Mościsko', 'mos_cisko'],
    ['ę. Dobra', 'dobra'],
    ['ę. Wojanów', 'wojano_w'],
    ['ę. Racibórz Miedonia', 'racibo_rz_miedonia'],
]

