
import os


class Config:
    AUS_STATE = [
        ('New South Wales', 'NSW'),
        ('Victoria', 'VIC'),
        ('Queensland', 'QLD'),
        ('Western Australia', 'WA'),
        ('Tasmania', 'TAS'),
        ('Northern Territory', 'NT'),
        ('Australian Capital Territory', 'ACT'),
    ]

    STATUS = [('confirmed', 'confirmed'),
              ('death', 'death'),
              ('recover', 'recover')]

    DATA_BASE_PATH = os.getenv('DATA_BASE_PATH', '/Users/wangjing/github/corona/corona-au')

    OZ_STATES = [{'state': 'New South Wales', 'pop': 7317500, 'beds': 28391},
                 {'state': 'Victoria', 'pop': 5640900, 'beds': 20025},
                 {'state': 'Queensland', 'pop': 4599400, 'beds': 17063},
                 {'state': 'Western Australia', 'pop': 2366900, 'beds': 8449},
                 {'state': 'South Australia', 'pop': 1659800, 'beds': 6556},
                 {'state': 'Tasmania', 'pop': 511000, 'beds': 2008},
                 {'state': 'Australian Capital Territory', 'pop': 366900, 'beds': 1441},
                 {'state': 'Northern Territory', 'pop': 231200, 'beds': 908},
                 {'state': 'Australia', 'pop': 2412000, 'beds': 91683},
                 ]
