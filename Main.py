from sense_hat import SenseHat
import insertdatabase
import globals
import Gyroscope
import Arrows
import sys
import tweepy
from ISStreamer.Streamer import Streamer
sense=SenseHat()
sense.set_imu_config(False,False,True)
logger= Streamer(bucket_name="Sense Hat Sensor Data", access_key="ist_QsJ_mdh5bnHzduJDFhorX59W811C67q4")
Felborul=False
Utkozes=False
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

def OAuth(consumer_key,consumer_secret,access_token,access_token_secret):
    try:
       auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
       auth.set_access_token(access_token, access_token_secret)
       return auth
    except Exception as e:
       return None
#globals.init()
   
while True:
    
            Gyroscope.gyro()
            logger.log("Pitch: ",globals.pitch)
            logger.log("Roll: ",globals.roll)
            logger.log("Yaw: ",globals.yaw)
            logger.log("X: ",globals.x)
            logger.log("Y: ",globals.y)
            logger.log("Z: ",globals.z)
            insertdatabase.insert(globals.pitch,globals.roll,globals.yaw,globals.x,globals.y,globals.z)
            if(-2>globals.x):
                sense.show_letter("!")
                consumer_key='JoCmFVTD0NpKaVxpT9t8aMf8K'
                consumer_secret='HobMjR2wOnVvWoxf9nOh7uwyFpqdqOZlfaNVej2vkAC98asG6n'
                access_token='1083299768514854913-WmiGPShhCsyfkbvHOvTzVGIzm0ka48'
                access_token_secret='tx5ALfWlLnwfYeOXm5Vbon8Ev08mBVPMq1G1cYxyJ8Gr2'
                oauth = OAuth(consumer_key,consumer_secret,access_token,access_token_secret)
                api = tweepy.API(oauth)
                if( not Utkozes):
                    api.update_status('Utkozesveszely! x:{0}'.format(globals.x) )
                    print('Utkozes')
                    Utkozes=True
        
            if (globals.pitch>90 and globals.pitch <270) or (globals.roll>90 and globals.roll <270):
                sense.set_pixels( Arrows.piros_x() )
                consumer_key='JoCmFVTD0NpKaVxpT9t8aMf8K'
                consumer_secret='HobMjR2wOnVvWoxf9nOh7uwyFpqdqOZlfaNVej2vkAC98asG6n'
                access_token='1083299768514854913-WmiGPShhCsyfkbvHOvTzVGIzm0ka48'
                access_token_secret='tx5ALfWlLnwfYeOXm5Vbon8Ev08mBVPMq1G1cYxyJ8Gr2'
                oauth = OAuth(consumer_key,consumer_secret,access_token,access_token_secret)
                api = tweepy.API(oauth)
                if( not Felborul):
                    api.update_status('Felborultam,kuldj segitseget! p:{0}'.format(globals.pitch) )
                    print('Borulas')
                    Felborul=True
    
            elif globals.pitch >40 and globals.pitch <90:
                sense.set_pixels( Arrows.nyil_balra())
       
            elif globals.pitch <320 and globals.pitch >270:
                sense.set_pixels( Arrows.nyil_jobbra())
        
            elif globals.roll >40 and globals.roll<90:
                sense.set_pixels( Arrows.nyil_felfele())
       
            elif globals.roll <320 and globals.roll >270:
                sense.set_pixels( Arrows.nyil_lefele())
            else:
                sense.set_pixels(Arrows.ures_matrix()) 
            print("p:{0},r:{1},y:{2},x:{3},y:{4},z:{5}".format(globals.pitch,globals.roll,globals.yaw,globals.x,globals.y,globals.z))
        
            
    