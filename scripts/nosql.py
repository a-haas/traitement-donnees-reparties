from services import elasticsearch
from models import wine
import collections
import json


def insert_1by1(reviews):
    if not isinstance(reviews, collections.Iterable):
        reviews = [reviews]
    for r in reviews:
        # On traite les vins
        w = {
            "points": r.points,
            "title": r.title,
            "variety": r.variety,
            "description": r.description,
            "country": r.country,
            "province": r.province,
            "region1": r.region1,
            "region2": r.region2,
            "winery": r.winery,
            "designation": r.designation,
            "price": r.price,
            "taster": {"twitter": r.taster.twitter, "name": r.taster.name}
        }
        json_wine = json.dumps(w)
        elasticsearch.create("wine", json_wine)


def insert(reviews):
    if not isinstance(reviews, collections.Iterable):
        reviews = [reviews]
    json_wines = []
    for r in reviews:
        # On traite les vins
        w = {
            "points": r.points,
            "title": r.title,
            "variety": r.variety,
            "description": r.description,
            "country": r.country,
            "province": r.province,
            "region1": r.region1,
            "region2": r.region2,
            "winery": r.winery,
            "designation": r.designation,
            "price": r.price,
            "taster": {"twitter": r.taster.twitter, "name": r.taster.name}
        }
        json_wines.append(json.dumps(w))
    elasticsearch.bulk_insert("wine", json_wines)


def getall():
    r = elasticsearch.retrieve_all("wine", {"match_all": {}})
    return r


def get(query):
    r = elasticsearch.search("wine", query)
    return r

def delete_all():
    elasticsearch.delete_by_query("wine", {"match_all": {}})


def count_all():
    c = elasticsearch.count("wine", {"match_all": {}})
    print(c)