from time import time,sleep
import json

speedUpFactor=10.0  #how much the tome in universe goes compared to reality
preferedStep=10*60  #which second the waitUntilEvent will try to end on

timeZero=0
currentTime=0
eventList=[]

def sortList(l):
    '''returns the list sorted given on the first element'''
    return sorted(eventList,key=lambda x: x[0])

def addEvent(t,arg):
    '''adds an event to the eventList as a side effect'''
    global eventList
    eventList.append(tuple([t])+tuple(arg))

def waitUntilEvent(t=-1,f=False):
    '''waits until given time, or until next event. will ignore events if f=True'''
    global currentTime
    eventList=sortList(eventList)
    event=False
    if len(eventList)>0:
        if eventList[0][0]<=t:
            if f:
                pass
            else:
                event=True
                t=eventList[0][0]

    while currentTime+preferedStep<t:
            if currentTime%preferedStep!=0:
                sleeptime=preferedStep - currentTime%preferedStep
                sleep(sleeptime/speedUpFactor)
                currentTime+=sleeptime
            else:
                sleeptime=preferedStep
                sleep(sleeptime/speedUpFactor)
                currentTime+=sleeptime

    sleeptime=t - currentTime
    sleep(sleeptime/speedUpFactor)
    currentTime+=sleeptime
    if event:
        return eventList.pop(0)
    else:
        return None
