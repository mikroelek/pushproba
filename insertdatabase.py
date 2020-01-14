import mysql.connector
from datetime import datetime
from sense_hat import SenseHat
import time



def insert(pitch,roll,yaw,x,y,z):
    mydb=mysql.connector.connect(host="localhost", user="Raspberry", password="root", database="exampledb5")
    mycursor=mydb.cursor()
    now=datetime.now()
    formatted_date=now.strftime('%Y-%m-%d %H:%M:%S')
    sql="""INSERT INTO adatok (datum,pitch,roll,yaw,backwardforward,rightleft,updown)
    VALUES(%s,%s,%s,%s,%s,%s,%s)"""
    val=(formatted_date,pitch,roll,yaw,x,y,z)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()