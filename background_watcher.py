import time
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from privacy_engine import process_image

SCREENSHOT_FOLDER = r"C:\Users\Lenovo\Pictures\Screenshots"

class ScreenshotHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.src_path.endswith((".png", ".jpg", ".jpeg")) and "_protected" not in event.src_path:

            print("New screenshot detected:", event.src_path)

            # wait for file to finish saving
            time.sleep(2)

            if os.path.exists(event.src_path):
                try:
                    output_path = event.src_path.replace(".png", "_protected.png")
                    process_image(event.src_path, output_path)
                    print("Protected version saved:", output_path)

                except Exception as e:
                    print("Error processing image:", e)


def start_monitor():

    # Wait after system boot so folders are ready
    time.sleep(10)

    if not os.path.exists(SCREENSHOT_FOLDER):
        print("Screenshot folder not found:", SCREENSHOT_FOLDER)
        return

    event_handler = ScreenshotHandler()
    observer = Observer()
    observer.schedule(event_handler, SCREENSHOT_FOLDER, recursive=False)
    observer.start()

    print("Monitoring screenshots folder...")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == "__main__":
    start_monitor()