import mysql.connector
import difflib 
from difflib import get_close_matches

class Connection:
    def __init__(self):
        self.conn=mysql.connector.connect(
            user="ardit700_student",
            password="ardit700_student",
            host="108.167.140.122",
            database="ardit700_pm1database"            
        )
        self.cursor=self.conn.cursor()
        self.query_1=self.cursor.execute("SELECT Expression From Dictionary")
        self.results_1=self.cursor.fetchall()
        self.values_1=[x[0] for x in self.results_1]

    def checking(self,word):
        if word in self.values_1:
            return True
        else:
            return False

    def translate(self,word):
        self.query=self.cursor.execute("SELECT Definition FROM Dictionary WHERE Expression='%s'"%word)
        results=self.cursor.fetchall()
        return results

    def translate_error(self,word):
        if len(get_close_matches((word),self.values_1))>0:
            return "Did you mean %s instead? "%get_close_matches((word),self.values_1)[0]
        else:
            return "No such word found.Please double check it."
    def choices_y(self,word):
        self.query=self.cursor.execute("SELECT Definition FROM Dictionary WHERE Expression='%s'"%get_close_matches((word),self.values_1)[0])
        results=self.cursor.fetchall()
        return results

    
        
        

