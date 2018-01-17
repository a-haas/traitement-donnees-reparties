import json
import argparse
import random
from models import wine
from scripts import sql
from scripts import tables
from scripts import nosql
from scripts import indexes
from services import utilities


# parsing des arguments
parser = argparse.ArgumentParser("tdr")
# file to use
parser.add_argument("filename", help="Le fichier de données", type=str)
parser.add_argument("db", help="Le système de gestion des données à utiliser SQL|NOSQL")
parser.add_argument("method", help="La méthode à tester et à mesurer INSERT|UPDATE|GET|DELETE")
parser.add_argument("-s", help="Le nombre de lignes du fichier de données à utiliser", type=int)
parser.add_argument("--size", help="Le nombre de lignes du fichier de données à utiliser", type=int)
parser.add_argument("-q", help="Lors d'un GET il est nécessaire de fournir une requête")
parser.add_argument("--query", help="Lors d'un GET il est nécessaire de fournir une requête")
args = parser.parse_args()

query_type = args.q or args.query or ""
if args.method.lower() == 'get' and query_type == "":
    print("Merci de préciser l'option -q ou --query lorsque la méthode GET est sélectionnée")
    exit()

with open(args.filename) as data_file:
    data = json.load(data_file)

reviews = []
for wine_review in data:
    reviews.append(wine.Wine(
        wine_review["points"], wine_review["title"], wine_review["variety"], wine_review["description"],
        wine_review["country"], wine_review["province"], wine_review["region_1"], wine_review["region_2"], wine_review["winery"],
        wine_review["designation"], wine_review["price"], wine_review["taster_twitter_handle"], wine_review["taster_name"]
    ))

size = args.s or args.size or len(reviews)
reviews = reviews[:size]
# randomise
# if args.method.lower() == 'update':
#
query = ""
sql_query = ""
if args.method.lower() == "get":
    if args.db.lower() == "nosql":
        query = json.loads(query_type)
    else:
        sql_query = query_type

# start the chrono
st_real, st_ps = utilities.chrono()
if args.db.lower() == 'sql':
    if args.method.lower() == 'insert':
        sql.insert_1by1(reviews)
    elif args.method.lower() == 'bulk':
        sql.insert(reviews)
    elif args.method.lower() == 'update':
        sql.update(reviews)
    elif args.method.lower() == 'getall':
        r = sql.getall()
        print("Retrieved "+str(len(r))+" rows")
    elif args.method.lower() == 'get':
        r = sql.get(sql_query)
    elif args.method.lower() == 'reset':
        tables.drop()
        tables.create()
elif args.db.lower() == 'nosql':
    if args.method.lower() == 'bulk':
        nosql.insert(reviews)
    if args.method.lower() == 'insert':
        nosql.insert_1by1(reviews)
    # elif args.method is 'update':
    elif args.method.lower() == 'count':
        nosql.count_all()
    elif args.method.lower() == 'getall':
        r = nosql.getall()
        print("Retrieved " + str(len(r)) + " rows")
    elif args.method.lower() == 'get':
        r = nosql.get(query)
    elif args.method.lower() == 'reset':
        indexes.reset()
        indexes.create()
    elif args.method.lower() == 'optimise':
        indexes.optimise()
# print time elapsed (process and real)
t_real, t_ps = utilities.end_chrono(st_real, st_ps)
print('Elapsed time in seconds : '+str(t_real))
print('Elapsed time for process : '+str(t_ps))
