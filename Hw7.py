import sqlite3
db = sqlite3.connect('studentsgeeks.db')
c = db.cursor()

c.execute('''create table if not exists studentsgeeks (
id int primary key,
hobby text,
first_name text,
last_name text,
birth_year int,
homework_score int
)''')

c.execute('''insert into studentsgeeks (hobby, first_name, last_name, birth_year, homework_score) values
('reading', 'alice', 'smith', 1998, 15),
('painting', 'bob', 'johnson', 1997, 8),
('sports', 'charlie', 'williams', 1999, 12),
('coding', 'david', 'brown', 1996, 20),
('dancing', 'emma', 'miller', 1995, 6),
('cooking', 'frank', 'taylor', 1994, 18),
('gaming', 'grace', 'anderson', 2000, 5),
('music', 'henry', 'thomas', 1993, 9),
('traveling', 'ivy', 'moore', 1992, 14),
('photography', 'jack', 'white', 1991, 7)''')

c.execute('''select * from studentsgeeks where length(last_name) > 10''')
for i in c.fetchall():
    print(i)

c.execute('''update studentsgeeks set first_name = 'genius' where homework_score > 10''')

c.execute('''select * from studentsgeeks where first_name = 'genius' ''')

c.execute('''delete from studentsgeeks where id % 2 = 0''')

db.commit()
db.close()