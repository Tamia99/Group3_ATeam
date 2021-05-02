import config
import pymysql
conn = pymysql.connect(host=config.HOST, user=config.USERNAME, password=config.PASSWORD, port=config.PORT,
                       db=config.DATABASE)
def test():
    cursor = conn.cursor()
    cursor.execute("INSERT INTO article(title,content) VALUES('999','jjjj')")
    conn.commit()
    cursor.close()
def getAllHouses():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM House")
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

