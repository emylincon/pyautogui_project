import pyautogui
import time
#click on word Point(x=807, y=1072)
#click on blank file Point(x=275, y=176)
#click on word Point(x=972, y=484)
#click close Point(x=1892, y=14)
#click save Point(x=968, y=672)
# print(pyautogui.position())


def create_word_file(filename, content):
    pyautogui.click(807, 1072)
    time.sleep(5)
    pyautogui.click(275, 176)
    time.sleep(2)
    pyautogui.click(972, 484)
    pyautogui.typewrite(content)
    pyautogui.click(1892, 14)
    time.sleep(1)
    pyautogui.typewrite(filename)
    pyautogui.click(968, 672)


create_word_file('emeka', 'i love jess she is a great wife')