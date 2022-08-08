SQLite adalah bagian dari standard library, tidak perlu install apapun.

SQLite tidak bisa dibaca tanpa aplikasi, karena akan terlihat karakter random.

```python
# conn = sqlite.connect(':memory:')

conn = sqlite.connect('employee.db')

c = conn.cursor()

c.execute("""
	CREATE TABLE employees (
		first text,
		last text,
		pay integer)
""")

conn.commit() 

conn.close()
```

Tipe data:
- NULL
- INTEGER
- REAL (float)
- TEXT (string)
- BLOB (disimpan seperti pada inputnya)

INSERT 
```python
c.execute("INSERT INTO employees VALUES ('John', 'Doe', 70000)")
```

Defend from SQLInjection:
- Menggunakan DB API placeholder (tanda ? pada INSERT)
	- Vulnerable
	  `c.execute(f"INSERT INTO employees VALUES ({val1}, {val2}, {val3}))`
	- Vulnerable
	  `c.execute("INSERT INTO employees VALUES ( '{}', '{}', '{}' )".format(val1, val2, val3))`
	- Safe
	   `c.execute("INSERT INTO employees VALUES (?, ?, ?)", (val1, val2, val3))`
	  `conn.commit()`
	- Safe 
	  `c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':val1, 'last': val2, 'pay': val3})`
	  `conn.commit()`
- Query 
	- Vulnerable = `c.execute("SELECT * FROM employees WHERE last='Schafer'"`
	- Safe 
	  `c.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))`
	- Safe
	  `c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Schafer'})
