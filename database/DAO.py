from database.DB_connect import DBConnect
from model.airport import Airport
from model.connessione import Connessione


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                FROM airports"""
        cursor.execute(query, )

        res = []
        for row in cursor:
            res.append(Airport(**row))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getEdges(miglia):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT 
                LEAST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS a1,
                GREATEST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS a2,
                AVG(DISTANCE) AS media_distanza
                FROM flights
                GROUP BY a1, a2
                HAVING media_distanza > %s"""
        cursor.execute(query,(miglia,) )

        res = []
        for row in cursor:
            res.append(Connessione(**row))

        cursor.close()
        conn.close()
        return res