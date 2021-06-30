import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="@mysqlketangurav22",
  database="MyPythonDatabase"
)
mycursor = mydb.cursor()

while True:
   print("type 1      :to add a new doctor ")
   print("type 2      :to add a new patient")
   print("type 3      :to relate patient and doctor")
   print("type 4      :to view doctor names")
   print("type 5      :to view patient names")
   print("type 6      :to view patient name and corresponding doctor")
   print("type 7      :terminate patient  and doctor relation")
   print("type 8      :view patients names related to a doctor")
   print("type 9      :view doctors names related to a patient")
   print("type EXIT   :to exit")
   inp = eval(input())
   if inp == "EXIT":
      exit()
   elif inp == 1:
      name = input("Please Enter Doctor Name: ")
      department = input("Please Enter Doctor department: ")
      id = input("Please Enter Doctor id: ")
      sql = "INSERT INTO Doctors (name,department, id) VALUES (%s, %s, %s)"
      val = (name,department,id)
      mycursor.execute(sql, val)
      mydb.commit()
   elif inp == 2:
      name = input("Please Enter Patient Name: ")
      id = input("Please Enter Patient id: ")
      sql = "INSERT INTO Patients (name, id) VALUES (%s, %s)"
      val = (name,id)
      mycursor.execute(sql, val)
      mydb.commit()
   elif inp == 3:
      id1 = input("Please Enter the id of responsible Doctor: ")
      id2 = input("Please Enter Patient id: ")
      sql = "INSERT INTO DOC_PAT (D_code, P_code) VALUES (%s, %s)"
      val = (id1,id2)
      mycursor.execute(sql, val)
      mydb.commit()
   elif inp == 4:
      mycursor.execute("SELECT * FROM Doctors")
      myresult = mycursor.fetchall()
      for x in myresult:
         print(x)
   elif inp == 5:
      mycursor.execute("SELECT * FROM Patients")
      myresult = mycursor.fetchall()
      for x in myresult:
         print(x)
   elif inp == 6:
      mycursor.execute("SELECT Patients.name, Doctors.name From Doctors JOIN DOC_PAT on Doctors.id=DOC_PAT.D_code JOIN Patients on DOC_PAT.P_code=Patients.id")
      myresult = mycursor.fetchall()
      for x in myresult:
         print(x)
   elif inp == 8:
      id1 = input("Please Enter the id of responsible Doctor: ")
      mycursor.execute("SELECT Patients.name From Doctors JOIN DOC_PAT on Doctors.id=DOC_PAT.D_code JOIN Patients on DOC_PAT.P_code=Patients.id  WHERE Doctors.id=%s",(id1,))
      myresult = mycursor.fetchall()
      for x in myresult:
         print(x)

   elif inp == 9:
      id2 = input("Please Enter Patient id: ")
      mycursor.execute("SELECT Doctors.name From Doctors JOIN DOC_PAT on Doctors.id=DOC_PAT.D_code JOIN Patients on DOC_PAT.P_code=Patients.id WHERE Patients.id=%s",(id2,))
      myresult = mycursor.fetchall()
      for x in myresult:
         print(x)
   else:
       pass
