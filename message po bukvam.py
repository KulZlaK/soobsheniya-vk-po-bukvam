'''
код печатания сообщения по буквам в Вконтакте с обходом антиспама.
(тестировалось в браузере opera с масштабом 50%)
*войти в "вконтакте", открыть "сообщения", поставить разрешение монитора 1680*1050.
*запустить программу в английской раскладке в pycharm c импортом библиотеки pyautogui.
*вставить руссктй текст, скопировать ctrl + c символ, который будет использоваться в качестве пробела.
*нажать enter, убедившись, что включена латинская раскладка.
*программа откроет переписку с новыми сообщениями. если такой нет - переписку, на которую будет наведен курсор.
'''
from time import sleep
import pyautogui


text = input('текст сообщения: ')
text_dva = ''
layout = dict(zip(map(ord, "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'),
                           "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'))
for el in text:
    if el == ' ':
        text_dva += '0'
    elif el == '!':
        text_dva += '!'
    elif el == '?':
        text_dva += '&'
    else:
        text_dva += el.translate(layout)


def viz_dva():
    sleep(0.2)
    fo = None
    while fo == None:
        fo = pyautogui.locateCenterOnScreen("finish.png", region=(761, 166, 931, 937))
    pyautogui.moveTo(fo[0], fo[1], duration=1)
    pyautogui.click()
    sleep(0.5)
    pyautogui.hotkey('shift', 'alt')
    for e in text_dva:
        spam = pyautogui.locateCenterOnScreen("spam.png", region=(868, 386, 917, 400))
        if spam != None:
            sleep(2.1)
            pyautogui.moveTo(790, 435, duration=2)
            pyautogui.click()
            sleep(1.1)
        if e == '0':
            sleep(2.8)
            pyautogui.moveTo(730, 969, duration=0.3)
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'v')
            sleep(0.6)
            pyautogui.press('enter')
        else:
            sleep(4.23)
            pyautogui.moveTo(730, 969)
            pyautogui.click()
            pyautogui.typewrite(e)
            pyautogui.press('enter')


viz_dva()
