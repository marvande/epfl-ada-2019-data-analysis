import datetime

def time_to_seconds(time):
    """
    Transforms a time into a number of seconds. 0 seconds corresponds to 00h00.
    @input:
        - time of the day, in type datetime.
    @output: returns the corresponding number of seconds.
    """
    return 60*time.minute + 3600*time.hour


def avg_time(times):
    """
    Calculates the average time of the day given a list of times.
    @input:
        - [array of datetime data] : the list of the times we want to average.
    @output: returns the average of the times.
    """
    avg = 0
    for elem in times:
        avg += 60*elem.minute + 3600*elem.hour
    avg /= len(times)
    if round(avg/3600) == 24 or round((avg%3600)/60) == 60:  
        return datetime.time(int(avg/3600),int((avg%3600)/60))
    else : 
        return datetime.time(round(avg/3600),round((avg%3600)/60))  
    
    #round is closer to reality, but we cannot do it for 59.7 minutes for example because 'minute = 60' is not allowed.