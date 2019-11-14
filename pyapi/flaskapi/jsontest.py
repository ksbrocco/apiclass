#!/usr/bin/python3

import requests
import json
import time

VALIDATEURL = "http://validate.jsontest.com/"
IPURL = "http://ip.jsontest.com/"
DATEURL = "http://date.jsontest.com/"
serverList = [server.rstrip('\n') for server in open("myservers.txt")]
def main():
    
    currentDate = requests.get(DATEURL)
    myIP = requests.get(IPURL)

    currentDatejson = currentDate.json()
    myIPjson = myIP.json()
    
    #print(time.localtime(currentDatejson["time"]))
    print(currentDatejson)
    print(myIPjson)
    print(serverList)

    validate = {"json": {"date" : currentDatejson["time"]}}
    print(validate)

if __name__ == "__main__":
    main()


