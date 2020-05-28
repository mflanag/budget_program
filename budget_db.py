import sqlite3
import time

def create_db():
    connection = sqlite3.connect("matt_budget.db")
    cursor = connection.cursor()
    cursor.execute("""DROP TABLE budget;""")
    sql_command = """
        CREATE TABLE budget (
            entry_id INTEGER PRIMARY KEY,
            entry_time timestamp,
            category VARCHAR(30),
            cost REAL,
            comments TEXT
        );"""
    cursor.execute(sql_command)

    connection.commit()
    connection.close()
#

# entry has the users commands and updates the db
def insert_entry(cat, cost, comments):
    connection = sqlite3.connect("matt_budget.db")
    cursor = connection.cursor()
    format_str = """INSERT INTO budget (entry_id, entry_time, category, cost, comments)
                        VALUES (NULL, "{entry_time}", "{category}", "{cost}", "{comments}");"""
    sql_command = format_str.format(entry_time=time.time(), category=cat, cost=cost, comments=comments)
    cursor.execute(sql_command)

    connection.commit()
    connection.close()
    return True
#

def query_table():
    connection = sqlite3.connect("matt_budget.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM budget")
    print("fetchall:")
    result = cursor.fetchall()
    for r in result:
        print(r)
    #
    connection.close()
#

if __name__=="__main__":
    query_table()