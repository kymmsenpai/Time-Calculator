import re

def add_time(start, duration, day=False):

    # dict of days
    days = {
      'monday': 0 ,
      'tuesday' : 1,
      'wednesday' : 2,
      'thrusday' : 3,
      'friday' : 4,
      'saturday' : 5,
      'sunday' : 6
    }

    # get hour, minute and pm or am
    startHM = list(map(int,re.findall('[0-9]+',start)))
    durationHM = list(map(int,re.findall('[0-9]+',duration)))
    pm_am = re.findall(r'\bAM\b|\bPM\b',start)[0]

    # variable that determine how many days has been pass
    nextDay = 0

    # determine minute and give plus one if touch 60
    minute =  durationHM[1] + startHM[1]
    if minute > 59:
        minute -= 60
        startHM[0] += 1
    if minute < 10:
        minute = f'0{minute}'
    
    # determine how many days after calculation
    if durationHM[0] > 23:
        nextDay += (durationHM[0] - durationHM[0]%24) // 24
        durationHM[0] = durationHM[0]%24        
    
    # get new hour
    hour = startHM[0] + durationHM[0]

    # change pm to am or am to pm
    if hour > 23:
        hour = 0
        pm_am = 'AM'
    elif hour > 11:
        hour -= 12
        if pm_am == 'AM':
            pm_am = 'PM'
        else:
            pm_am = 'AM'
            nextDay += 1
    
    # hour control
    if hour == 0 and (pm_am =='PM' or pm_am == 'AM'):
        hour = 12

    # ouput control
    if day == False:
        if nextDay == 1:
            new_time = f'{hour}:{minute} {pm_am} (next day)'
        elif nextDay > 1:
            new_time = f'{hour}:{minute} {pm_am} ({nextDay} days later)'
        else:
            new_time = f'{hour}:{minute} {pm_am}'
    else:
        if nextDay == 1:
            new_day = days.get(day.lower()) + 1
            day = list(days.keys())[new_day]
            new_time = f'{hour}:{minute} {pm_am}, {day.title()} (next day)'
        elif nextDay > 1:
            new_day = days.get(day.lower())
            new_day += nextDay
            if new_day > 6:
              new_day %= 7
            day = list(days.keys())[new_day]
            new_time = f'{hour}:{minute} {pm_am}, {day.title()} ({nextDay} days later)'
        else:
            new_time = f'{hour}:{minute} {pm_am}, {day}'

    return new_time
  
if __name__ == '__main__':
    print(add_time("2:59 AM", "24:00", "saturDay"))