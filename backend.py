import mysql.connector
import difflib
from difflib import get_close_matches


con=mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
    )

cursor=con.cursor()

def translate(word):
    query=cursor.execute("SELECT Definition FROM Dictionary WHERE Expression='%s'" %word)
    results=cursor.fetchall()
    if results:
        return results
    else:
        query=cursor.execute("SELECT Expression FROM Dictionary")
        results=cursor.fetchall()
        values=[x[0] for x in results]
        
        if len(get_close_matches((word),values))>0:
            Yn=input("Did you mean %s instead? Enter Y for Yes and N for No "%get_close_matches((word),values)[0])
            if Yn=="Y":
                query=cursor.execute("SELECT Definition FROM Dictionary WHERE Expression='%s'"%get_close_matches((word),values)[0]) 
                results=cursor.fetchall()
                return results
            elif Yn=="N":
                return "The word does not exist.Please double check it."
            else:
                return "Unsupported query"
        else:
            return "The word does not exist.Please double check it!"
word=input("Enter a word: ")


output= translate(word)

if type(output)==list:
    for item in output:
        print(item[0])
else:
    print(output)


