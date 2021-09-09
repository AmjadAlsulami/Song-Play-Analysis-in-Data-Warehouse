import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

# drop_tables(cur, conn)
def drop_tables(cur, conn):
    """
    The function will execute the drop table statment
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

# create_tables(cur, conn)
def create_tables(cur, conn):
     """
    The function will execute the create table statment
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

# main()
def main():
    """
    start a config object and connection
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()