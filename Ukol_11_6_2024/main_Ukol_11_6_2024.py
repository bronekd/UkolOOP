import sqlite3

conn = sqlite3.connect('vegatables_and_fruits.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS vegfruit (
            id INTEGER PRIMARY KEY,
            name TEXT,
            druh TEXT,
            obsah_kalorii INTEGER,
            popis TEXT)""")


#cur.execute("""INSERT INTO vegfruit (name, druh, obsah_kalorii, popis) VALUES ('rajce', 'zelenina', 17, 'Rajčata jsou bohatá na vitaminy a minerály, přitom však mají nízký obsah kalorií')""")
#cur.execute("""INSERT INTO vegfruit (name, druh, obsah_kalorii, popis) VALUES ('pomeranc', 'ovoce', 50, 'Pomeranč je oranžový')""")
#cur.execute("""INSERT INTO vegfruit (name, druh, obsah_kalorii, popis) VALUES ('mandarinka', 'ovoce', 40, 'Mandarinka je oranžový')""")
#cur.execute("""INSERT INTO vegfruit (name, druh, obsah_kalorii, popis) VALUES ('mrkev', 'zelenina', 35, 'Mrkev je důležitá především pro svůj obsah betakarotenů a vitamínů A, B, C, D. Čerstvá mrkev nabízí také spoustu zdravé vlákniny.')""")
#cur.execute("""INSERT INTO vegfruit (name, druh, obsah_kalorii, popis) VALUES ('okurka', 'zelenina', 16, 'Okurka je zelená a plná vody')""")


conn.commit()

#načtení dat
cur.execute("SELECT * FROM vegfruit")
print(cur.fetchall())


