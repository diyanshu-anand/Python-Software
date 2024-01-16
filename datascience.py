from http import client
import gspread
import oauth2client
import mysql.connector
from oauth2client.service_account import ServiceAccountCredentials
import MySQLCredentials as mc

#initialize varialbles for gspread

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('training.json', scope);

client = gspread.authorize(creds)

#define method to pull data from spreadsheet
def GetSpreadSheetData(sheetName, worksheetIndex):
    sheet = client.open(sheetName).get_worksheet(worksheetIndex)
    return sheet.get_all_values()[1:]

data = GetSpreadSheetData('trial2', 0)
print(data[1])
print(len(data))

# defining method to write list of data in mysql 
def WriteToMySQLTabel(sql_data, tableName):
    # we are using a try/except block (also called a try/catch block in other languages) which is good for error handling. It will “try” to execute anything in the “try” block, and if there is an error, it will report the error in the “except” block. Regardless of any errors, the “finally” block will always be executed.
    try:
        # Here we include the connection credentials for MySQL. We create a connection object that we pass the credentials to, and notice that we can specify the database which is ‘sys’ in the MySQLCredentials.py file because I’m using since I’m using the default database in MySQL Workbench 8.0.
        connection = mysql.connector.connect(
            user = mc.user,
            password = mc.password,
            host = mc.host,
            database = mc.database
        )
        sql_drop = "DROP TABLE IF EXISTS {}".format(tableName)
        # Now we will create the table, and the triple quotes are used so that when we go to the next line of code, we remain in a string. Otherwise it will terminate the string at the end of the line, and we want ALL of this to be one giant string. When injecting data into VALUES, we use the placeholder %s for each column of data we have.
        sql_create_table = '''CREATE TABLE {}(
            Timestamp VARCHAR(30),
            Answer VARCHAR(30),
            PRIMARY KEY (Timestamp)
        )'''.format(tableName)

        sql_insert_statement = '''INSERT INTO {} (
            Timestamp, 
            Answer
        ) VALUES(%s,%s)'''.format(tableName)
        # Here we create a cursor, which we will use to execute the MySQL statements above. After each statement is executed, a message will be printed to the console if the execution was successful.# Here we create a cursor, which we will use to execute the MySQL statements above. After each statement is executed, a message will be printed to the console if the execution was successful.
        cursor = connection.cursor()

        cursor.execute(sql_drop)
        print('Table {} has been droppped'.format(tableName))

        cursor.execute(sql_create_table)

        print('Table {} has been created'.format(tableName))
        # We need to write each row of data to the table, so we use a for loop that will insert each row of data one at a time

        for i in sql_data:
            cursor.execute(sql_insert_statement, i)
        # Now we execute the commit statement, and print to the console that the table was updated successfully            
        connection.commit()

        print("Table {} has successfully updated".format(tableName()))

    except mysql.connector.Error as error:
            connection.rollback()
            print("Error: {}. Table {} not updated!".format(error,tableName))
    

    finally:
        cursor.execute('SELECT COUNT(*) FROM {}'.format(tableName))

        rowCount = cursor.fetchone() [0]

        print(tableName, 'row count:', rowCount)

        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



WriteToMySQLTabel(data, 'MyData')