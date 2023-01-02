import os
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    # YOUR CODE
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)


def create_table(conn, name, cols):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    # YOUR CODE
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {name}({cols})")




def createDatabase(db_name):
    conn = create_connection(db_name)

    try:
        if conn is not None:
            # create exchange table
            # YOUR CODE

            create_table(conn, "region", '''
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name VARCHAR(50) NOT NULL,
                                code VARCHAR(50) NOT NULL
                                            ''')

            create_table(conn, "departement", '''
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name VARCHAR(50) NOT NULL,
                                code VARCHAR(50) NOT NULL,
                                id_reg VARCHAR(50) NOT NULL,
                                FOREIGN KEY (id_reg) REFERENCES region(id)
                                            ''')
            create_table(conn, "commune", '''
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            name VARCHAR(50) NOT NULL,
                                            code VARCHAR(50) NOT NULL,
                                            code_postal VARCHAR(50) NOT NULL,                                
                                            Population INTEGER(12) NOT NULL,
                                            id_dpt VARCHAR(50) NOT NULL,                           
                                            FOREIGN KEY (id_dpt) REFERENCES departement(id)
                                                        ''')
            create_table(conn, "vente", '''
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                date DATE NOT NULL,
                                valeur INTEGER(12) NOT NULL
                                            ''')
            create_table(conn, "bien", '''
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name_voie VARCHAR(50) NOT NULL,
                                number INTEGER NOT NULL,
                                type_voie VARCHAR(50) NOT NULL,
                                total_piece INTEGER(12) NOT NULL,
                                surface_carree FLOAT(12) NOT NULL,
                                surface_local INTEGER(12) NOT NULL,
                                type_local VARCHAR(50) NOT NULL,
                                id_cmn VARCHAR(50) NOT NULL,
                                id_vente VARCHAR(50) NOT NULL,
                                FOREIGN KEY (id_cmn) REFERENCES commune(id),
                                FOREIGN KEY (id_vente) REFERENCES vente(id)
                                ''')
        else:
            print("Error! cannot create the database connection.")
    except Error as e:
        print(e)
    finally:
        if conn:
            # conn.commit()
            # cur = conn.cursor()
            # cur.execute("SELECT * FROM exchange")
            # df = pd.DataFrame(cur.fetchall(),columns = ['id','name','currency','code'])
            # print(df)
            conn.close()


