import mysql.connector
from datetime import datetime


class EmployeeManager:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ajiThh**#110",
            database="company_db",
        )

    print("connected successfully")

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()

            query = """INSERT INTO employee
                       (name, place, mobile, email, department,salary,joining_date)
                       VALUES (%s, %s, %s, %s, %s, %s,%s)"""

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connection.commit()

            print("employee added successfully..!")

        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor=self.connection.cursor()

            query="select * from employee"

            self.cursor.execute(query)
            records=self.cursor.fetchall()

            for data in records:
                print(data)

        except Exception as e:
            print(e)

    def retrieve(self,id=None):
        try:
            self.cursor=self.connection.cursor()

            query = "SELECT * FROM employee WHERE id=%s"
            values = (id,)

            self.cursor.execute(query, values)

            records = self.cursor.fetchone()

            print(records)

        except Exception as e:
            print(e)

    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM employee WHERE id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            records = self.cursor.fetchone()
            return records
        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            records = self.get_object(id=id)

            if records != None:
                self.cursor = self.connection.cursor()

                placeholder = ", ".join([k + "=%s" for k in kwargs.keys()])

                query = f"UPDATE employee SET {placeholder} WHERE id = %s"

                values = list(kwargs.values())
                values.append(id)

                self.cursor.execute(query, values)
                self.connection.commit()

                print("Employee Updated successfully...!")

            else:
                print("Employee not found...!")

        except Exception as e:
            print(e)


    def delete(self, id=None):
        try:
            records = self.get_object(id=id)
            values = (id,)

            if records != None:
                query = "DELETE FROM employee WHERE id = %s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Employee deleted successfully...!")
            else:
                print("Employee not found...!")
        except Exception as e:
            print(e)


employee_instance = EmployeeManager()
# employee_instance.post(name="ajith",place="alattil",mobile="7306464646",email="ajith572@gmail.com",department="Developer",salary=100000,joining_date=datetime.datetime.today())
# employee_instance.post(name="anto",place="kannur",mobile="7305554646",email="anto2@gmail.com",department="software engineer",salary=102000,joining_date=datetime.today())

employee_instance.get()
print("-------------------------")
employee_instance.retrieve(1)
print("-------------------------")
employee_instance.put(1, name="kannan",email="kannan123@gmail.com")
employee_instance.get()
print("-------------------------")
employee_instance.delete(1)
employee_instance.get()
