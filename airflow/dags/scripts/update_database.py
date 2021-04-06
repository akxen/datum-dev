"""Update MySQL database with latest current report data"""

import os
import csv

import MySQLdb
import MySQLdb.cursors
from sqlalchemy import create_engine

import numpy as np
import pandas as pd

from io import TextIOWrapper
from zipfile import ZipFile


def connect_to_database():
    """Connect to MySQL database"""

    conn = MySQLdb.connect(
        host=os.environ['MYSQL_HOST'],
        port=int(os.environ['MYSQL_PORT']),
        user=os.environ['MYSQL_USER'],
        passwd=os.environ['MYSQL_PASSWORD'],
        cursorclass=MySQLdb.cursors.DictCursor)

    cur = conn.cursor()

    return conn, cur


def get_table_columns(table):
    """Get table columns"""

    # Read rows and append column name and data type to main container
    template_path = os.path.join(os.environ['MYSQL_TABLE_TEMPLATES_DIR'], f'{table}.csv')

    with open(template_path, newline='') as f:
        template_reader = csv.reader(f, delimiter=',')

        # Rows in the CSV template (corresponding to columns into MySQL table)
        columns = []
        for row in template_reader:
            columns.append(row[0])

    return columns


def get_table_unique_keys(table):
    """Get columns that correspond to jointly unique keys"""

    # Read rows and append column name and data type to main container
    template_path = os.path.join(os.environ['MYSQL_TABLE_TEMPLATES_DIR'], f'{table}.csv')

    with open(template_path, newline='') as f:
        template_reader = csv.reader(f, delimiter=',')

        # Rows in the CSV template (corresponding to columns into MySQL table)
        columns = []
        for row in template_reader:
            if row[2] == 'KEY':
                columns.append(row[0])

    return columns


def get_columns_sql(table):
    """Construct SQL component specifying table columns"""

    # Read rows and append column name and data type to main container
    template_path = os.path.join(os.environ['MYSQL_TABLE_TEMPLATES_DIR'], f'{table}.csv')

    with open(template_path, newline='') as f:
        template_reader = csv.reader(f, delimiter=',')

        # Rows in the CSV template (corresponding to columns into MySQL table)
        columns = []
        for row in template_reader:
            columns.append(row[:2])

    # SQL to construct column name component for query
    sql = ', '.join([' '.join(c) for c in columns])

    return sql


def get_unique_key_sql(table):
    """Get SQL component that specifies jointly unique keys"""

    keys = get_table_unique_keys(table=table)

    # SQL to construct unique key statement for query
    if keys:
        sql = ', UNIQUE KEY (' + ', '.join(keys) + '))'
    else:
        sql = ')'

    return sql


def create_table(table):
    """
    Create SQL table based on template.

    Parameters
    ----------
    table : str
        Name of MySQL table. Note this must correspond with the CSV template.
    """

    # Query used to create table
    columns_sql = get_columns_sql(table=table)
    unique_key_sql = get_unique_key_sql(table=table)

    create_table_sql = (f"""
    CREATE TABLE IF NOT EXISTS
    {os.environ['MYSQL_SCHEMA']}.{table} ({columns_sql},
    PRIMARY KEY (row_id) {unique_key_sql}""")

    # Create database if it doesn't already exist
    conn, cur = connect_to_database()
    create_database_sql = f"CREATE DATABASE IF NOT EXISTS {os.environ['MYSQL_SCHEMA']}"
    cur.execute(create_database_sql)
    conn.commit()

    # Create table
    cur.execute(create_table_sql)

    # Close database connections
    cur.close()
    conn.close()


def initialise_tables():
    """Setup database tables if they don't already exist"""

    tables = [
        'dispatch_scada',
        'dispatch_scada_files',
        'dispatch_report_case_solution',
        'dispatch_report_case_solution_files',
    ]

    for t in tables:
        create_table(t)


def get_uploaded_files(table):
    """List of all files that have been uploaded"""

    conn, cur = connect_to_database()

    cur.execute(f"SELECT filename FROM {os.environ['MYSQL_SCHEMA']}.{table}_files")
    files = cur.fetchall()

    cur.close()
    conn.close()

    return [i['filename'] for i in files]


