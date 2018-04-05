# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import errorcode
import configparser

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('config_file',help='indiquez le fichier de configuration')

    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config_file)

    dict_config = {
        'user': config['DATABASE']['user'],
        'password': config['DATABASE']['password'],
        'host': config['DATABASE']['host'],
        'database': config['DATABASE']['database']
    }

    test_dict_conf = {}
    for k in config['DATABASE']:
        test_dict_conf[k] = config['DATABASE'][k]


    cnx = cur = None
    try:
        cnx = mysql.connector.connect(**test_dict_conf)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your user name or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cur = cnx.cursor()
        cur.execute('show databases;')
        for row in cur.fetchall():
            print(row)
    finally:
        if cur:
            cur.close()
        if cnx:
            cnx.close()