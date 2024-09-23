import tkinter as tk
import time
import threading
import random
import pip
import os
import importlib


# reqs:
# pip install pywin32
# pip install keyboard
# pip install pynput
# pip install pyautogui
# pip install opencv-python

def import_or_install(packagename, package):
    try:
        __import__(packagename)
    except ImportError:
        try:
            pip.main(['install', package])
        except AttributeError:
            try:
                pip._internal.main(['install', package])
            except:
                import subprocess
                subprocess.call(['pip', 'install', package])

import_or_install("pynput", "pynput")
import_or_install("PyAutoGUI", "pyautogui")
import_or_install("customtkinter", "customtkinter")
import_or_install("keyboard", "keyboard")
import_or_install("win32crypt", "pywin32")
import_or_install("opencv-python", "opencv-python")

import customtkinter
import win32api, win32con
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
from pyautogui import *
import pyautogui
import keyboard


os.chdir(os.path.dirname(os.path.abspath(__file__)))
main_target_x = 970
main_target_y = 760
sleep = 0.1

mouse = Controller()

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()

app.title("Instalocker")
app.geometry("700x450")

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def perform_click_iso():
    image1_path = 'images/iso.png'
    num_clicks = 5

    while num_clicks > 0:
        location = pyautogui.locateOnScreen(image1_path, region=(30, 300, 440, 900), confidence=0.8)

        if location is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x + 2, center_y + 2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return


def perform_click_vyse():
    image1_path = 'images/vyse.png'
    num_clicks = 5

    while num_clicks > 0:
        location = pyautogui.locateOnScreen(image1_path, region=(30, 300, 440, 900), confidence=0.8)

        if location is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x + 2, center_y + 2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return

def perform_click_reyna():
        image1_path = 'images/reyna.png'
        num_clicks = 5

        while num_clicks > 0:
            location = pyautogui.locateOnScreen(image1_path, region=(30, 300, 440, 900), confidence=0.8)

            if location is not None:
                mouse.position = (960, 530)
                mouse.click(Button.left, 1)
                mouse.click(Button.left, 1)
                time.sleep(0.03)
                x, y, width, height = location
                center_x = x + width / 2
                center_y = y + height / 2

                mouse.position = (center_x, center_y)
                pyautogui.moveTo(center_x + 2, center_y + 2, duration=0.03)
                mouse.click(Button.left, 1)
                time.sleep(0.05)
                mouse.click(Button.left, 1)

                mouse.position = (main_target_x, main_target_y)
                mouse.click(Button.right, 1)
                time.sleep(0.03)
                mouse.click(Button.left, 1)
                num_clicks -= 1
                return
            

