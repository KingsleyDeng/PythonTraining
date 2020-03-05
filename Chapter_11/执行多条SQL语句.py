import sqlite3

conn = sqlite3.connect('first.db')

c = conn.cursor()

c.executemany('insert into user_tb values(null, ?, ?, ?)',
              (('sun', '123456', 'male'), ('bai', '123456', 'female'),
               ('zhu', '123456', 'male'), ('niu', '123456', 'male'),
               ('tang', '123456', 'male')))

conn.commit()

c.close()

conn.close()