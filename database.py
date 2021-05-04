import config
import pymysql

conn = pymysql.connect(host=config.HOST, user=config.USERNAME, password=config.PASSWORD, port=config.PORT,
                       db=config.DATABASE)


def test():
    cursor = conn.cursor()
    cursor.execute("INSERT INTO article(title,content) VALUES('999','jjjj')")
    conn.commit()
    cursor.close()


def getAllHouses(n,m):
    cursor = conn.cursor()
    match = ""
    if len(m) != 0:
        match = "WHERE "
        for word in m:
            if word == m[-1] :
                match += "Neighborhood = '" + word + "'"
            else:
                match += "Neighborhood = '" + word + "' OR "

    #WHERE Neighborhood = 'Blmngtn' OR Neighborhood = 'CollgCr'
    print("match =", match)
    if n == 9:
        cursor.execute("SELECT * FROM House " + match + " ORDER BY Neighborhood")
    elif n==8:
        cursor.execute("SELECT * FROM House " + match + " ORDER BY FullBath+0.5*HalfBath")
    elif n == 7:
        cursor.execute("SELECT * FROM House " + match + " ORDER BY BedroomAbvGr")
    elif n == 6:
        cursor.execute("SELECT * FROM House " + match + " ORDER BY LotArea")
    elif n == 5:
        cursor.execute("SELECT * FROM House " + match + " ORDER BY SalePrice")
    elif n == 4:
        cursor.execute("SELECT * FROM House " + match + " ORDER BY FullBath+0.5*HalfBath DESC ")
    elif n == 3:
        cursor.execute("SELECT * FROM House " + match + " ORDER BY BedroomAbvGr DESC ")
    elif n == 2:
        cursor.execute("SELECT * FROM House " + match + " ORDER BY LotArea DESC ")
    elif n == 1:
        cursor.execute("SELECT * FROM House " + match + " ORDER BY SalePrice DESC ")
    else:
        cursor.execute("SELECT * FROM House " + match )
    houses = cursor.fetchall()
    conn.commit()
    cursor.close()
    return houses


def getAllRecommendations():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Recommendation")
    recommendations = cursor.fetchall()
    conn.commit()
    cursor.close()
    return recommendations


def getHouseByIds(ids):
    cursor = conn.cursor()
    result = []
    for i in ids:
        statement = "SELECT * FROM House WHERE id = " + i
        cursor.execute(statement)
        result.append(list(cursor.fetchone()))
    conn.commit()
    cursor.close()
    return result
