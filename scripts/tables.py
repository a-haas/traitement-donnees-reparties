from services import mysql


def create():
    # First create the database
    tasters_query = "CREATE TABLE Tasters(" \
                    "twitter VARCHAR(50) NOT NULL UNIQUE, " \
                    "name VARCHAR(100), " \
                    "PRIMARY KEY (twitter));"

    wines_query = "CREATE TABLE Wines(" \
                    "id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY," \
                    "points INT(6) UNSIGNED," \
                    "title VARCHAR(300)," \
                    "variety VARCHAR(100)," \
                    "description VARCHAR(1000)," \
                    "country VARCHAR(50)," \
                    "province VARCHAR(50)," \
                    "region1 VARCHAR(50)," \
                    "region2 VARCHAR(50)," \
                    "winery VARCHAR(300)," \
                    "designation VARCHAR(100)," \
                    "price INT(6) UNSIGNED," \
                    "taster_twitter VARCHAR(50)," \
                    "FOREIGN KEY (taster_twitter) REFERENCES Tasters(twitter)" \
                    ");"
    mysql.query_db(tasters_query)
    mysql.query_db(wines_query)


def drop():
    tasters_query = "DROP TABLE Tasters;"
    wines_query = "DROP TABLE Wines;"
    mysql.query_db(wines_query)
    mysql.query_db(tasters_query)
