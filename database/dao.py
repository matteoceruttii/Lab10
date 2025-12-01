from database.DB_connect import DBConnect
from model.archi import Archi
from model.hub import Hub

# classe DAO per l'interfaccia con database
class DAO:
    def __init__(self):
        pass

# funzione che ricava dal database i nodi e gli archi tra gli hub (anche il valore della merce)
    @staticmethod
    def load_archi_spedizioni():
        # apro le connessioni
        conn = DBConnect.get_connection()
        result = []
        query = ''' SELECT 
                        LEAST(s.id_hub_origine, s.id_hub_destinazione)       AS h1, 
                        GREATEST(s.id_hub_origine, s.id_hub_destinazione)    AS h2, 
                        SUM(s.valore_merce)                                  AS valore_totale, 
                        COUNT(*)                                             AS n_spedizioni
                    FROM spedizione s 
                    GROUP BY h1, h2 '''
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)

        # popolo la struttura dati
        for row in cursor:
            elemento = Archi(row['h1'],
                             row['h2'],
                             row['valore_totale'],
                             row['n_spedizioni'])
            result.append(elemento)

        # chiudo le connessioni
        cursor.close()
        conn.close()
        return result


# funzione che gestisce gli hub e ricava le informazioni necessarie dal database
    @staticmethod
    def load_hub():
        # apro le connessioni
        conn = DBConnect.get_connection()
        result = []
        query = ''' SELECT *
                    FROM hub h '''
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)

        # popolo la struttura dati
        for row in cursor:
            elemento = Hub(row['id'],
                           row['codice'],
                           row['nome'],
                           row['citta'],
                           row['stato'],
                           row['latitudine'],
                           row['longitudine'])
            result.append(elemento)

        # chiudo le connessioni
        cursor.close()
        conn.close()
        return result


if __name__ == '__main__':
    dao = DAO()
    for hub in dao.load_hub():
        print(hub)

    for arco in dao.load_archi_spedizioni():
        print(arco)