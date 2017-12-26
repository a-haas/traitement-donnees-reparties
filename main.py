import json
from models import wine

ressources_dir = "wine-reviews/"
with open(ressources_dir+'winemag-data-130k-v2.json') as data_file:
    data = json.load(data_file)

reviews = []
for wine_review in data:
    reviews.append(wine.Wine(
        wine_review["points"], wine_review["title"], wine_review["variety"], wine_review["description"],
        wine_review["country"], wine_review["province"], wine_review["region_1"], wine_review["region_2"], wine_review["winery"],
        wine_review["designation"], wine_review["price"], wine_review["taster_twitter_handle"], wine_review["taster_name"]
    ))