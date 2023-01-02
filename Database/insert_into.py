import sqlite3
from sqlite3 import Error


def insert_into(conn ,data_to_table: dict):

    # exemple for dict data_to_table
    # data_to_table = {
    #         "commune" : {
    #             "name" : ["test_name1", "test_name2", "test_name3"],
    #             "code_postal" : ["test_code_postal1", "test_code_postal2", "test_code_postal3"],
    #             "population" : ["test_population1", "test_population2", "test_population3"]
    #         }
    #     }

    string_for_insert = []

    for_values = {}

    columns_of_data = []
    for datas_key ,datas in data_to_table.items():
        columns_of_data = [x.strip().title() for x in datas]
        count = 0

        for i in datas[list(datas.keys())[0]]:

            for_values[count] = []
            for_values[count].append([x[count] for key, x in datas.items()])
            count += 1
        count = 0
        for data_key, data in for_values.items():

            string_for_insert.append(f'''*INSERT INTO {str(datas_key)} ({', '.join(columns_of_data)}) VALUES''')
            string_for_insert.append("(")
            for data_key, data in datas.items():
                string_for_insert.append(f''''{str(data[count]).replace("'", " ")     }', ''')
            string_for_insert[len(string_for_insert)-1] = string_for_insert[len(string_for_insert)-1][:-2] + ")"
            count += 1


    cur = conn.cursor()

    for data in ''.join(string_for_insert).split("*"):

        print(''.join(data))
        cur.execute(''.join(data))

    conn.commit()
