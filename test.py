data_to_table = {
        "commune" : {
            "name" : ["test_name1", "test_name2", "test_name3"],
            "code_postal" : ["test_code_postal1", "test_code_postal2", "test_code_postal3"],
            "population" : ["test_population1", "test_population2", "test_population3"]
        }
    }

string_for_insert = []
for datas_key ,datas in data_to_table.items():
    columns_of_data = [x.strip().title() for x in datas]
    for_values = {}
    count = 0
    for data_key, data in datas.items():
        for_values[count] = [dat for dat in data]
        count += 1
    print(for_values)

    count = 0
    for data_key, data in datas.items():
        string_for_insert.append(f'''INSERT INTO {str(datas_key)} ({', '.join(columns_of_data)}) VALUES''')
        string_for_insert.append("(")
        string_for_insert.append(f''' '{"', '".join(for_values[count])}' ''')
        string_for_insert[len(string_for_insert) - 1] = string_for_insert[len(string_for_insert) - 1][:-1]
        string_for_insert.append(")")
        count += 1
    # string_for_insert.append(f'''INSERT INTO {str(datas_key)} ({', '.join(columns_of_data)}) VALUES''')
    # string_for_insert.append("(")
    # for data_key, data in datas.items():
    #     string_for_insert.append(f"'{str(data[0])}', ")
    # string_for_insert[len(string_for_insert)-1] = string_for_insert[len(string_for_insert)-1][:-1]
    # string_for_insert.append(")")

for data in string_for_insert:
    print(''.join(data))
