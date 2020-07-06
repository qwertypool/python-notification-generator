import time
import os
from plyer import notification

# current_path = os.path.dirname('main.py') # Where your .py file is located
# resource_path = os.path.join(current_path, 'E:\python_notif') # The resource folder path
# image_path = os.path.join(resource_path, 'E:\python_notif') # The image folder path


if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please take your medicine!!",
            message = "Taking the prescirbed medicine at time is very imp for a faster recovery!!",
            #app_icon= "E:\python_notif\drugs2.png",
            timeout=5           #give the required time for scheduling
        )
        time.sleep(60*60*12)
