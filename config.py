# coding=utf-8
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'Nancy990927'
HOST = 'bj-cynosdbmysql-grp-d2ehu1js.sql.tencentcdb.com'
PORT = 24040
DATABASE = 'realEstate'
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)