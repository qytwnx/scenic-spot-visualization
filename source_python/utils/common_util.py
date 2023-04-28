import hashlib
import pymysql as mysql
import config.config as config


def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode("utf8"))
    return md5.hexdigest()


def connect_mysql():
    db = mysql.connect(host=config.MYSQL_HOST, user=config.MYSQL_USERNAME, password=config.MYSQL_PASSWORD,
                       port=config.MYSQL_PORT, database=config.MYSQL_DATABASE, charset='utf8')
    return db
