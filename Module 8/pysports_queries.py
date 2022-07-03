from select import select
import mysql.connector
from mysql.connector import errorcode

config = {
    "user":"pysports_user",
    "password": "Azerus07!",
    "host":"127.0.0.1",
    "database":"pysports",
    "raise_on_warnings":True
}

try:
    db=mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"],config["host"],config["database"]))
    cursor = db.cursor()
    cursor.execute('SELECT player_id, first_name, last_name, team_id FROM player')
    employees = cursor.fetchall()

    for employee in employees:
        print('Player ID: {}'.format(employee[0]))
        print('First Name: {}'.format(employee[1]))
        print('Last Name: {}'.format(employee[2]))
        print('Team ID: {}'.format(employee[3]))
        print("\n")

        #input("\n\n Press any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")
    else:
        print(err)
finally:
    db.close()
