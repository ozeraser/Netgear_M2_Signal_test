import requests 
import json
import time
from datetime import datetime 


#Setup
startDatetime = datetime.now()
filename = "logfile-" + startDatetime.strftime("%Y%m%d %H-%M-%S")

url = 'http://192.168.1.1/api/model.json?internalapi=1'
durationToLog = 12*60 #minutes
timeCheck = True
print('***************************************************')
print('*                                                 *')
print('*    Getting stats from 192.168.1.1               *')
print('*    Highest RSRP 1st Important                   *')
print('*    Highest SINR 2nd Important                   *')
print('*    Better signal 20 > 0 > -5 >-80 Worse signal  *')
print('*                                                 *')
print('***************************************************')

while timeCheck:
    
    #go grab the JSON data and load it into a dict
    response = requests.get(url)
    r = response.json()

    #grab only the pertinent data and add current time
    rsrpdata = r['wwan']['signalStrength']['rsrp']
    sinrdata = r['wwan']['signalStrength']['sinr']
    barsdata = r['wwan']['signalStrength']['bars']
    datedata = datetime.now().isoformat() #don't bother with now_string at all
    logline = "RSRP: " + str(rsrpdata) + "     SINR: " + str(sinrdata) + "     Signal Bars: " + str(barsdata) + "     Date time: " + str(datedata)
    print(logline)

    logline = logline.replace("'","")
    
    

    #write JSON formatted data to the logfile and close it
    with open('%s.txt' % filename, mode='a') as file:
        file.write('%s\n' %logline)
        #json.dump(data, file)
        file.close

    timeCheck = (datetime.now() - startDatetime ).total_seconds() < durationToLog*60
    time.sleep(1)
    
print('All Done!')
#(r['wwan']['signalStrength'])
#print(r['wwan']['signalStrength']['sinr'])