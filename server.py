from flask import Flask, render_template
import pymssql
app = Flask(__name__)

@app.route("/")
def main():
  conn = pymssql.connect(server='eats.database.windows.net', 
    user='th2520@eats', 
    password='123*&$eats', 
    database='AERIS') 
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
  conn.commit()
  conn.close()
  
  return render_template('index.html', data= dataTable)
    # , data = row[2])

if __name__ == "__main__":
  app.debug = True
  app.run()
  app.run(debug = True)