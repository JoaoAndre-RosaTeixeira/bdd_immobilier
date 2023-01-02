from os.path import exists

# function from another file
from Database.createDatabase import createDatabase
from Database.insertData import insert_into_database

# #  function who install a dependance neccessary for this code un_comment this for the first run
# import subprocess
# import sys
# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#
# pips_install = ['numpy', 'pandas']
# # , 'requests', 'beautifulsoup4', "Flask ", "flask-restful", "flask-cors", "requests"
#
# for pip in pips_install:
#     try:
#         install(pip)
#     except:
#         print(f"impossible d'installer {pip}")

# need pip install
import numpy as np
import pandas as pd

# the name of the database
db_name = "dataImmo.db"

pd_ref_geo = pd.read_csv("ressources/referentiel-geographique.csv")
pd_donnees_communes = pd.read_csv("ressources/donnees_communes.csv")

test = pd_donnees_communes.merge(pd_ref_geo, left_on='COM', right_on='com_nom' )
test = test.drop_duplicates(subset=["com_nom", "com_code1" ], keep='first')

if exists(db_name) == False:
    createDatabase(db_name)


# exemple to stock data in data_to_table from csv
data_to_table = {
    "region": {
        "name": list(test["reg_nom"]),
        "code": list(test["reg_code"])
    }
}
insert_into_database(db_name, data_to_table)


list_for_index = list(range(1, len(test.index)+1))
data_to_table = {
    "departement": {
        "name": list(test["dep_nom"]),
        "code": list(test["dep_code"]),
        "id_reg": list_for_index
    }
}
insert_into_database(db_name, data_to_table)

# probleme doublon for population
data_to_table = {
    "commune": {
        "name": list(test["com_nom"]),
        "code": list(test["com_code"]),
        "code_postal": list(test["com_code1"]),
        "population": list(test["PTOT"].where(test["com_nom"] == test["COM"])),
        "id_dpt": list_for_index
    }
}
insert_into_database(db_name, data_to_table)