import mysql.connector
from difflib import get_close_matches

class Connection:
    def __init__(self):

        self.con=mysql.connector.connect(
            user="ardit700_student",
            password="ardit700_student",
            host="108.167.140.122",
            database="ardit700_pm1database"
            )
        self.cursor=self.con.cursor()
        
    def checking(self,word):
        self.query=self.cursor("SELECT Expression FROM Dictionary")
        results=self.cursor.fetchall()    
        if  word in results:
            return True
        else:
            return False
           
    def translate(self,word):
        self.query=self.cursor.execute("SELECT DEFINITION FROM Dictionary WHERE Expression='%s'"%word)
        results=self.cursor.fetchall()
        return results

    def translate_error(self,word):
        self.values=[x[0] for x in self.results]
        if len(get_close_matches((word),self.values))>0:
            return "Did you mean %s instead?"%word
        else:
            return "No such word found.Please double check it."
        
    

        


