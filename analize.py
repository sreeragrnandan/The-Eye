import pymysql
from playsound import playsound

i=0
connection = pymysql.connect(host="localhost",port=3307, user="root", passwd="", database="theEye")
cursor = connection.cursor()
cursor.execute("TRUNCATE TABLE blinks;") 
connection.close()

while True:
    connection = pymysql.connect(host="localhost",port=3307, user="root", passwd="", database="theEye")
    cursor = connection.cursor()
    # Query for mintime maxTime blinkCount
    MinTime = "SELECT time FROM blinks WHERE id=(SELECT min(id) FROM blinks);"
    print(MinTime)
    MaxTime = "SELECT time FROM blinks WHERE id=(SELECT max(id) FROM blinks);"
    BlinkCount = "SELECT blinkCount FROM blinks WHERE id=(SELECT max(id) FROM blinks);"

    cursor.execute(MinTime)
    MinTime = cursor.fetchall()
    if MinTime:
        MinTime = MinTime[0][0]
        MinTime = int(MinTime)
    
    # break
    cursor.execute(MaxTime)
    MaxTime = cursor.fetchall()
    if MaxTime:
        MaxTime = MaxTime[0][0]
        MaxTime = int(MaxTime)

    cursor.execute(BlinkCount)
    BlinkCount = cursor.fetchall()
    if BlinkCount:
        BlinkCount = BlinkCount[0][0]
      
 

    print(MinTime)
    print(MaxTime)
    print(BlinkCount)
    
    # print(TotalTime)
    if MinTime and MaxTime:
        TotalTime = MaxTime-MinTime
        print(TotalTime)
        if TotalTime<4000 and BlinkCount==6:
            print("Help me")
            playsound('audio/help.mp3')
            cursor.execute("TRUNCATE TABLE blinks;")
            break
    connection.close()  