def perform_click_jett():
    image2_path = 'images/jett.png'
    num_clicks = 5

    while num_clicks > 0:
        location2 = pyautogui.locateOnScreen(image2_path, region=(30, 300, 440, 900), confidence=0.8)

        if location2 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location2
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_phoenix():
    image3_path = 'images/phoenix.png'
    num_clicks = 5

    while num_clicks > 0:
        location3 = pyautogui.locateOnScreen(image3_path, region=(30, 300, 440, 900), confidence=0.8)

        if location3 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location3
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_raze():
    image4_path = 'images/raze.png'
    num_clicks = 5

    while num_clicks > 0:
        location4 = pyautogui.locateOnScreen(image4_path, region=(30, 300, 440, 900), confidence=0.8)

        if location4 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location4
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_neon():
    image5_path = 'images/neon.png'
    num_clicks = 5

    while num_clicks > 0:
        location5 = pyautogui.locateOnScreen(image5_path, region=(30, 300, 440, 900), confidence=0.8)

        if location5 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location5
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_yoru():
    image6_path = 'images/yoru.png'
    num_clicks = 5

    while num_clicks > 0:
        location6 = pyautogui.locateOnScreen(image6_path, region=(30, 300, 440, 900), confidence=0.8)

        if location6 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location6
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            mouse.click(Button.left, 1)
            time.sleep(0.01)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.01)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_brimstone():
    image7_path = 'images/brimstone.png'
    num_clicks = 5

    while num_clicks > 0:
        location7 = pyautogui.locateOnScreen(image7_path, region=(30, 300, 440, 900), confidence=0.8)

        if location7 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location7
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_omen():
    image8_path = 'images/omen.png'
    num_clicks = 5

    while num_clicks > 0:
        location8 = pyautogui.locateOnScreen(image8_path, region=(30, 300, 440, 900), confidence=0.8)

        if location8 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location8
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_viper():
    image9_path = 'images/viper.png'
    num_clicks = 5

    while num_clicks > 0:
        location9 = pyautogui.locateOnScreen(image9_path, region=(30, 300, 440, 900), confidence=0.8)

        if location9 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location9
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_harbor():
    image10_path = 'images/harbor.png'
    num_clicks = 5

    while num_clicks > 0:
        location10 = pyautogui.locateOnScreen(image10_path, region=(30, 300, 440, 900), confidence=0.8)

        if location10 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location10
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_astra():
    image11_path = 'images/astra.png'
    num_clicks = 5

    while num_clicks > 0:
        location11 = pyautogui.locateOnScreen(image11_path, region=(30, 300, 440, 900), confidence=0.8)

        if location11 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location11
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        
def perform_click_skye():
    image12_path = 'images/skye.png'
    num_clicks = 5

    while num_clicks > 0:
        location12 = pyautogui.locateOnScreen(image12_path, region=(30, 300, 440, 900), confidence=0.8)

        if location12 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location12
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_breach():
    image13_path = 'images/breach.png'
    num_clicks = 5

    while num_clicks > 0:
        location13 = pyautogui.locateOnScreen(image13_path, region=(30, 300, 440, 900), confidence=0.8)

        if location13 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location13
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_kayo():
    image14_path = 'images/kayo.png'
    num_clicks = 5

    while num_clicks > 0:
        location14 = pyautogui.locateOnScreen(image14_path, region=(30, 300, 440, 900), confidence=0.8)

        if location14 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location14
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_fade():
    image15_path = 'images/fade.png'
    num_clicks = 5

    while num_clicks > 0:
        location15 = pyautogui.locateOnScreen(image15_path, region=(30, 300, 440, 900), confidence=0.8)

        if location15 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location15
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_sova():
    image16_path = 'images/sova.png'
    num_clicks = 5

    while num_clicks > 0:
        location16 = pyautogui.locateOnScreen(image16_path, region=(30, 300, 440, 900), confidence=0.8)

        if location16 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location16
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_gekko():
    image17_path = 'images/gekko.png'
    num_clicks = 5

    while num_clicks > 0:
        location17 = pyautogui.locateOnScreen(image17_path, region=(30, 300, 440, 900), confidence=0.8)

        if location17 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location17
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_sage():
    image18_path = 'images/sage.png'
    num_clicks = 5

    while num_clicks > 0:
        location18 = pyautogui.locateOnScreen(image18_path, region=(30, 300, 440, 900), confidence=0.8)

        if location18 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location18
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_killjoy():
    image19_path = 'images/killjoy.png'
    num_clicks = 5

    while num_clicks > 0:
        location19 = pyautogui.locateOnScreen(image19_path, region=(30, 300, 440, 900), confidence=0.8)

        if location19 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location19
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_cypher():
    image20_path = 'images/cypher.png'
    num_clicks = 5

    while num_clicks > 0:
        location20 = pyautogui.locateOnScreen(image20_path, region=(30, 300, 440, 900), confidence=0.8)

        if location20 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location20
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_chamber():
    image21_path = 'images/chamber.png'
    num_clicks = 5

    while num_clicks > 0:
        location21 = pyautogui.locateOnScreen(image21_path, region=(30, 300, 440, 900), confidence=0.8)

        if location21 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location21
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

