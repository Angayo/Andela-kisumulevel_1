import psycopg2
conn = psycopg2.connect(database="project", user = "postgres", password = "angayo", host = "127.0.0.1", port = "5432")
print("success")

cur = conn.cursor()
cur.execute('''CREATE TABLE users (
    user_id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR(100),
    second_name VARCHAR(100),
    sur_name VARCHAR(50),
    email VARCHAR(100),
    username VARCHAR(100),
    password VARCHAR(100));''')
print("Table created")

cur = conn.cursor()
cur.execute('''CREATE TABLE comments (
    comment_id SERIAL PRIMARY KEY NOT NULL,
    comment VARCHAR(255),
    date TIMESTAMP(255),
    username VARCHAR(100));''')
print("comments table created")

cur = conn.cursor()
cur.execute(''' CREATE TABLE admini (
    admin_id SERIAL PRIMARY KEY NOT NULL,
    username VARCHAR(100),
    password VARCHAR(100));''')
print("admin created")

cur = conn.cursor()
cur.execute("INSERT INTO users (user_id,first_name,second_name,sur_name,email,username,password) \
      VALUES (1, 'Amoth','Angayo', 'Aaron', 'oamoth@gmail.com','oma','1234' )");

cur.execute("INSERT INTO comments (comment_id,comment,date,username) \
      VALUES (1, 'Welcome to the new begining','20180709', 'oma')");

cur.execute("INSERT INTO admini (admin_id,username,password) \
      VALUES (1, 'Paul', 'kotieno')");

cur.execute("SELECT user_id, first_name, second_name, sur_name, email, password from users")
rows = cur.fetchall()
for row in rows:
	print("user_id", row[0])
	print ("first_name", row[1])
	print ("second_name", row[2])
	print ("sur_name", row[3])
	print ("username", row[4], "\n")
print("fetch successful")

conn.commit()
print("added admin")
conn.close()
