# Packages:
import win32gui, win32con
import pyautogui
from PIL import ImageGrab
import pytesseract
import numpy as nm
import cv2
from time import sleep


# Functions:
def alert_chat(id):
  chat = pyautogui.locateCenterOnScreen('./assets/chat.png')
  pyautogui.moveTo(chat)
  pyautogui.click()
  pyautogui.write(f'ALERT: { id } IS AN IMPOSTER AMONG US')

def guardian():
  pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
  zoom_window = win32gui.FindWindowEx(None, None, None, 'Zoom Meeting')
  # win32gui.SetForegroundWindow(zoom_window)
  win32gui.ShowWindow(zoom_window, win32con.SW_MAXIMIZE)

  participants = pyautogui.locateCenterOnScreen('./assets/participants.png')
  pyautogui.moveTo(participants)
  pyautogui.click()

  arrow_down = pyautogui.locateCenterOnScreen('./assets/arrow_down.png')
  pyautogui.moveTo(arrow_down)

  leftX = pyautogui.position().x
  topY = pyautogui.position().y
  rightX = pyautogui.size().width
  bottomY = pyautogui.size().height
  
  top_of_scrollbar = pyautogui.locateCenterOnScreen('./assets/top_of_scrollbar.png')
  pyautogui.moveTo(top_of_scrollbar)

  MAX_SCROLL_COUNT = 15
  scroll_count = 0
  while True:
    scroll_count = 0
    while scroll_count < MAX_SCROLL_COUNT:
      cap = ImageGrab.grab(bbox =(leftX, topY, rightX, bottomY))
      raw_string = pytesseract.image_to_string(
        cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
        lang ='eng')
      print(raw_string)
      pyautogui.scroll(5)
      scroll_count = scroll_count + 1
      sleep(2)
    sleep(5)

sleep(5)
guardian()
