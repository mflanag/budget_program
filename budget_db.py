import sqlite3
import datetime

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

def insert_entry(entry):
    connection = sqlite3.connect("matt_budget.db")
    cursor = connection.cursor()
    format_str = """INSERT INTO budget (entry_id, entry_time, category, cost, comments)
                        VALUES (NULL, "{entry_time}", "{category}", "{cost}", "{comments}");"""
    sql_command = format_str.format(entry_time=entry[0], category=entry[1], cost=entry[2], comments=entry[3])
    cursor.execute(sql_command)

    connection.commit()
    connection.close()
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
    create_db()
    entry = [datetime.datetime.now(), "food", 10.32, "i bought lunch"]
    insert_entry(entry)
    query_table()
