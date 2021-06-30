import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@mysqlketangurav22"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE MyPythonDatabase")
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="@mysqlketangurav22",
  database="MyPythonDatabase"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Doctors (name VARCHAR(255),department VARCHAR(255), id INT, PRIMARY KEY(id))")
mycursor.execute("CREATE TABLE Patients (name VARCHAR(255), id INT, PRIMARY KEY(id))")
mycursor.execute("CREATE TABLE DOC_PAT ( D_code INT, P_code INT, FOREIGN KEY (P_code) REFERENCES Patients(id),FOREIGN KEY (D_code) REFERENCES Doctors(id))")
import