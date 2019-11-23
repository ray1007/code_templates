import sqlite3

conn = sqlite3.connect("temp.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS supplier_groups;
CREATE TABLE supplier_groups (
    group_id integer PRIMARY KEY,
    group_name text NOT NULL
);
DROP TABLE IF EXISTS suppliers;
CREATE TABLE suppliers (
    supplier_id   INTEGER PRIMARY KEY,
    supplier_name TEXT    NOT NULL,
    group_id      INTEGER NOT NULL,
    FOREIGN KEY (group_id)
       REFERENCES supplier_groups (group_id)
);
INSERT INTO supplier_groups (group_name)
VALUES
   ('Domestic'),
   ('Global'),
   ('One-Time');
INSERT INTO suppliers (supplier_name, group_id)
VALUES ('HP', 2);
INSERT INTO suppliers (supplier_name, group_id)
VALUES('ABC Inc.', 4);
""")

# use namedtuple to for insert, retrieve rows
from collections import namedtuple

# make the tuples same as db schema.
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# create data containers.
link = Link(0, 60398, 1334014208.0, 109, "C ovx.", "http://")

# Insertion
# use ? in SQL command, and pass the tuple to .execute()
db.execute('insert into links values (?, ?, ?, ?, ?, ?)', l)

# Query
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print((emp.name, emp.title))


