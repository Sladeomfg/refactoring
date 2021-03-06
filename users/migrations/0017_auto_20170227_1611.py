# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 13:11
from __future__ import unicode_literals

from django.db import migrations

CITIES = (
    '2-я Гавриловка (Тамбовская область)',
    'Абакан (Республика Хакасия)',
    'Азов (Ростовская область)',
    'Аксай (Ростовская область)',
    'Алапаевск (Свердловская область)',
    'Алексеевка (Белгородская область)',
    'Алексин (Тульская область)',
    'Алушта (Крым)',
    'Альметьевск',
    'Анапа (Краснодарский край)',
    'Анжеро-Судженск (Кемеровская область)',
    'Апатиты (Мурманская область)',
    'Арамильский ГО (Свердловская область)',
    'Ардон (Республика Северная Осетия-Алания)',
    'Арзамас (Нижегородская область)',
    'Армавир',
    'Арсеньев (Приморский Край)',
    'Арсеньево (Тульская область)',
    'Артемовск (Свердловская область)',
    'Архангельск (Архангельская область)',
    'Асбест (Свердловская область)',
    'Астрахань (Астраханская область)',
    'Ахтубинск (Астраханская область)',
    'Ачинск',
    'Баган (Новосибирская область)',
    'Балаково (Саратовская область)',
    'Балашиха (Московская область)',
    'Балтийск (Калининградская область)',
    'Барабинск (Новосибирская область)',
    'Барнаул (Алтайский край)',
    'Барыш (Ульяновская область)',
    'Батайск (ростовская область)',
    'Бахчисарай (Крым)',
    'Белгород (Белгородская область)',
    'Белев (Тульская область)',
    'Белово (Кемеровская область)',
    'Беломорск (Республика Карелия)',
    'Белореченск (Краснодарский край)',
    'Белоярский (Ханты-Мансийский АО)',
    'Белоярский ГО (Свердловская область)',
    'Бердск (Новосибирская область)',
    'Березники (Пермский край)',
    'Березово (Ханты-Мансийский АО)',
    'Березовский (Кемеровская область)',
    'Березовский (Свердловская область)',
    'Беслан (Республика Северная Осетия-Алания)',
    'Бийск (Алтайский край)',
    'Бийск(Алтайский край)',
    'Биробиджан (Еврейская автономная область)',
    'Бирюч (Белгородская область)',
    'Бисертский ГО (Свердловская область)',
    'Благовещенск (Амурская область)',
    'Благодарный (Ставропольский край)',
    'Богданович (Свердловская область)',
    'Богородицк (Тульская область)',
    'Богучар (Воронежская область)',
    'Болотное (Новосибирская область)',
    'Бондари (Тамбовская область)',
    'Борисоглебск (Тамбовская область)',
    'Боровичи (Новгородская область)',
    'Боровск (Калужская область)',
    'Братск (Иркутская область)',
    'Брянск (Брянская область)',
    'Бугульма',
    'Бугурслан (Оренбургская область)',
    'Бузулук (Оренбургская область)',
    'Валдай (Новгородская область)',
    'Валуйки (Белгородская область)',
    'Великие Луки (Псковская область)',
    'Великий Новгород (Новгородская область)',
    'Великий Устюг (Вологодская область)',
    'Вельск (Архангельская  область)',
    'Вельск (Архангельская область)',
    'Венгерово (Новосибирская область)',
    'Венев (Тульская область)',
    'Верхний Тагил (Свердловская область)',
    'Верхняя Пышма (Свердловская область)',
    'Видное (Московская область)',
    'Видяево (Мурманская область)',
    'Вилюйск (Якутия)',
    'Вихоревка (Иркутской область)',
    'Владивосток (Приморский край)',
    'Владикавказ (Республика Северная Осетия-Алания)',
    'Владимир (Владимирская область)',
    'Волгоград (Волгоградская область)',
    'Волжск (Республика Марий Эл)',
    'Волжский (Волгоградская область)',
    'Волово (Липецкая область)',
    'Вологда (Вологодская область)',
    'Володарский (Астраханская область)',
    'Воркута (Республика Коми)',
    'Воронеж (Воронежская область)',
    'Воскресенск (Московская область)',
    'Всеволожск (Ленинградская область)',
    'Выборг (Ленинградская область)',
    'Выкса (Нижегородская область)',
    'Вязьма (Смоленская область)',
    'Вятские Поляны (Кировская область)',
    'Гагарин (Смоленская область)',
    'Гаджиево (Мурманская область)',
    'Гатчина (Ленинградская область)',
    'Геленджик (Краснодарский край)',
    'Георгиевск (Ставропольский край)',
    'Глазов (Удмуртская Республика)',
    'Горно- Алтайск (Республика Алтай)',
    'Горячий Ключ (Краснодарский край)',
    'Грайворон (Белгородская область)',
    'Грозный (Чеченская республика)',
    'Грязи (Липецкая область)',
    'Губкин (Белгородская область)',
    'Гурьевск (Кемеровская область)',
    'Гусиноозерск (республика Бурятия)',
    'Данков (Липецкая область)',
    'Дегтярск (Свердловская область)',
    'Демидов (Смоленской область)',
    'Десногорск (Смоленская область)',
    'Дзержинск (Нижегородская область)',
    'Димитровград (Ульяновская область)',
    'Дмитриевка (Тамбовская область)',
    'Дмитриев-Льговский (Курская область)',
    'Доброе (Липецкая область)',
    'Довольное (Новосибирская область)',
    'Долгоруково (Липецкая область)',
    'Домодедово (Московская область)',
    'Донской (Тульская область)',
    'Дорогобуж (Смоленская область)',
    'Дубна (Московская обл)',
    'Екатеринбург (Свердловская область)',
    'Елец (Липецкая область)',
    'Енотаевка (Астраханская область)',
    'Ефремов (Тульская область)',
    'Железногорс-Илимский (Иркутской обл.)',
    'Железногорск (Курская область)',
    'Железнодорожный (Московская область )',
    'Жердевка (Тамбовская область)',
    'Жиздра (Калужская область)',
    'Жуков (Калужская область)',
    'Задонск (Липецкая область)',
    'Заинск',
    'Заозерск (Мурманская область)',
    'Заокский (Тульская область)',
    'Заполярный (Мурманская область)',
    'Заречный (Свердловская область)',
    'Здвинск (Новосибирская область)',
    'Зеленодольск',
    'Зеленодольск ( Татарстан)',
    'Зилаир (Республика Башкортостан)',
    'Златоуст (Челябинская область)',
    'Знаменка (Тамбовская область)',
    'Знаменск (Астраханская область)',
    'Иваново (Ивановская область)',
    'Ивня (Белгородская область)',
    'Ижевск (Удмуртская Республика)',
    'Измалково (Липецкая область)',
    'Икряное (Астраханская область)',
    'Инжавино (Тамбовская область)',
    'Инза (Ульяновская область)',
    'Инза (Ульяновская область,  )',
    'Ирбит (Свердловская область)',
    'Иркутск (Иркутская область)',
    'Искитим (Новосибирская область)',
    'Ишим (Тюменская область)',
    'Йошкар-Ола (Республика Марий Эл)',
    'Казань (Республика Татарстан)',
    'Калининград (Калининградская область)',
    'Калтан (Кемеровская область)',
    'Калуга (Калужская область)',
    'Каменка (Пензенская область)',
    'Каменский ГО (Свердловская область)',
    'Каменск-Уральский (Свердловская область)',
    'Камызяк (Астраханская область)',
    'Камышин (Волгоградская область)',
    'Камышлов (Свердловская область)',
    'Канаш (Республика Чувашия)',
    'Кандалакша (Мурманская область)',
    'Карасук (Новосибирская область)',
    'Каргат (Новосибирская область)',
    'Карталы (Челябинская область)',
    'Карталы (Челябинская область)',
    'Качканар (Свердловская область)',
    'Кашин (Тверской область)',
    'Кемерово (Кемеровская область)',
    'Керчь (Крым)',
    'Кимовск (Тульская область)',
    'Кингисепп (Ленинградская область)',
    'Киреевск (Тульская область)',
    'Кириши (Ленинградская область)',
    'Киров (Калужская область)',
    'Киров (Кировская область)',
    'Кировоградский (Свердловская область)',
    'Кирово-Чепецк (Кировская область)',
    'Кировск (Мурманская область)',
    'Кирсанов (Тамбовская область)',
    'Киселевск (Кемеровская область)',
    'Кисловодск (Ставропольский край)',
    'Клинцы (Брянская область)',
    'Ковдор (Мурманская область)',
    'Ковров (Владимирская область)',
    'Когалым (Ханты-Мансийский АО)',
    'Козельск (Калужская область)',
    'Козьмодемьянск (Республика Марий Эл)',
    'Кола (Мурманская область)',
    'Колпино (Ленинградская область)',
    'Колывань (Новосибирская область)',
    'Кольцово (Новосибирская область)',
    'Комсомольск-на-Амуре (Хабаровский край)',
    'Комсомольск-на-Амуре (Хабаровский край)',
    'Кондрово (Калужская область)',
    'Косая Гора (Тульская область)',
    'Костомукша (Республика Карелия)',
    'Кострома (Костромская область)',
    'Котлас (Архангельская область)',
    'Котовск (Тамбовская область)',
    'Коченёво (Новосибирская область)',
    'Кочки (Новосибирская область)',
    'Красная Яруга (Белгородская область)',
    'Красногорск М.О.',
    'Краснодар (Краснодарский край)',
    'Красное (Липецкая область)',
    'Красное село (Санкт-Петербург)',
    'Краснозерское (Новосибирская область)',
    'Краснообск (Новосибирская область)',
    'Красноярск (Красноярский край)',
    'Красный Яр (Астраханская область)',
    'Кронштадт (Санкт-Петербург)',
    'Кропоткин (Краснодарский край)',
    'Кузнецк (Пензенская область)',
    'Куйбышев (Новосибирская область)',
    'Купино (Новосибирская область)',
    'Курган (Курганская область)',
    'Куркино (Тульская область)',
    'Курск (Курская область)',
    'Кызыл (Республика Тыва)',
    'Кыштовка (Новосибирская область)',
    'Лангепас (Ханты-Мансийский АО)',
    'Лебедянь (Липецкая область)',
    'Лесной (Свердловская область)',
    'Лесозаводск (Приморский край)',
    'Ливны (Орловская область)',
    'Лиман (Астраханская область)',
    'Липецк (Липецкая область)',
    'Л-Кузнецкий (Кемеровская область)',
    'Ловозеро (Мурманская область)',
    'Лодейное поле (Ленинградская область)',
    'Лыткарино (Московская область)',
    'Лыткарино (Московская область)',
    'Людиново (Калужская область)',
    'Магадан (Магаданская область)',
    'Магнитогорск (Челябинская область)',
    'Майкоп (Адыгея)',
    'Малоярославец (Калужская область)',
    'Малышевский ГО (Свердловская область)',
    'Мамадыш (Республика Татарстан)',
    'Мариинск (Кемеровская область)',
    'Маслянино (Новосибирская область)',
    'Махачкала (Республика Дагестан)',
    'Мегион (Ханты-Мансийский АО)',
    'Медвежьегорск (Республика Карелия)',
    'Медынь (Калужская область)',
    'Междуреченск (Кемеровская область)',
    'Междуреченский (Ханты-Мансийский АО)',
    'Мещовск (Калужская область)',
    'Миасс (Челябинская область)',
    'Минусинск (Красноярский край)',
    'Мирный (Архангельская  область)',
    'Мичуринск (Тамбовская область)',
    'Моздок (Республика Северная Осетия-Алания)',
    'Монастырщина (Смоленская область)',
    'Мончегорск (Мурманская область)',
    'Мордово (Тамбовская область)',
    'Моршанск (Тамбовская область)',
    'Мосальск (Калужская область)',
    'Москва (Москва)',
    'Мошково (Новосибирская область)',
    'Мурманск (Мурманская область)',
    'Мурмаши (Мурманская область)',
    'Муром (Владимирская область)',
    'Мучкап (Тамбовская область)',
    'Мценск (Мценская область)',
    'Мыски (Кемеровская область)',
    'Мытищи (Московская область)',
    'Набережные Челны',
    'Надын',
    'Назрань',
    'Нальчик (Кабардино-Балкария)',
    'Нариманов (Астраханская область)',
    'Наро-Фоминск (Московская область)',
    'Нарьян-Мар (Ненецкий АО)',
    'Находка (Приморский край)',
    'Началово (Астраханская область)',
    'Невьянск (Свердловская область)',
    'Невьянский ГО(Свердловская область)',
    'Нерчинск (Забайкальский край)',
    'Нерюнгри',
    'Нефтекамск',
    'Нефтеюганск (Ханты-Мансийский АО)',
    'Нижневартовск (Ханты-Мансийский АО)',
    'Нижнекамск',
    'Нижнесергинский МР (Свердловская область)',
    'Нижний Новгород (Нижегородская область)',
    'Нижний Тагил (Свердловская область)',
    'Никель (Мурманская область)',
    'Новокузнецк (Кемеровская область)',
    'Новокуйбышевск (Самарская область)',
    'Новомосковск (Тульская область)',
    'Новороссийск (Краснодарский край)',
    'Новосибирск (Новосибирская область)',
    'Новоуральск (Свердловская область)',
    'Новочебоксарск (Чувашская Республика)',
    'Новочеркаск (Ростовская область)',
    'Новый Оскол (Белгородская область)',
    'Новый Уренгой',
    'Ногинск (Московская область)',
    'Норильск (Красноярский край)',
    'Ноябрьск',
    'Нягань (Ханты-Мансийский АО)',
    'Обнинск, (Калужская область)',
    'Обь (Новосибирская область)',
    'Одоев (Тульская область)',
    'Октябрьское (Республика Северная Осетия-Алания)',
    'Октябрьское (Ханты-Мансийский АО)',
    'Оленегорск (Мурманская область)',
    'Олонец (Республика Карелия)',
    'Олонец (Республика Карелия)',
    'Омск (Омская область)',
    'Опочка (Псковской область)',
    'Ордынское (Новосибирская область)',
    'Орел (Орловская область)',
    'Оренбург (Оренбургская область)',
    'Орск (Оренбургская область)',
    'Осинники (Кемеровская область)',
    'Пенза (Пензенская область)',
    'Первомайский (Тамбовская область)',
    'Первоуральск (Свердловская область)',
    'Переславль-Залесский (Ярославская область)',
    'Пермь (Пермский край)',
    'Петергоф (Ленинградская область)',
    'Петергоф (Санкт-Петербург)',
    'Петровское (Тамбовская область)',
    'Петрозаводск (Республика Карелия)',
    'Петропавловск-Камчатский (Камчатский край)',
    'Печора (Республика Коми)',
    'Пионерский (Калининградская область)',
    'Пичаево (Тамбовская область)',
    'Плавск (Тульская область)',
    'Плесецк (Архангельская область)',
    'Покачи (Ханты-Мансийский АО)',
    'Полевской (Свердловская область)',
    'Полысаево (Кемеровская область)',
    'Полярные Зори (Мурманская область)',
    'Полярный (Мурманская область)',
    'поселок Деденево (Московская область, Дмитровский район)',
    'поселок Новосиньково (Московская область, Дмитровский район)',
    'Починок (Смоленская область)',
    'Приозерск (Ленинградская область)',
    'Прокопьевск (Кемеровская область)',
    'Псков (Псковская область)',
    'Пушкин (Ленинградская область)',
    'Пушкин (Санкт-Петербург)',
    'Пушкино (Московская область)',
    'Пыть-Ях (Ханты-Мансийский АО)',
    'Пятигорск (Cтавропольский край)',
    'Пятигорск (Ставропольский край)',
    'Радужный (Ханты-Мансийский АО)',
    'Ракитное (Белгородская область)',
    'Рассказово (Тамбовская область)',
    'Ревда (Мурманская область)',
    'Ревда (Свердловская область)',
    'Реж (Свердловская область)',
    'Реутов (Московская область)',
    'Рефтинский (Свердловская область)',
    'Ржакса (Тамбовская область)',
    'Рославль (Смоленская область)',
    'Росляково (Мурманская область)',
    'Ростов (Ярославская область)',
    'Ростов-на-Дону (Ростовская область)',
    'Рудня (Смоленская область)',
    'Рузаевка (Республика Мордовия)',
    'Рыбинск (Ярославская область)',
    'Рязань (Рязанская область)',
    'Салехард (ЯНАО)',
    'Самара (Самарская область)',
    'Санкт-Петербург (Санкт-Петербург)',
    'Саранск (Республика Мордовия)',
    'Сарапул (Удмуртская Республика)',
    'Саратов (Саратовская область)',
    'Саров (Нижегородская область)',
    'Сатинка (Тамбовская область)',
    'Сафоново (Смоленская область)',
    'Саяногорск (республика Хакасия)',
    'Севастополь (Крым)',
    'Северное (Новосибирская область)',
    'Северодвинск (Архангельская область)',
    'Североморск (Мурманская область)',
    'Сергиев Посад (Московская область)',
    'Сестрорецк (Ленинградская область)',
    'Симферополь (Крым)',
    'Славгород (Алтайский край)',
    'Славянск-на-Кубани (Краснодарский край)',
    'Смоленск (Смоленская область)',
    'Снежногорск (Мурманская область)',
    'Советск (Калининградская область)',
    'Советский (Ханты-Мансийский АО)',
    'Сорск (Республика Хакасия)',
    'Сортавала (Республика Карелия)',
    'Сосновка (Тамбовская область)',
    'Сосново (Ленинградская область)',
    'Сосновый Бор (Ленинградская область)',
    'Сосногорск (Республика Коми)',
    'Сочи (Краснодарский край)',
    'Спас-Деменск (Калужская область)',
    'Спасск-Дальний (Приморский край)',
    'Среднеуральск (Свердловская область)',
    'Ставрополь (Ставропольский край)',
    'Становое (Липецкая область)',
    'Старая Русса (Новгородская область)',
    'Староюрьево (Тамбовская область)',
    'Старый Оскол (Белгородская область)',
    'Стерлитамак (респ.Башкортостан)',
    'Строитель (Белгородская область)',
    'Ступино (Московская область)',
    'Суворов (Тульская область)',
    'Сузун (Новосибирская область)',
    'Сургут (Ханты-Мансийский АО)',
    'Сухиничи (Калужская область)',
    'Сухой Лог (Свердловская область)',
    'Сызрань (Самарская область)',
    'Сыктывкар (Республика Коми)',
    'Сысерть (Свердловская область)',
    'Таганрог (Ростовская область)',
    'Тайга (Кемеровская область)',
    'Тамбов (Тамбовская область)',
    'Таруса (Калужская область)',
    'Татарск (Новосибирская область)',
    'Таштагол (Кемеровская область)',
    'Тверь (Тверская область)',
    'Тербуны (Липецкая область)',
    'Тихвин (Ленинградская область)',
    'Тобольск (Тюменская область)',
    'Тогучин (Новосибирская область)',
    'Токаревка (Тамбовская область)',
    'Тольятти (Самарская область)',
    'Томск (Томская область)',
    'Топки (Кемеровская область)',
    'Торжок (Тверская область)',
    'Тотьма (Вологодская область)',
    'Туймазы (Башкортостан)',
    'Тула (Тульская область)',
    'Тутаев (Ярославская область)',
    'Тюмень (Тюменская область)',
    'Убинское (Новосибирская область)',
    'Уварово (Тамбовская область)',
    'Углич (Ярославская область)',
    'Узловая (Тульская область)',
    'Улан-Удэ (Республика Бурятия)',
    'Ульяновск (Ульяновская область)',
    'Умба (Мурманская область)',
    'Умет (Тамбовская область)',
    'Урай (Ханты-Мансийский АО)',
    'Усинск (Республика Коми)',
    'Усмань (Липецкая область)',
    'Уссурийск (Приморский край)',
    'Усть-Тарка (Новосибирская область)',
    'Уфа (Республика Башкортостан)',
    'Ухта (Республика Коми)',
    'Феодосия (республика Крым)',
    'Фрязино (Московская область)',
    'Хабаровск (Хабаровский край)',
    'Ханты-Мансийск (Ханты-Мансийский АО)',
    'Харабали (Астраханская область)',
    'Хасавюрт (Дагестан)',
    'Хасавюрт (республика Дагестан)',
    'Химки (Московская область)',
    'Хлевное (Липецкая область)',
    'Чаны (Новосибирская область)',
    'Чаплыгин (Липецкая область)',
    'Чебоксары (Республика Чувашия)',
    'Челябинск (Челябинская область)',
    'Черепаново (Новосибирская область)',
    'Череповец (Вологодская область)',
    'Черкесск (Карачаево-Черкессия)',
    'Черногорск (Республика Хакасия)',
    'Черный Яр (Астраханская область)',
    'Чернь (Тульская область)',
    'Черняховск (Калининградская область)',
    'Чистоозерное (Новосибирская область)',
    'Чита (Забайкальский край)',
    'Чулым (Новосибирская область)',
    'Шалинский ГО (Свердловская область)',
    'Шахты (Ростовская область)',
    'Щекино (Тульская область)',
    'Щёлково (Московская область)',
    'Электросталь (Московская область)',
    'Элиста (Калмыкия)',
    'Энгельс (Саратовская область)',
    'Югорск (Ханты-Мансийский АО)',
    'Южно-Сахалинск (Сахалинская область)',
    'Южноуральск (Челябинская область)',
    'Юрга, (Кемеровская область)',
    'Юхнов (Калужская область)',
    'Якутск (Республика Саха, Якутия)',
    'Ялта (Крым)',
    'Ярославль (Ярославская область)',
    'Ярцево (Смоленская область)',
    'Ясногорск (Тульская область)',
)


def add_cities(apps, *args, **kwargs):
    City = apps.get_model('users', 'City')
    for city_name in CITIES:
        City.objects.create(name=city_name)


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20170227_1611'),
    ]

    operations = [
        migrations.RunPython(add_cities)
    ]
