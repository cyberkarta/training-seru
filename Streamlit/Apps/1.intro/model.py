import sqlite3

conn = sqlite3.connect("komentar.db")

c = conn.cursor()

c.execute("""CREATE TABLE komentar(
    nama TEXT,
    judul TEXT,
    komentar TEXT)
    """)

conn.commit()

conn.close()