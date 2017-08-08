# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 09:03
from __future__ import unicode_literals

from django.db import migrations


def add_tire(apps, schema_editor):
    intial = (
        (1, 'Accelera'),
        (2, 'Achilles'),
        (3, 'Aeolus'),
        (4, 'America'),
        (5, 'Amtel'),
        (6, 'Amtel-Vredestein'),
        (7, 'Apollo'),
        (8, 'Atturo'),
        (9, 'Aurora'),
        (10, 'Austone'),
        (11, 'Austyre'),
        (12, 'Avon'),
        (13, 'AvsTyre'),
        (14, 'Barum'),
        (15, 'BFGoodrich'),
        (16, 'Bridgestone'),
        (17, 'CEAT'),
        (18, 'Chengshan'),
        (19, 'Continental'),
        (20, 'Contyre'),
        (21, 'Cooper'),
        (22, 'Cordiant'),
        (23, 'Daewoo'),
        (24, 'Dayton'),
        (25, 'Dean'),
        (26, 'Debica'),
        (27, 'Diplomat'),
        (28, 'DMACK'),
        (29, 'Dunlop'),
        (30, 'Effiplus'),
        (31, 'Eurotec'),
        (32, 'Euzkadi'),
        (33, 'Falken'),
        (34, 'Fate'),
        (35, 'Federal'),
        (36, 'Fenix'),
        (37, 'Firenza'),
        (38, 'Firestone'),
        (39, 'Firststop'),
        (40, 'Flamingo'),
        (41, 'Formula'),
        (42, 'Fortuna'),
        (43, 'Forward'),
        (44, 'Fulda'),
        (45, 'FullWay'),
        (46, 'Fuzion'),
        (47, 'General'),
        (48, 'Gislaved'),
        (49, 'Goodride'),
        (50, 'Goodyear'),
        (51, 'GT'),
        (52, 'Hankook'),
        (53, 'Hercules'),
        (54, 'HIFLY'),
        (55, 'Infinity'),
        (56, 'Insa-Turbo'),
        (57, 'Interstate'),
        (58, 'Ironman'),
        (59, 'Kama'),
        (60, 'Kelly'),
        (61, 'Kelly Tires'),
        (62, 'Kenda'),
        (63, 'Kenex'),
        (64, 'Kingstar'),
        (65, 'Kirov'),
        (66, 'Kleber'),
        (67, 'Kormoran'),
        (68, 'Kumho'),
        (69, 'Lassa'),
        (70, 'LingLong'),
        (71, 'Mabor'),
        (72, 'Maloya'),
        (73, 'Marangoni'),
        (74, 'Marshal'),
        (75, 'Mastercraft'),
        (76, 'Matador'),
        (77, 'Matador-Омскшина'),
        (78, 'Maxtrek'),
        (79, 'Maxxis'),
        (80, 'Medved'),
        (81, 'Metzeler'),
        (82, 'Michelin'),
        (83, 'Mickey Thompson'),
        (84, 'Milestone'),
        (85, 'Millennium'),
        (86, 'Minerva'),
        (87, 'Mitas'),
        (88, 'MRF'),
        (89, 'Nankang'),
        (90, 'Neuton'),
        (91, 'Nexen Roadstone'),
        (92, 'Nitto'),
        (93, 'Nokian'),
        (94, 'Nordman'),
        (95, 'Novex'),
        (96, 'OHTSU'),
        (97, 'Ornet'),
        (98, 'Pirelli'),
        (99, 'Pneumant'),
        (100, 'PointS'),
        (101, 'PREMIORRI'),
        (102, 'President'),
        (103, 'Rapid'),
        (104, 'Regal'),
        (105, 'Remington'),
        (106, 'Riken'),
        (107, 'Rockstone'),
        (108, 'Rosava'),
        (109, 'Rotex'),
        (110, 'Sagitar'),
        (111, 'Sailun'),
        (112, 'Satoya'),
        (113, 'Sava'),
        (114, 'Semperit'),
        (115, 'SIBUR'),
        (116, 'Sportiva'),
        (117, 'StarFire'),
        (118, 'Starperformer'),
        (119, 'Stunner'),
        (120, 'Sumitomo'),
        (121, 'Sumo'),
        (122, 'Sunny'),
        (123, 'Tigar'),
        (124, 'Toyo'),
        (125, 'Tracmax'),
        (126, 'Trayal'),
        (127, 'Tunga'),
        (128, 'Tyrex'),
        (129, 'Uniroyal'),
        (130, 'Valsa'),
        (131, 'Viatti'),
        (132, 'Viking'),
        (133, 'Voltyre'),
        (134, 'Vredestein'),
        (135, 'VSP'),
        (136, 'Wanli'),
        (137, 'Westlake'),
        (138, 'Winterforce'),
        (139, 'Yokohama'),
        (140, 'Zeetex'),
        (141, 'АШК'),
        (142, 'Барнаул'),
        (143, 'Белшина'),
        (144, 'Воронеж'),
        (145, 'Дніпрошина'),
        (146, 'Кenda'),
        (147, 'Красноярск'),
        (148, 'МШЗ'),
        (149, 'НИИШП'),
        (150, 'Омскшина'),
        (151, 'Уралшина'),
        (152, 'ЯШЗ'),
        (153, 'Triangle'),
        (154, 'Headway'),
        (155, 'Horizon'),
    )

    tyre_vendor = apps.get_model("cards", "TyreVendor")
    for tyre in intial:
        tyre_vendor.objects.create(name=tyre[1])


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20170205_1154'),
    ]

    operations = [
        migrations.RunPython(add_tire),
    ]
