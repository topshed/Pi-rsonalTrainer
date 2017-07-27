import time
import signal
import random
import os
import scrollphathd
from scrollphathd.fonts import font5x7
from gpiozero import Buzzer, Button
import signal

exercises = [' burpees ', 
             ' press-ups ', 
             ' side-steps ', 
             ' step-ups ', 
             ' sit-ups ', 
             ' skipping ',
             ' star-jumps ',
             ' shuttles ',
             ' dips ',
             ' lunges ',
             ' squats ',
             ' plank ']

buzz = Buzzer(18)
button_onoff = Button(9)
button_start = Button(19)


def shutdown():
    cmd = "shutdown -h now"
    os.system(cmd)

button_onoff.when_pressed = shutdown

def countdown(t):
    for i in range(t,0,-1):
        print(i)
        scrollphathd.write_string(str(i), x=5, y=0, font=font5x7, brightness=0.5)
        scrollphathd.show()
        buzz.on()
        time.sleep(1)
        buzz.off()
        scrollphathd.clear()
        scrollphathd.show()
        
def flash(t):
    buzz.on()
    for x in range(int(t/0.2)):
        scrollphathd.fill(1, x=0, y=0, width=17, height=7)
        scrollphathd.show()
        time.sleep(0.1)
        scrollphathd.clear()
        scrollphathd.show()
        time.sleep(0.1)
    buzz.off()

def run_session():
    flash(1)        
    #Set a more eye-friendly default brightness
    for r in range(4):
        for f in range(10):
            scrollphathd.set_brightness(0.6)
            rep = random.choice(exercises)
            l = scrollphathd.write_string(' next: ' +rep, x=0, y=0, font=font5x7, brightness=0.5)
            start = time.time()
            rest = True
            while rest:
                scrollphathd.show()
                scrollphathd.scroll()
                time.sleep(0.025)
                intermed = time.time()
                if intermed - start > 5:
                    rest = False
            scrollphathd.clear()
            scrollphathd.show()
            countdown(5)
            flash(1)
            l = scrollphathd.write_string(rep, x=0, y=0, font=font5x7, brightness=0.5)
            w = scrollphathd.get_buffer_shape()[0]
            #scrollphathd.clear()

            start = time.time()
            train = True
            while train:
                scrollphathd.show()
                scrollphathd.scroll()
                time.sleep(0.025)
                intermed = time.time()
                if intermed - start > 15:
                    train = False
            scrollphathd.clear()
            scrollphathd.show()
            countdown(5)
            flash(1)
        msg = " break "
        l = scrollphathd.write_string(msg, x=0, y=0, font=font5x7, brightness=0.5)
        ex_break = True
        start = time.time()
        while ex_break:
            scrollphathd.show()
            scrollphathd.scroll()
            time.sleep(0.025)
            intermed = time.time()
            if intermed - start > 55:
                ex_break = False
        scrollphathd.clear()
        scrollphathd.show()
        countdown(5)
        flash(1)

button_start.when_pressed = run_session
signal.pause()