def perform_click_deadlock():
    image22_path = 'images/deadlock.png'


    num_clicks = 5

    while num_clicks > 0:
        location22 = pyautogui.locateOnScreen(image22_path, region=(30, 300, 440, 900), confidence=0.8)

        if location22 is not None:
            mouse.position = (960, 530)
            mouse.click(Button.left, 1)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            x, y, width, height = location22
            center_x = x + width / 2
            center_y = y + height / 2

            mouse.position = (center_x, center_y)
            pyautogui.moveTo(center_x +2, center_y+2, duration=0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.05)
            mouse.click(Button.left, 1)

            mouse.position = (main_target_x, main_target_y)
            mouse.click(Button.right, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            time.sleep(0.03)
            mouse.click(Button.left, 1)
            num_clicks -= 1
            return
        

duelist_button = customtkinter.CTkButton(master=app, text="Duelist")
duelist_button.place(relx=0.02, rely=0.0)

reyna_button = customtkinter.CTkButton(master=app, text="Reyna", command=perform_click_reyna)
reyna_button.place(relx=0.02, rely=0.15)

jett_button = customtkinter.CTkButton(master=app, text="Jett", command=perform_click_jett)
jett_button.place(relx=0.02, rely=0.3)

phoenix_button = customtkinter.CTkButton(master=app, text="Phoenix", command=perform_click_phoenix)
phoenix_button.place(relx=0.02, rely=0.45)

raze_button = customtkinter.CTkButton(master=app, text="Raze", command=perform_click_raze)
raze_button.place(relx=0.02, rely=0.6)

neon_button = customtkinter.CTkButton(master=app, text="Neon", command=perform_click_neon)
neon_button.place(relx=0.02, rely=0.75)

yoru_button = customtkinter.CTkButton(master=app, text="Yoru", command=perform_click_yoru)
yoru_button.place(relx=0.02, rely=0.9)

controller_button = customtkinter.CTkButton(master=app, text="Controller")
controller_button.place(relx=0.27, rely=0.0)

brimstone_button = customtkinter.CTkButton(master=app, text="Brimstone", command=perform_click_brimstone )
brimstone_button.place(relx=0.27, rely=0.15)

omen_button = customtkinter.CTkButton(master=app, text="Omen", command=perform_click_omen)
omen_button.place(relx=0.27, rely=0.3)

viper_button = customtkinter.CTkButton(master=app, text="Viper", command=perform_click_viper)
viper_button.place(relx=0.27, rely=0.45)

harbor_button = customtkinter.CTkButton(master=app, text="Harbor", command=perform_click_harbor)
harbor_button.place(relx=0.27, rely=0.6)

astra_button = customtkinter.CTkButton(master=app, text="Astra", command=perform_click_astra)
astra_button.place(relx=0.27, rely=0.75)

iso_button = customtkinter.CTkButton(master=app, text="Iso", command=perform_click_iso)
iso_button.place(relx=0.27, rely=0.9)

initiator_button = customtkinter.CTkButton(master=app, text="Initiator")
initiator_button.place(relx=0.52, rely=0.0)

skye_button = customtkinter.CTkButton(master=app, text="Skye", command=perform_click_skye)
skye_button.place(relx=0.52, rely=0.15)

breach_button = customtkinter.CTkButton(master=app, text="Breach", command=perform_click_breach)
breach_button.place(relx=0.52, rely=0.3)

kayo_button = customtkinter.CTkButton(master=app, text="Kayo", command=perform_click_kayo)
kayo_button.place(relx=0.52, rely=0.45)

fade_button = customtkinter.CTkButton(master=app, text="Fade", command=perform_click_fade)
fade_button.place(relx=0.52, rely=0.6)

sova_button = customtkinter.CTkButton(master=app, text="Sova", command=perform_click_sova)
sova_button.place(relx=0.52, rely=0.75)

gekko_button = customtkinter.CTkButton(master=app, text="Gekko", command=perform_click_gekko)
gekko_button.place(relx=0.52, rely=0.9)

sentinel_button = customtkinter.CTkButton(master=app, text="Sentinel")
sentinel_button.place(relx=0.77, rely=0.0)

sage_button = customtkinter.CTkButton(master=app, text="Sage", command=perform_click_sage)
sage_button.place(relx=0.77, rely=0.15)

killjoy_button = customtkinter.CTkButton(master=app, text="Killjoy", command=perform_click_killjoy)
killjoy_button.place(relx=0.77, rely=0.3)

cypher_button = customtkinter.CTkButton(master=app, text="Cypher", command=perform_click_cypher)
cypher_button.place(relx=0.77, rely=0.45)

chamber_button = customtkinter.CTkButton(master=app, text="Chamber", command=perform_click_chamber)
chamber_button.place(relx=0.77, rely=0.6)

deadlock_button = customtkinter.CTkButton(master=app, text="Deadlock", command=perform_click_deadlock)
deadlock_button.place(relx=0.77, rely=0.75)

vyse_button = customtkinter.CTkButton(master=app, text="Vyse", command=perform_click_vyse)
vyse_button.place(relx=0.77, rely=0.9)

app.mainloop()
