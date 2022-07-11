#Christopher McCracken pysports_join_queries Assignment 9.2 7_10_2022

#import
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

db = mysql.connector.connect(**config)

cursor=db.cursor()

cursor.execute("SELECT player_id,first_name,last_name,team_name FROM player INNER JOIN team ON player.team_id=team.team_id;")
players = cursor.fetchall()

print("DISPLAYING PLAYER RECORDS")

#for loop
for player in players:
        #output formatting
        print(f"Player ID: {player[0]}")
        print(f"First Name: {player[1]}")
        print(f"Last Name: {player[2]}")
        print(f"Team Name: {player[3]}")
        print()


print()

input("press key to continue...")