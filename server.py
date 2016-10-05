from flask import Flask, render_template, request
import pymssql
app = Flask(__name__)

conn = pymssql.connect(server='eats.database.windows.net', 
    user='th2520@eats', 
    password='123*&$eats', 
    database='AERIS') 

@app.route("/")
def main():

  cursor = conn.cursor()  

  
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
  # conn.close()

if __name__ == "__main__":
  app.debug = True
  app.run()
  app.run(debug = True)