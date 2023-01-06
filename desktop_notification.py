'''
To run in background 
   >>> pythonw <filename.py>
'''

from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "*** Take Rest ***",
            message = "Its time to take a 5 min break.",
            timeout = 5
        )
        time.sleep(10)

