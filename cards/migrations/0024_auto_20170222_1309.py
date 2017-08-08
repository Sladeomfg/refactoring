# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 10:09
from __future__ import unicode_literals

from django.db import migrations


SOURCE_DATA = (
    ('Acura', ['CL', 'EL', 'Integra', 'MDX', 'NSX', 'RDX', 'RL', 'RSX', 'TL', 'TSX']),
    ('Alfa Romeo', ['33', '75', '145', '146', '147', '155', '156', '159', '164', '166', 'Alfetta', 'Brera', 'GT', 'GTV', 'Giulietta', 'Spider']),
    ('Alpina', ['B11', 'B12', 'B3', 'B6', 'B7', 'Roadster S']),
    ('Aro', ['10', '24']),
    ('Asia', ['Rocsta']),
    ('Aston Martin', ['DB7', 'DB9', 'DBS', 'V12 Vanquish', 'V8']),
    ('Audi', ['80', '90', '100', '200', 'A2', 'A3', 'A4', 'A5', 'A6', 'A8', 'Allroad', 'Cabriolet', 'Coupe', 'Q7', 'Quattro', 'R8', 'RS4', 'RS6', 'S2', 'S3', 'S4', 'S5', 'S6', 'S8', 'TT', 'V8 (D11)']),
    ('Austin', ['Metro', 'Mini MK', 'Montego']),
    ('Bentley', ['Arnage', 'Azure', 'Brooklands', 'Continental', 'Mulsanne', 'Turbo R']),
    ('BMW', ['02 (E10)', '1er 116', '1er 118', '1er 120', '1er 130', '3er 315', '3er 316', '3er 318', '3er 320', '3er 323', '3er 324', '3er 325', '3er 328', '3er 330', '3er 335', '5er 518', '5er 520', '5er 523', '5er 524', '5er 525', '5er 528', '5er 530', '5er 535', '5er 540', '5er 545', '5er 550', '6er 628', '6er 630', '6er 635', '6er 645', '6er 650', '7er 725', '7er 728', '7er 730', '7er 732', '7er 735', '7er 740', '7er 745', '7er 750', '7er 760', '8er 850', 'M3', 'M5', 'M6', 'X3', 'X5', 'X6', 'Z1', 'Z3', 'Z3 M', 'Z4', 'Z4 M', 'Z8']),
    ('Brilliance', ['M1', 'M2']),
    ('Bugatti', ['57 SC Atlantic', 'EB 16.4']),
    ('Buick', ['Century', 'Enclave', 'LE Sabre', 'Park Avenue', 'Reatta', 'Rendezvous', 'Riviera', 'Roadmaster', 'Skylark']),
    ('BYD', ['F3', 'FLYER II']),
    ('Cadillac', ['BLS', 'CTS', 'Catera', 'DE Ville', 'Eldorado', 'Escalade', 'Fleetwood', 'SRX', 'STS', 'Seville', 'XLR']),
    ('Caterham', ['Super Seven']),
    ('ChangFeng', ['Flying', 'SUV']),
    ('Chery', ['Amulet', 'Flagcloud', 'Fora', 'Kimo (A1)', 'Oriental Son', 'QQ6 (S21)', 'Sweet (QQ)', 'Tiggo']),
    ('Chevrolet', ['Alero', 'Astro', 'Avalanche', 'Aveo', 'Beretta', 'Blazer', 'C-10', 'Camaro', 'Caprice', 'Captiva', 'Cavalier', 'Cobalt', 'Colorado', 'Corsica', 'Corvette', 'Epica', 'Equinox', 'Evanda', 'Express', 'Geo Storm', 'HHR', 'Impala', 'Lacetti', 'Lanos', 'Lumina', 'Metro', 'Niva', 'Prizm', 'Rezzo', 'SSR', 'Savana', 'Silverado', 'Spark', 'Starcraft', 'Suburban', 'Tahoe', 'Tracker', 'Trailblazer', 'Uplander', 'Van', 'Venture', 'Viva']),
    ('Chrysler', ['300C', '300M', 'Aspen', 'Cirrus', 'Concorde', 'Crossfire', 'Fifth Avenue', 'Grand Voyager', 'Intrepid', 'LE Baron', 'LHS', 'NEW Yorker', 'Neon', 'PT Cruiser', 'Pacifica', 'Prowler', 'Saratoga', 'Sebring', 'Stratus', 'Town amp']),
    ('Citroen', ['AX', 'BX', 'Berlingo', 'C2', 'C25', 'C3', 'C4', 'C4 Picasso', 'C5', 'C6', 'C8', 'Evasion', 'Jumper', 'Jumpy', 'LNA', 'Saxo', 'Visa', 'XM', 'Xantia', 'Xsara', 'Xsara Picasso', 'ZX']),
    ('Coggiola', ['T-Rex']),
    ('Dacia', ['1410']),
    ('Dadi', ['City Leading', 'Shuttle']),
    ('Daewoo', ['Damas', 'Espero', 'Evanda', 'Kalos', 'LE Mans', 'Lacetti', 'Lanos', 'Leganza', 'Magnus', 'Matiz', 'Nexia', 'Nubira', 'Prince', 'Racer', 'Rezzo', 'Tacuma', 'Tico']),
    ('Daihatsu', ['Altis', 'Applause', 'Atrai/extol', 'Be-go', 'Boon', 'Charade', 'Copen', 'Cuore', 'Esse', 'Feroza', 'Materia', 'Mira', 'Move', 'Pyzar', 'Rocky', 'Sirion', 'Storia', 'Terios', 'YRV']),
    ('Daimler', ['2.8 - 5.3', 'Limousine']),
    ('Derways', ['Aurora', 'Cowboy', 'Plutus', 'Shuttle']),
    ('Dodge', ['Avenger', 'Caliber', 'Caravan', 'Challenger', 'Charger', 'Dakota', 'Durango', 'Grand Caravan', 'Intrepid', 'Magnum', 'Neon', 'Nitro', 'RAM', 'Ramcharger', 'Shadow', 'Spirit', 'Stealth', 'Stratus', 'Viper']),
    ('Dong Feng', ['MPV']),
    ('Doninvest', ['Assol', 'Kondor', 'Orion']),
    ('Donkervoort', ['D8']),
    ('Eagle', ['Talon', 'Vision']),
    ('FAW', ['Admiral', 'Jinn', 'Vita']),
    ('Ferrari', ['360', '430', '599', '612 Scaglietti', 'California', 'Enzo', 'F355', 'Maranello', 'Mondial', 'Testarossa']),
    ('Fiat', ['131', 'Albea', 'Barchetta', 'Brava', 'Bravo', 'Cinquecento', 'Coupe', 'Croma', 'Doblo', 'Fiorino', 'Marea', 'Multipla', 'New 500', 'Palio', 'Panda', 'Punto', 'Regata', 'Ritmo', 'Sedici', 'Seicento', 'Stilo', 'Tempra', 'Tipo', 'UNO', 'Ulysse', 'X 1/9']),
    ('Ford', ['Aerostar', 'Bronco', 'C-MAX', 'Capri', 'Contour', 'Cougar', 'Crown Victoria', 'Econoline', 'Edge', 'Escape', 'Escort', 'Excursion', 'Expedition', 'Explorer', 'F-150', 'Fiesta', 'Fiesta ST', 'Five Hundred', 'Focus', 'Focus ST', 'Freestyle', 'Fusion', 'Fusion (USA)', 'GT', 'Galaxy', 'Granada', 'Granada (USA)', 'KA', 'Kuga', 'Maverick', 'Mondeo', 'Mustang', 'Orion', 'Probe', 'Puma', 'Ranger', 'S-MAX', 'Scorpio', 'Shelby', 'Sierra', 'Taunus', 'Taurus', 'Tempo', 'Thunderbird', 'Tourneo Connect', 'Windstar']),
    ('Geely', ['MK', 'Otaka']),
    ('Geo', ['Metro', 'Prizm', 'Storm', 'Tracker']),
    ('GMC', ['Acadia', 'Envoy', 'Jimmy', 'Safari', 'Savana', 'Sierra', 'Sonoma', 'Yukon', 'suburban']),
    ('Great Wall', ['Deer', 'Hover', 'SUV', 'Safe', 'Sailor', 'Socool', 'Wingle']),
    ('Hafei', ['Brio', 'Princip', 'Simbo']),
    ('Honda', ['Accord', 'Airwave', 'Avancier', 'CR-V', 'CRX', 'Capa', 'City', 'Civic', 'Civic Shuttle', 'Concerto', 'Domani', 'Edix', 'Element', 'FIT', 'FR-V', 'Fit Aria', 'Hr-v', 'Insight', 'Inspire', 'Integra', 'Jazz', 'Legend', 'Life', 'Logo', 'Mobilio', 'NSX', 'Odyssey', 'Orthia', 'Partner', 'Passport', 'Pilot', 'Prelude', 'Rafaga', 'Ridgeline', 'S2000', 'Saber', 'Shuttle', 'Sm-x', 'Stepwgn', 'Stream', 'Torneo', 'Vamos', 'Vigor', 'Z']),
    ('HuangHai', ['Antelope']),
    ('Hummer', ['Hummer', 'Hummer H1', 'Hummer H2', 'Hummer H3']),
    ('Hyundai', ['Accent', 'Atos', 'Coupe', 'Elantra', 'Galloper', 'Getz', 'Grandeur', 'H-1 Starex', 'H100', 'Lavita', 'Marcia', 'Matrix', 'NF', 'Pony', 'S-Coupe', 'Santa FE', 'Santamo', 'Sonata', 'Terracan', 'Tiburon', 'Trajet', 'Tucson', 'Tuscani', 'Veracruz', 'Verna', 'XG']),
    ('Infiniti', ['EX', 'FX 35', 'FX 45', 'FX 50', 'G35', 'G37', 'I30', 'I35', 'J30', 'M35', 'M45', 'Q45', 'QX4', 'QX56']),
    ('Iran Khodro', ['Samand']),
    ('Isuzu', ['Ascender', 'Aska', 'Axiom', 'Bighorn', 'Gemini', 'Impulse', 'Rodeo', 'Trooper', 'VehiCross', 'Wizard']),
    ('JAC', ['Refine', 'Rein']),
    ('Jaguar', ['E-type', 'S-type', 'X-type', 'XF', 'XJ', 'XJR', 'XJS Coupe', 'XJSc Convertible', 'XK 8', 'XKR']),
    ('Jeep', ['CJ5 - CJ8', 'Cherokee', 'Commander', 'Compass', 'Grand Cherokee', 'Liberty', 'Patriot', 'Wrangler']),
    ('Kia', ['Avella', 'Besta', 'Borrego', 'Capital', 'Carens', 'Carnival', 'Ceeu0026#039']),
    ('Koenigsegg', ['CC']),
    ('Lamborghini', ['Diablo', 'Espada', 'Gallardo', 'Murcielago']),
    ('Lancia', ['Beta', 'Dedra', 'Delta', 'Kappa', 'Lybra', 'Phedra', 'Thema', 'Thesis', 'Y']),
    ('Land Rover', ['90/110', 'Defender', 'Discovery', 'Freelander', 'Land Rover', 'Range Rover', 'Range Rover Sport']),
    ('Landwind', ['Double Gate', 'SUV']),
    ('Lexus', ['ES 300', 'ES 330', 'ES 350', 'GS 300', 'GS 350', 'GS 400', 'GS 430', 'GS 450h', 'GS 460', 'GX', 'IS 200', 'IS 250', 'IS 300', 'IS 350', 'IS-F', 'LS 400', 'LS 430', 'LS 460', 'LS 600', 'LX 450', 'LX 470', 'LX 570', 'RX 300', 'RX 330', 'RX 350', 'RX 400h', 'SC 300', 'SC 400', 'SC 430']),
    ('Lifan', ['Breez (520)']),
    ('Lincoln', ['Aviator', 'Continental', 'LS', 'MKX', 'MKZ', 'Mark', 'Mark LT', 'Navigator', 'Town Car', 'Zephyr']),
    ('Lotus', ['Elise', 'Exige', 'Super 7']),
    ('Mahindra', ['Marshal']),
    ('Maruti', ['Alto']),
    ('Maserati', ['228', '3200 GT', '4300 GT Coupe', 'Biturbo', 'Coupe', 'GranSport', 'GranTurismo', 'Quattroporte', 'Spyder']),
    ('Maybach', ['Maybach 57 S', 'Maybach 62 S', 'Maybach 57', 'Maybach 62']),
    ('Mazda', ['121', '323', '626', '929', 'Atenza', 'Axela', 'Az-wagon', 'B-serie', 'BT-50', 'Bongo', 'CX-7', 'CX-9', 'Capella', 'Carol', 'Demio', 'E 2000', '2200 Bus', 'Eunos 500', 'Eunos Cosmo', 'Familia', 'Lantis', 'Levante', 'Luce', 'MPV', 'Mazda 2', 'Mazda 3', 'Mazda 3 MPS', 'Mazda 5', 'Mazda 6', 'Mazda 6 MPS', 'Millenia', 'Mx-3', 'Mx-5', 'Mx-6', 'Premacy', 'Protege', 'RX 7', 'Roadster', 'Rx-8', 'Tribute', 'Verisa', 'Xedos 6', 'Xedos 9']),
    ('Mercedes-Benz', [' Cabrio', ' Coupe', ' T-mod.', '/8', '190', '200', '220', '230', '240', '250', '260', '280', '300', '500', 'A-klasse A 140', 'A-klasse A 150', 'A-klasse A 160', 'A-klasse A 170', 'A-klasse A 180', 'A-klasse A 190', 'A-klasse A 200', 'A-klasse A 210', 'B-klasse B 170', 'B-klasse B 180', 'B-klasse B 200', 'C-klasse C 180', 'C-klasse C 200', 'C-klasse C 220', 'C-klasse C 230', 'C-klasse C 240', 'C-klasse C 250', 'C-klasse C 270', 'C-klasse C 280', 'C-klasse C 32 AMG', 'C-klasse C 320', 'C-klasse C 350', 'C-klasse C 36 AMG', 'C-klasse C 55 AMG', 'C-klasse C 63 AMG', 'CL-Klasse CL 420', 'CL-Klasse CL 500', 'CL-Klasse CL 55 AMG', 'CL-Klasse CL 600', 'CL-Klasse CL 63 AMG', 'CL-Klasse CL 65 AMG', 'CLC-klasse CLC 220 CDI', 'CLK-klasse CLK 200', 'CLK-klasse CLK 220', 'CLK-klasse CLK 230', 'CLK-klasse CLK 240', 'CLK-klasse CLK 270', 'CLK-klasse CLK 320', 'CLK-klasse CLK 350', 'CLK-klasse CLK 430', 'CLK-klasse CLK 500', 'CLK-klasse CLK 55 AMG', 'CLK-klasse CLK 63 AMG', 'CLS-klasse CLS 320', 'CLS-klasse CLS 350', 'CLS-klasse CLS 500', 'CLS-klasse CLS 55 AMG', 'CLS-klasse CLS 63 AMG', 'E-klasse E 200', 'E-klasse E 220', 'E-klasse E 230', 'E-klasse E 240', 'E-klasse E 250', 'E-klasse E 270', 'E-klasse E 280', 'E-klasse E 290', 'E-klasse E 300', 'E-klasse E 320', 'E-klasse E 350', 'E-klasse E 400', 'E-klasse E 420', 'E-klasse E 430', 'E-klasse E 50 AMG', 'E-klasse E 500', 'E-klasse E 55 AMG', 'E-klasse E 63 AMG', 'G-Klasse G 230', 'G-Klasse G 250', 'G-Klasse G 270', 'G-Klasse G 280', 'G-Klasse G 290', 'G-Klasse G 300', 'G-Klasse G 320', 'G-Klasse G 350', 'G-Klasse G 400', 'G-Klasse G 500', 'G-Klasse G 55 AMG', 'GL-klasse GL 320', 'GL-klasse GL 420', 'GL-klasse GL 450', 'GL-klasse GL 500', 'GL-klasse GL 550', 'M-klasse ML 230', 'M-klasse ML 270', 'M-klasse ML 280', 'M-klasse ML 320', 'M-klasse ML 350', 'M-klasse ML 400', 'M-klasse ML 430', 'M-klasse ML 500', 'M-klasse ML 55 AMG', 'M-klasse ML 63 AMG', 'Pullmann', 'R-klasse', 'R-klasse R 320', 'R-klasse R 350', 'R-klasse R 500', 'S-klasse S 260', 'S-klasse S 280', 'S-klasse S 300', 'S-klasse S 320', 'S-klasse S 350', 'S-klasse S 380', 'S-klasse S 400', 'S-klasse S 420', 'S-klasse S 430', 'S-klasse S 450', 'S-klasse S 500', 'S-klasse S 55 AMG', 'S-klasse S 550', 'S-klasse S 560', 'S-klasse S 600', 'S-klasse S 65 AMG', 'SL-klasse SL 280', 'SL-klasse SL 300', 'SL-klasse SL 320', 'SL-klasse SL 350', 'SL-klasse SL 380', 'SL-klasse SL 420', 'SL-klasse SL 450', 'SL-klasse SL 500', 'SL-klasse SL 55 AMG', 'SL-klasse SL 600', 'SL-klasse SL 63 AMG', 'SL-klasse SL 65 AMG', 'SLK-klasse SLK 200', 'SLK-klasse SLK 230', 'SLK-klasse SLK 280', 'SLK-klasse SLK 32 AMG', 'SLK-klasse SLK 320', 'SLK-klasse SLK 350', 'SLK-klasse SLK 55 AMG', 'SLR McLaren', 'V-klasse V 200', 'V-klasse V 220', 'V-klasse V 230', 'V-klasse V 280', 'Vaneo', 'Viano']),
    ('Mercury', ['Capri', 'Cougar', 'Grand Marquis', 'Mariner', 'Montego', 'Mountaineer', 'Mystique', 'Sable', 'Topaz', 'Tracer', 'Villager']),
    ('Metrocab', ['Taxi  (II -series)']),
    ('MG', ['MGB', 'MGF', 'TF', 'ZR', 'ZT']),
    ('Microcar', ['MC1']),
    ('Mini', ['Clubman', 'Cooper', 'One']),
    ('Mitsubishi', ['3000 GT', 'Airtrek', 'Aspire', 'Carisma', 'Challenger', 'Chariot', 'Colt', 'Debonair', 'Delica', 'Diamante', 'Dingo', 'Dion', 'EK Wagon', 'Eclipse', 'Emeraude', 'Endeavor', 'FTO', 'GTO', 'Galant', 'Grandis', 'L 200', 'Lancer', 'Lancer', 'Lancer Cedia', 'Lancer Evolution', 'Legnum', 'Libero', 'Minica', 'Mirage', 'Montero', 'Montero Sport', 'Outlander', 'Pajero', 'Pajero Sport', 'RVR', 'Sapporo', 'Sigma', 'Space Gear', 'Space Runner', 'Space Star', 'Space Wagon', 'Starion', 'Town BOX', 'i']),
    ('Mitsuoka', ['Galue', 'Le-Sayde', 'Le-Seyde']),
    ('Morgan', ['Aero 8']),
    ('Nissan', ['100 NX', '200 SX', '300 ZX', '350Z', 'AD', 'Almera', 'Almera Classic', 'Almera Tino', 'Altima', 'Armada', 'Avenir', 'Bassara', 'Bluebird', 'Cedric', 'Cefiro', 'Cherry', 'Cima', 'Cube', 'Datsun', 'Elgrand', 'Expert', 'Fairlady', 'Frontier', 'Fuga', 'GT-R', 'Gloria', 'King Cab', 'Lafesta', 'Largo', 'Laurel', 'Leopard', 'Liberty', 'Lucino', 'March', 'Maxima', 'Micra', 'Mistral', 'Moco', 'Murano', 'Navara', 'Note', 'Pathfinder', 'Patrol', 'Pick UP', 'Prairie', 'Presage', 'Presea', 'Primera', 'Pulsar', 'Qashqai', 'Quest', 'R Nessa', 'Rasheen', 'Rogue', 'Safari', 'Sentra', 'Serena', 'Silvia', 'Skyline', 'Stagea', 'Stanza', 'Sunny', 'Teana', 'Terrano', 'Tiida', 'Tino', 'Titan', 'Urvan', 'Vanette', 'Wingroad', 'X-Terra', 'X-Trail']),
    ('Oldsmobile', ['Achieva', 'Alero', 'Aurora', 'Bravada', 'Cutlass', 'Silhouette']),
    ('Opel', ['Agila', 'Antara', 'Ascona', 'Astra', 'Astra OPC', 'Calibra', 'Campo', 'Combo', 'Commodore', 'Corsa', 'Corsa OPC', 'Frontera', 'GT', 'Kadett', 'Manta', 'Meriva', 'Monterey', 'Movano', 'Omega', 'Rekord', 'Senator', 'Signum', 'Sintra', 'Speedster', 'Tigra', 'Vectra', 'Vita', 'Zafira']),
    ('Pagani', ['Zonda C12']),
    ('Peugeot', ['106', '107', '205', '206', '207', '305', '306', '307', '308', '309', '405', '406', '407', '605', '607', '806', '807', '1007', '4007']),
    ('Plymouth', ['Acclaim', 'Breeze', 'Grand Voyager', 'Laser', 'Neon', 'Prowler', 'Sundance', 'Voyager']),
    ('Pontiac', ['6000', 'Aztec', 'Bonneville', 'Firebird', 'GTO', 'Grand AM', 'Grand Prix', 'Phoenix', 'Solstige', 'Sunbird', 'Sunfire', 'Trans Sport', 'Vibe']),
    ('Porsche', ['911', '924', '928', '944', '968', 'Boxster', 'Carrera GT', 'Cayenne', 'Cayman']),
    ('Proton', ['Persona 300 Compact', 'Persona 400']),
    ('PUCH', ['G-modell', 'Pinzgauer']),
    ('Renault', ['5', '9', '11', '18', '19', '20', '21', '25', 'Avantime', 'Clio', 'Clio Symbol', 'Espace', 'Fuego', 'Grand Scenic', 'Kangoo Express', 'Kangoo Passenger', 'Laguna', 'Logan', 'Master', 'Megane', 'Modus', 'Rapid', 'Safrane', 'Scenic', 'Scenic RX', 'Super 5', 'Symbol', 'Trafic', 'Twingo', 'Vel Satis']),
    ('Rolls-Royce', ['Corniche Cabrio', 'Phantom', 'Phantom Drophead Coupe', 'Silver Seraph', 'Silver Spur']),
    ('Rover', ['25', '45', '75', '200', '400', '600', '800', 'Maestro', 'Mini MK', 'Montego']),
    ('Saab', ['9-2X', '9-3', '9-5', '9-7X', '99', '900', '9000']),
    ('Saleen', ['S7']),
    ('Saturn', ['ION', 'LS', 'SC', 'SL', 'VUE']),
    ('Scion', ['tC', 'xA', 'xB']),
    ('SEAT', ['Alhambra', 'Altea', 'Arosa', 'Cordoba', 'Ibiza', 'Leon', 'Malaga', 'Ronda', 'Toledo']),
    ('ShuangHuan', ['Sceo']),
    ('Skoda', ['Fabia', 'Favorit', 'Felicia', 'Octavia', 'Octavia Scout', 'Roomster', 'Superb']),
    ('Smart', ['Crossblade', 'Forfour', 'Fortwo', 'Roadster']),
    ('Spyker', ['C8']),
    ('SsangYong', ['Actyon', 'Chairman', 'Family', 'Istana', 'Korando', 'Kyron', 'Musso', 'Rexton', 'Rodius', 'Tager']),
    ('Subaru', ['Baja', 'Forester', 'Impreza', 'Impreza WRX', 'Justy', 'Legacy', 'Leone', 'Libero', 'Outback', 'Pleo', 'R2', 'SVX', 'Stella', 'Traviq', 'Tribeca', 'Vivio', 'XT']),
    ('Suzuki', ['Aerio', 'Alto', 'Baleno', 'Cultus Wagon', 'Escudo', 'Every', 'Every Landy', 'Forenza', 'Grand Vitara', 'Ignis', 'Jimny', 'Kei', 'Liana', 'MR Wagon', 'SX4', 'Samurai', 'Sidekick', 'Swift', 'Verona', 'Vitara', 'Wagon R+', 'X-90', 'XL7']),
    ('Tatra', ['T613']),
    ('Tianma', ['Century']),
    ('Tianye', ['Admiral']),
    ('Toyota', ['4runner', 'Allex', 'Allion', 'Alphard', 'Altezza', 'Aristo', 'Aurion', 'Auris', 'Avalon', 'Avensis', 'Avensis Verso', 'BB', 'Brevis', 'Caldina', 'Cami', 'Camry', 'Camry Solara', 'Carib', 'Carina', 'Carina E', 'Carina ED', 'Cavalier', 'Celica', 'Chaser', 'Corolla', 'Corolla', 'Corolla Ceres', 'Corolla FX', 'Corolla Fielder', 'Corolla Levin', 'Corolla Rumion', 'Corolla RunX', 'Corolla Spacio', 'Corolla Verso', 'Corona', 'Corsa', 'Cressida', 'Cresta', 'Crown', 'Crown', 'Crown Athlete', 'Crown Majesta', 'Curren', 'Cynos', 'Duet', 'Echo', 'Estima', 'FJ Cruiser', 'Fortuner', 'Funcargo', 'Gaia', 'Grand Hiace', 'Granvia', 'Harrier', 'Hiace', 'Highlander', 'Hilux Pick Up', 'Hilux Surf', 'ISis', 'Ipsum', 'Ist', 'Kluger', 'Land Cruiser', 'Land Cruiser (120) Prado', 'Land Cruiser (90) Prado', 'Land Cruiser 100', 'Land Cruiser 200', 'Land Cruiser 70', 'Land Cruiser 80', 'Lite Ace', 'MR 2', 'MR-S', 'Mark II', 'Mark X', 'MasterAce', 'Matrix', 'Nadia', 'Noah', 'Opa', 'Origin', 'Paseo', 'Passo', 'Picnic', 'Platz', 'Porte', 'Premio', 'Previa', 'Prius', 'Probox', 'Progres', 'Pronard', 'RAV 4', 'Ractis', 'Raum', 'Regius', 'Regius', 'Regius Ace', 'Scepter', 'Sequoia', 'Sera', 'Sienna', 'Sienta', 'Soarer', 'Solara', 'Sparky', 'Sprinter', 'Starlet', 'Succeed', 'Supra', 'Tacoma', 'Tercel', 'Tundra', 'Vellfire', 'Venza', 'Verossa', 'Vista', 'Vitz', 'Voltz', 'Voxy', 'Will', 'Windom', 'Wish', 'Yaris', 'Yaris Verso']),
    ('Trabant', ['P 601']),
    ('TVR', ['Griffith']),
    ('Vector', ['W8 Twin Turbo']),
    ('Volkswagen', ['Bora', 'Caddy', 'Corrado', 'Eos', 'Fox', 'Golf', 'Golf Plus', 'Jetta', 'Kaefer', 'Lupo', 'Multivan', 'NEW Beetle', 'Passat', 'Phaeton', 'Pointer', 'Polo', 'Santana', 'Scirocco', 'Sharan', 'Taro', 'Tiguan', 'Touareg', 'Touran', 'Vento']),
    ('Volvo', ['164', '240', '340-360', '440 K', '460 L', '480 E', '740', '760', '780 Bertone', '850', '940', '960', 'C30', 'C70', 'S40', 'S60', 'S70', 'S80', 'S90', 'V40 Kombi', 'V50', 'V70', 'XC70', 'XC90']),
    ('Wartburg', ['353']),
    ('Wiesmann', ['GT', 'Roadster']),
    ('Xin Kai', ['PICKUP X3', 'SR-V X3', 'SUV X3']),
    ('ZX', ['GrandTiger', 'Landmark']),
    ('ВАЗ', ['1111 Ока 1111', '1111 Ока 11113', '2101', '2102', '2103', '2104', '2105', '2106', '2107', '2108', '2109', '2110', '2111', '2112', '2113', '2114', '2115', '2123', '2129', '2131', '2329', '21043', '21047', '21053', '21054', '21055', '21061', '21063', '21065', '21071', '21072', '21073', '21074', '21079', '21081', '21083', '21086', '2108i', '21093', '21099', '21099i', '2109i', '21101', '21102', '21103', '21104', '21108', '21111', '21112', '21113', '21121', '21122', '21123', '21124', '2115 Wankel', '2115i', '2120 Надежда', '2121 4x4 2121', '2121 4x4 21213', '2121 4x4 21214', '2121 4x4 21217', '2121 4x4 21218', 'Kalina Hatchback', 'Kalina Sedan', 'Kalina Wagon', 'Priora']),
    ('Велта', ['Автокам']),
    ('ГАЗ', ['13', '14', '20', '21', '22', '24', '69', '3102', '3105', '3110', '3111', '31022', '31026', '31029', '3102i', '31105', '310221', '311055', '3110i', 'c1']),
    ('ЗАЗ', ['965', '968', '1102', '1103', '1105', '1140', 'Sens']),
    ('ЗИЛ', ['114', '117', '4104']),
    ('ИЖ', ['412', '2125', '2126', '2715', '2717', '21261', '27171']),
    ('КАМАЗ', ['Ока']),
    ('ЛУАЗ', ['967', '968', '969']),
    ('Москвич', ['400', '401', '402', '403', '406', '407', '408', '412', '2125', '2140', '2141', '2335', '423 Kombi', '5846', 'Aslk 2137 Kombi', 'Aslk 2138', 'Aslk 2140', 'Князь Владимир', 'Святогор', 'Юрий Долгорукий']),
    ('СеАЗ', ['1111']),
    ('СМЗ', ['Мотоколяска']),
    ('ТагАЗ', ['Tager']),
    ('УАЗ', ['469', '2206', '3151', '3153', '3159', '3160', '3162', '3163', '31512', '31514', '31519', '315195']),
)


def add_data(apps, schema_editor):
    TsMark = apps.get_model("cards", "TsMark")
    TsModel = apps.get_model("cards", "TsModel")

    for data in SOURCE_DATA:
        mark = TsMark.objects.get(name=data[0])
        for ts_model in data[1]:
            TsModel.objects.create(mark=mark, name=ts_model)



class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0023_tsmodel'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]