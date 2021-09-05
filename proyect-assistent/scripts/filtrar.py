from watchdog import observers
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json
import os,time,shutil
#Instale la libreria watchdog "pip install watchdog"

class FileHandler(FileSystemEventHandler):
    def on_modified(self,event):
        for file in os.listdir(path):
            
            file_folder = os.path.join(path,file)
            shutil.move(file_folder,move_folder)
        

# Cambiar la ruta dependiendo el PC

path = 'C://Users//Bryan Turrubiates//Downloads'
move_folder = "C://Users//Bryan Turrubiates//Desktop//CarpetaReceptora"   

event_handler = FileHandler()
observer = observers.Observer()
observer.schedule(event_handler,path,recursive=True)
observer.start()


try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
 