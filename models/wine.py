from collections import namedtuple

# Taster class
Taster = namedtuple('Taster', ['name', 'twitter'])

class Wine:
    def __init__(self, points, title, variety, description, country, province, region1, region2,
                 winery, designation, price, taster_name, taster_twitter):
        #the number of points WineEnthusiast rated the wine on a scale of 1-100 (though they say they only post reviews for wines that score >=80)
        self.points = points
        # the title of the wine review, which often contains the vintage if you're interested in extracting that feature
        self.title = title
        #the type of grapes used to make the wine (ie Pinot Noir)
        self.variety = variety
        #a few sentences from a sommelier describing the wine's taste, smell, look, feel, etc.
        self.description = description
        #the country that the wine is from
        self.country = country
        #the province or state that the wine is from
        self.province = province
        #the wine growing area in a province or state (ie Napa)
        self.region1 = region1
        #sometimes there are more specific regions specified within a wine growing area (ie Rutherford inside the Napa Valley), but this value can sometimes be blank
        self.region2 = region2
        #the winery that made the wine
        self.winery = winery
        #the vineyard within the winery where the grapes that made the wine are from
        self.designation = designation
        #the cost for a bottle of the wine
        self.price = price
        #name of the person who tasted and reviewed the wine
        #Twitter handle for the person who tasted and reviewed the wine
        self.taster = Taster(name=taster_name, twitter=taster_twitter)
