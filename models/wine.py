from collections import namedtuple
import collections
from services import mysql

# Taster class
Taster = namedtuple('Taster', ['name', 'twitter'])


class Wine:
    def __init__(self, points, title, variety, description, country, province, region1, region2,
                 winery, designation, price, taster_twitter, taster_name):
        self.id = 0
        # the number of points WineEnthusiast rated the wine on a scale of 1-100
        # (though they say they only post reviews for wines that score >=80)
        if points is None:
            self.points = 0
        else:
            self.points = points
        # the title of the wine review, which often contains the vintage if you're interested in extracting that feature
        if title is None:
            self.title = ""
        else:
            self.title = title
        # the type of grapes used to make the wine (ie Pinot Noir)
        if variety is None:
            self.variety = ""
        else:
            self.variety = variety
        # a few sentences from a sommelier describing the wine's taste, smell, look, feel, etc.
        if description is None:
            self.description = ""
        else:
            self.description = description
        # the country that the wine is from
        if country is None:
            self.country = ""
        else:
            self.country = country
        # the province or state that the wine is from
        if province is None:
            self.province = ""
        else:
            self.province = province
        # the wine growing area in a province or state (ie Napa)
        if region1 is None:
            self.region1 = ""
        else:
            self.region1 = region1
        # sometimes there are more specific regions specified within a wine growing area
        # (ie Rutherford inside the Napa Valley), but this value can sometimes be blank
        if region2 is None:
            self.region2 = ""
        else:
            self.region2 = region2
        # the winery that made the wine
        if winery is None:
            self.winery = ""
        else:
            self.winery = winery
        # the vineyard within the winery where the grapes that made the wine are from
        if designation is None:
            self.designation = ""
        else:
            self.designation = designation
        # the cost for a bottle of the wine
        if price is None:
            self.price = 0
        else:
            self.price = price
        # name of the person who tasted and reviewed the wine
        # Twitter handle for the person who tasted and reviewed the wine
        if taster_twitter is None:
            taster_twitter = ""
        if taster_name is None:
            taster_name = ""
        self.taster = Taster(name=taster_name, twitter=taster_twitter)

    def set_id(self, newid):
        self.id = newid
