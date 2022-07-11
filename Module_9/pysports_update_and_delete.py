#Christopher McCracken pysports_update_and_delete.py 7_10_2022

import mysql.connector

from mysql.connector import errorcode

#config


config = {
    "user":"pysports_user",
    "password": "Azerus07!",
    "host":"127.0.0.1",
    "database":"pysports",
    "raise_on_warnings":True
}




try: #try

    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    def outputDB(): #output db class

        cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")

        players = cursor.fetchall()  
        
        for player in players:  #formatting

            print(f"Player ID: {player[0]}")

            print(f"First Name: {player[1]}")

            print(f"Last Name: {player[2]}")

            print(f"Team Name: {player[3]}")

            print()
        
        print()# output

    cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1);") #insert and display

    print("-- DISPLAYING PLAYERS AFTER INSERT --")#display

    outputDB()

    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';") #update and display

    print("-- DISPLAYING PLAYERS AFTER UPDATE --")#display

    outputDB()


    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum';")#delete and display

    print("-- DISPLAYING PLAYERS AFTER DELETE --")#display

    outputDB()
    
    db.close()
    
    input("press any key to continue...")#open line


except mysql.connector.Error as err: #except for errors

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:

        print("The supplied username or password are invalid.")


    elif err.errno == errorcode.ER_BAD_DB_ERROR:

        print("The specified database does not exist.")

    else:
        print(err)