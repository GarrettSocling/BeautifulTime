import tingbot
from tingbot import *
import time

@every(seconds=1.0/30)
def loop():
    week_day = time.strftime("%A")
    current_time = time.strftime("%H:%M")
    month = time.strftime("%B")
    day = time.strftime("%d")
    year = time.strftime("%Y")
    current_hour = time.strftime("%H")
    current_minute = time.strftime("%M")
    
    def date_extention(day):
        if day%10 == 1:
            return '%dst' % day
        if day== 2:
            return '%dnd' % day
        if day%10 == 3:
            return '%drd' % day
        if (day%10 >= 4) or (day%10== 0):
            return '%dth' % day
            
    day_formatted = date_extention(int(day))

    screen.fill(
        color='black'
    )
    screen.text(
        "It is %s, the %s" %(week_day, day_formatted) ,
        xy=(160,35),
        color='white',
        font_size=20,
        align='center'
    )
    
    screen.text(
        "of %s, %s" %(month, year),
        xy=(160,60),
        color='white',
        font_size=20,
        align='center'
    )
    
    screen.text(
        "%s:%s" %(current_hour, current_minute),
        color='white',
        font_size=70,
        align='center'
    )
    
    screen.text(
        "Make the Most Out of Today",
        xy=(160,190),
        color='white',
        font_size=15,
        align='center'
    )
    
    screen.text(
        "Beautiful Time",
        xy=(160,210),
        color='white',
        font_size=10,
        align='center'
    )
    
    
   
  
tingbot.run()