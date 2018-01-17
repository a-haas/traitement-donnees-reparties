from services import utilities
from services import mysql
from models import wine
import collections


WINE_TABLE = 1
TASTER_TABLE = 2


def insert(reviews):
    if not isinstance(reviews, collections.Iterable):
        reviews = [reviews]
    wines = []
    tasters = {}
    # define the query
    for w in reviews:
        wines.append("("+parse_str(w.points)+",'"+parse_str(w.title)+"','"+parse_str(w.variety)+"','"
                     +parse_str(w.description)+"','"+parse_str(w.country)+"','"+parse_str(w.province)+"','"
                     +parse_str(w.region1)+"','"+parse_str(w.region2)+"','"+parse_str(w.winery)+"','"
                     +parse_str(w.designation)+"',"+ parse_str(w.price)+",'"+parse_str(w.taster.twitter)+"')")
        if w.taster.twitter is not None:
            tasters[w.taster.twitter] = "('"+parse_str(w.taster.twitter)+"','"+parse_str(w.taster.name)+"')"
    wines_queries = []
    # split the query in multiple part to prevent the query to be too big
    for subwines in utilities.split_list(wines, int(utilities.byte_size(wines)/1048576) ):  # 1048576 is the default size of mysql query
        wines_query = "INSERT INTO Wines(points, title, variety, description, country, province, region1, region2, " \
                      "winery, designation, price, taster_twitter) VALUES"+ ",".join(subwines) + ";"
        wines_queries.append(wines_query)
    tasters_query = "INSERT INTO Tasters(twitter, name) VALUES" + ",".join(str(x) for x in tasters.values())\
                    +" ON DUPLICATE KEY UPDATE name=name;"
    # execute the queries
    mysql.query_db(tasters_query)
    for wines_query in wines_queries:
        mysql.query_db(wines_query)


def insert_1by1(reviews):
    if not isinstance(reviews, collections.Iterable):
        reviews = [reviews]
    for r in reviews:
        insert(r)


def getall():
    reviews = []
    query = "SELECT id, points, title,variety, description, country, province, region1, region2, winery, " \
            "designation, price, twitter, name " \
            "FROM Wines LEFT JOIN Tasters ON twitter = taster_twitter"
    raw_reviews = mysql.query_db(query)
    for raw in raw_reviews:
        w = wine.Wine(raw[1], raw[2], raw[3], raw[4], raw[5], raw[6], raw[7], raw[8], raw[9], raw[10]
                      , raw[11], raw[12], raw[13])
        w.set_id(raw[0])
        reviews.append(w)
    return reviews

def update(reviews):
    if not isinstance(reviews, collections.Iterable):
        reviews = [reviews]
    wines = []
    tasters = {}
    # define the query
    for wine in reviews:
        wines.append("SET points="+parse_str(wine.points)+",variety='"+parse_str(wine.variety)+"',description='"+parse_str(wine.description)+"',country='"
                     +parse_str(wine.country)+"',province='"+parse_str(wine.province)+"',region1='"+parse_str(wine.region1)+"',region2='"
                     +parse_str(wine.region2)+"',winery='"+parse_str(wine.winery)+"',designation='"
                     +parse_str(wine.designation)+"',price="+ parse_str(wine.price)+",taster_twitter='"+parse_str(wine.taster.twitter)
                     +"' WHERE id="+parse_str(wine.id))
    wines_queries = []
    # split the query in multiple part to prevent the query to be too big
    for subwines in utilities.split_list(wines, int(utilities.byte_size(wines)/1048576) ):  # 1048576 is the default size of mysql query
        for w in subwines:
            wines_query = "UPDATE Wines "+ w + ";"
            mysql.query_db(wines_query)


def delete(table_id, ids):
    tablename = {
        1: "Wines",
        2: "Tasters",
    }[table_id]
    parsed_ids = map(lambda x : parse_str(x), ids)
    query = "DELETE FROM "+tablename+" WHERE id IN ("+",".join(parsed_ids)+");"
    mysql.query_db(query)


def get(q):
    return mysql.query_db(q)


def parse_str(s):
    return str(s).replace("'", "\\'")
