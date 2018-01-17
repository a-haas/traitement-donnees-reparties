#!/usr/bin/python
import MySQLdb


# Configuration de l'accès à la base de données
def config_db():
    return MySQLdb.connect(host="localhost",  # your host, usually localhost
                           user="tdr",  # your username
                           passwd="tdr",  # your password
                           db="wine-review",
                           use_unicode=True,
                           charset="utf8")  # name of the data base


def query_db(query, f=lambda x: x):
    """
    :param query str La requête a exécutée
    :param f function Une fonction qui va traiter le résultat de la requête
    :return Le résultat de la fonction f
    """
    db = config_db()
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()
    # Use all the SQL you like
    cur.execute(query)
    # fetch the results
    res = cur.fetchall()
    fresult = f(res)
    db.commit()
    db.close()
    return fresult
