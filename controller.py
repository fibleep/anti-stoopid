import time
import pyautogui
import threading
import os

img_dirpath = os.path.join(os.path.abspath(os.curdir), 'stoopids')

class Controller:
    def __init__(self) -> None:
        self.focus = False
        self.stoopids = os.listdir(img_dirpath)
        self.mainThread = threading.Thread(target=self.remove_stoopid)
        self.mainThread.start()
        self.pause = threading.Event()
        
    def toggle_focus(self):
        self.focus = not self.focus
        self.pause.set() if self.focus else self.pause.clear()
        
    def remove_stoopid(self):
        while True:
            if self.focus:
                stoopid_present = [pyautogui.locateOnScreen(os.path.join(img_dirpath, stoopid), confidence=0.5) for stoopid in self.stoopids]
                time.sleep(5)
                if any(stoopid_present):
                    print("STTOPID CONTAINED")
                    pyautogui.hotkey('ctrl', 'w')
            
            
            