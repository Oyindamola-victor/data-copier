# This integrates the read and write logic to load a json file into a Database

import os
from read import get_json_reader
from write import load_db_table


def main():
    BASE_DIR = os.environ.get('BASE_DIR')
    table_name = os.environ.get('TABLE_NAME')
    json_reader = get_json_reader(BASE_DIR,table_name)
    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
    
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])

    
if __name__ == "__main__":
    main()
       