import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(self.command, shell=True)

    def on_any_event(self, event):
        if event.src_path.endswith("README.md"):
            return
        if event.event_type in ('modified', 'created', 'deleted'):
            print(f'{event.src_path} has been {event.event_type}. Restarting...')
            self.process.terminate()
            self.process = subprocess.Popen(self.command, shell=True)

if __name__ == "__main__":
    path = "."
    command = "python main.py"
    event_handler = ChangeHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("Watching for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
