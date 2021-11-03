import redis

import pywinauto


help = """
[1] - 
[2] -
[3] - 
"""




def main_loop():
    while True:
        # if ans := input("Enter command > "):
        #     print(help)
        app = pywinauto.Application().Start('f-zila.exe')
        wizard = app['I Agree']
        wizard.NextButton.Click()
        exit()

main_loop()


#pyautogui, pywinauto, pyautoit, mouse и т.д