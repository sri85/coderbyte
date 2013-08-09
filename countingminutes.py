import datetime as dt
import time
def CountingMinutesI():
    mystr ="12:30pm-12:00am"
    x = mystr.split('-')
    print 
    start=time.strftime("%H:%M", time.strptime(x[0], "%I:%M%p")) 
    end=time.strftime("%H:%M", time.strptime(x[1], "%I:%M%p")) 
    start_dt = dt.datetime.strptime(start, '%H:%M')
    end_dt = dt.datetime.strptime(end, '%H:%M')
    diff = (end_dt - start_dt) 
    print (diff.seconds/60)
    
    
CountingMinutesI()
