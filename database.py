import pymysql


def get_connection():

    conn = pymysql.connect(

        host="mysql-192bf532-voquynhhuong10a7-26bd.e.aivencloud.com",

        port=16801,

        user="avnadmin",

        password="AVNS_Gdo4fbPWzLsMDy83myf",

        database="company",

        ssl={
            "ca": "ca.pem"
        }

    )

    return conn
