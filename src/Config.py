HERO_CLASSES = ['Druid']#, 'Hunter', 'Mage', 'Paladin', 'Priest', 'Rogue', 'Shaman', 'Warlock', 'Warrior']

CARD_SETS = ['Basic', 'Expert']

CARDS_TO_IGNORE = ['CS2_013t', 'EX1_573t', 'EX1_158t', 'EX1_160t', 'CS2_017', 'EX1_165t2', 'EX1_165t1',
                    'CS2_034', 'tt_010a', 'CS2_mirror', 'EX1_323h', 'EX1_317t', 'EX1-tk33', 'CS2_102',
                    'CS2_056', 'EX1_323w', 'EX1_554t', 'EX1_538t', 'EX1_534t', 'DS1h_292', 'NEW1_034', 
                    'NEW1_033', 'NEW1_032', 'EX1_345t', 'CS1h_001', 'EX1_625t2', 'EX1_625t', 'EX1_130a', 
                    'CS2_101t', 'CS2_101', 'EX1_383t', 'NEW1_006', 'EX1_131t', 'CS2_082', 'CS2_083b',
                    'EX1_tk9', 'EX1_tk33', 'EX1_tk34', 'NEW1_009', 'CS2_050', 'CS2_051', 'CS2_052',
                    'EX1_tk11', 'CS2_049', 'EX1_398t', 'EX1_409t'
                    ]
                    
#Cards and Pages
MAX_CARD_LABELS_PER_ROW = 4
MAX_ROWS_PER_PAGE = 2
MAX_CARD_LABELS_PER_PAGE = MAX_CARD_LABELS_PER_ROW*MAX_ROWS_PER_PAGE
MAX_PAGES = 4
MAX_CARDS_IN_DECK = 30

#Dimensions
CARD_LABEL_WIDTH = 200
CARD_LABEL_HEIGHT = 304

#Paths
DECK_PATH = '..\decks'
JSON_PATH = '..\json'
IMAGES_URL = r'http://wow.zamimg.com/images/hearthstone/cards/enus/original'