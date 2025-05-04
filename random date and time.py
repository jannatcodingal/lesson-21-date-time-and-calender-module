import random
import time
def getRandomDate(startDate,endDate):
    print("printing random date between",startDate,"and",endDate)
    randomGenerator=random.random()
    dateFormat="%m/%d/%Y"
    startTime=time.mktime(time.strptime(startDate,dateFormat))
    endtime=time.mktime(time.strptime(endDate,dateFormat))
    randomtime=startTime+randomGenerator*(endtime-startTime)
    randomDate=time.strftime(dateFormat,time.localtime(randomtime))
    return randomDate
print("randomDate= ",getRandomDate("01/01/2000","12/31/2023"))