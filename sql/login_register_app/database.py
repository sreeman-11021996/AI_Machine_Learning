import mysql.connector

class DBHelper:
    def __init__ (self):
        try:
            self.conn = mysql.connector.connect(
                host = "localhost",user = "root",password = "",
                database = "login_register")
            self.mycurser = self.conn.cursor()
        except:
            print("Server could not connect! Some error occured")
        else:
            print("Server Connected")
    
    def register (self,name,email,password):
        try:
            self.mycurser.execute("""
            INSERT INTO `users` (`User Id`, `Name`, `Email Id`, `Password`) VALUES (NULL, '{}', '{}', '{}');
            """.format(name,email,password))
            self.conn.commit()
        except Exception as e:
            return 0
        else:
            return 1
    def login(self,email,password):
        try:
            self.mycurser.execute("""
            SELECT * FROM `users` WHERE `Email Id` LIKE '{}' AND `Password` = {}
            """.format(email,password))
            # fetching data from database
            data = self.mycurser.fetchall()
        except:
            return 0
        else:
            return data