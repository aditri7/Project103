import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/aditri"
to_dir = "C:/Users/downloaded"

class FileMovementHandler(FileSystemEventHandler):
 event_handler=FileMovementHandler()
 from_dir = "C:/Users/aditri"
 to_dir = "C:/Users/downloaded"
 def on_created(self,event):
    print(event)
    
    event_handler=FileMovementHandler()
    
    observer=Observer()
    
    observer.schedule(event_handler, from_dir,recursive=True)
    
    observer.start()
    
    try:
     while True:
        time.sleep(2)
        print("running...")
        except KeyboardInterrupt:
        print("stopped!")
        observer.stop()

