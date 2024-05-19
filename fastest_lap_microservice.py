import time
import math
import re


def readLapTimes(path_to_read_file):
    with open(path_to_read_file, 'r+') as file1:

        laps = file1.readlines()
        if laps != []:
            try:
                user_fastest_lap = int(laps[0].split(':')[0]) * 60 + int(laps[0].split(':')[1])
                fastest_race_lap= int(laps[1].split(':')[0]) * 60 + int(laps[1].split(':')[1])

                percentage_off = (user_fastest_lap - fastest_race_lap)/ 60
                percentage_off = math.floor((percentage_off*100)*10)/10
                if percentage_off <= 0:
                    result = "Gold!"
                else:
                    result = str(percentage_off)+'%'
                
                #done with current lap data
                file1.truncate(0)

                writeData(result, './percentage_off.txt')
            except:
                writeData('There was an error calculating the data requested', './percentage_off.txt')
                file1.truncate(0)

    file1.close()


def writeData(data, path_to_write_file):
    with open(path_to_write_file, 'r+') as file2:
        content = file2.read()
        file2.seek(0)
        file2.write(data)
        file2.truncate()
    
    file2.close()


while True:
    time.sleep(1)
    readLapTimes('./fastest_laps.txt')



            
    

