import pymssql
from utils.get_credentials import get_credentials


def connect_to_db():
    credentials = get_credentials()
    # print(credentials)

    # db_name = ""
    # conn = pymssql.connect(credentials['db']['url'], credentials['db']['user'], credentials['db']['password'], db_name)
    # cursor = conn.cursor()
    # conn.close()
    return  # return a db instance (maybe a cursor???)
