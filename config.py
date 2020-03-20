
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
