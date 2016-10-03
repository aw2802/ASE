from flask import Flask, render_template, request
import pymssql
app = Flask(__name__)

conn = pymssql.connect(server='eats.database.windows.net', 
    user='th2520@eats', 
    password='123*&$eats', 
    database='AERIS') 

@app.route("/")
def main():
  # conn = pymssql.connect(server='eats.database.windows.net', 
  #   user='th2520@eats', 
  #   password='123*&$eats', 
  #   database='AERIS') 
  print ("connected!")
  cursor = conn.cursor()  

  # cursor.executemany(
  # "INSERT INTO Contacts VALUES (%s, %d)",
  # [('Anna Wen', 1234567890),
  # ('Tin Nilar', 4567123456),
  # ('James Corden', 1235768970)])

 # while row:  
  #     print ("Inserted Product ID : " +str(row[0]))  
  #     row = cursor.fetchone() 

  # while row: 
  #   print ("Name=%s, Number=%d" % (row[0], row[1]))
  #   render_template('index.html', name = row[0], number = row[1])
  #   row = cursor.fetchone()
  
  cursor.execute("SELECT * FROM Contacts")
  data= cursor.fetchall()  
 
    

  dataTable = []
  for i in data:
    dataTable.append(i[0]+ " , "+ str(i[1]))
 
  
  return render_template('index.html', data= dataTable)

@app.route('/add', methods=['GET', 'POST'])
def add():
  addedNum = request.form['number']
  addedName = request.form['name']
  cursor = conn.cursor()
  cursor.execute("SELECT name FROM Contacts WHERE number = %d", addedNum)
  result = []
  data = cursor.fetchall()

  for d in data:
    result.append(d[0])

  if len(result)== 0: # no matched ph num (not sure)
    print("hello")

    cursor.execute("INSERT INTO Contacts VALUES (%s, %d)", (addedName, addedNum)) 
    conn.commit()
  else:
    cursor.execute("UPDATE Contacts SET name = %s WHERE number = %d", (addedName, addedNum))

  cursor.execute("SELECT * FROM Contacts")
  data1= cursor.fetchall()  
 
  dataTable = []
  for i in data1:
    dataTable.append(i[0]+ " , "+ str(i[1]))


  return render_template('index.html', data= dataTable)
  
  



@app.route('/delete', methods=['GET', 'POST'])
def delete():
  addedNum = request.form['number']
  cursor = conn.cursor()
  cursor.execute("DELETE FROM Contacts WHERE number=%d", addedNum)
  conn.commit()

  cursor.execute("SELECT * FROM Contacts")
  data1= cursor.fetchall()  
 
  dataTable = []
  for i in data1:
    dataTable.append(i[0]+ " , "+ str(i[1]))


  return render_template('index.html', data= dataTable)
  conn.close()

if __name__ == "__main__":
  app.debug = True
  app.run()
  app.run(debug = True)