def get_available_files(files_dir):
    """List of all files that have been downloaded"""

    return [i for i in os.listdir(files_dir) if i.endswith('.zip')]


def get_files_to_upload(files_dir, table):
    """List of files to upload"""

    uploaded = get_uploaded_files(table=table)
    available = get_available_files(files_dir=files_dir)

    to_upload = list(set(available) - set(uploaded))

    # Sort from oldest to most recent
    to_upload.sort()

    return to_upload


def extract_values(files_dir, filename, filters):
    """Extract values from zip file. Filtering on colum values to identify sections."""

    out = []
    csv_filename = filename.replace('.zip', '.CSV')
    with ZipFile(os.path.join(files_dir, filename)) as zf:
        with zf.open(csv_filename, 'r') as infile:
            reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
            for row in reader:

                # Check if row should be retained by checking filters
                keep_row = all([row[index] == value for index, value in filters])
                if keep_row:
                    out.append(row)
    return out


def get_dispatch_scada_data(files_dir, filename):
    """Extract dispatch SCADA data from zipped archive"""

    file_path = os.path.join(files_dir, filename)
    df = pd.read_csv(file_path, skiprows=1, skipfooter=1, engine='python',
                     usecols=['SETTLEMENTDATE', 'DUID', 'SCADAVALUE'],
                     dtype={'DUID': str, 'SCADAVALUE': float})

    return df


def get_dispatch_report_case_solution(files_dir, filename):
    """Extract case solution form dispatch reports"""

    data = extract_values(files_dir=files_dir, filename=filename,
                          filters=[(1, 'DISPATCH'), (2, 'CASESOLUTION')])

    df = pd.DataFrame(data)
    df = df.rename(columns=df.iloc[0]).drop(df.index[0])

    # Get table columns, convert to lower case, remove 'row_id'
    columns = get_table_columns(table='dispatch_report_case_solution')
    columns = [i for i in columns if i != 'row_id']
    columns = [i.upper() for i in columns]

    out = df.loc[:, columns].replace(r'', np.NaN)

    return out


def upload_to_database(table, files_dir, filename, func):
    """Upload data to MySQL database"""

    host = os.environ['MYSQL_HOST']
    schema = os.environ['MYSQL_SCHEMA']
    user = os.environ['MYSQL_USER']
    password = os.environ['MYSQL_PASSWORD']

    connection_string = f"mysql+mysqldb://{user}:{password}@{host}/{schema}"
    my_conn = create_engine(connection_string)

    # Extract data and upload to database
    df = func(files_dir=files_dir, filename=filename)

    print("TEST DF", df)
    df.to_sql(con=my_conn, schema=schema, name=table,
              if_exists='append', index=False)

    # Record filename
    conn, cur = connect_to_database()
    record_sql = f"INSERT INTO {schema}.{table}_files (filename) VALUES ('{filename}')"
    cur.execute(record_sql)
    conn.commit()

    cur.close()
    conn.close()


def update_database(table):
    """Upload all files to MySQL database"""

    initialise_tables()

    # Root folder containing nemweb data
    nemweb_root = os.environ['NEMWEB_ROOT_DIR']

    table_info = {
        'dispatch_scada': {
            'files_dir': os.path.join(nemweb_root, 'Reports', 'CURRENT', 'Dispatch_SCADA'),
            'extractor_function': get_dispatch_scada_data
        },
        'dispatch_report_case_solution': {
            'files_dir': os.path.join(nemweb_root, 'Reports', 'CURRENT', 'Dispatch_Reports'),
            'extractor_function': get_dispatch_report_case_solution
        },
    }

    files_dir = table_info[table]['files_dir']
    files_to_upload = get_files_to_upload(files_dir=files_dir, table=table)

    for i in files_to_upload:
        try:
            print('Uploading', table, i)
            upload_to_database(table=table,
                               files_dir=files_dir,
                               filename=i,
                               func=table_info[table]['extractor_function'])
        except MySQLdb.IntegrityError as e:
            print(e, table, i)


if __name__ == '__main__':
    from dotenv import load_dotenv

    load_dotenv(os.path.join(os.path.dirname(__file__),
                'config', 'db-updater-development.env'))

    initialise_tables()
    update_database(table='dispatch_scada')
