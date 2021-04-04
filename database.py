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

# class mysqlConnect:
#     def __init__(self):
#         self.conn = self.to_connect()
#
#     def __del__(self):
#         self.conn.close()
#
#     def to_connect(self):
#         return pymysql.connect(host=config.HOST, user=config.USERNAME, password=config.PASSWORD, port=config.PORT, db=config.DATABASE)
#
#     def is_connected(self):
#         """Check if the server is alive"""
#         try:
#             self.connection.ping()
#         except:
#             self.connection()
#
#     def test(self):
#         cursor = self.conn.cursor()
#         cursor.execute("INSERT INTO article(title,content) VALUES('999','jjjj')")
#         self.conn.commit()
#         cursor.close()
#     def getAllHouses(self):
#         cursor = self.conn.cursor()
#         cursor.execute("SELECT * FROM House")
#         houses = cursor.fetchall()
#         self.conn.commit()
#         cursor.close()
#         return houses
#     def getAllRecommendations(self):
#         cursor = self.conn.cursor()
#         cursor.execute("SELECT * FROM Recommendation")
#         recommendations = cursor.fetchall()
#         self.conn.commit()
#         cursor.close()
#         return recommendations

