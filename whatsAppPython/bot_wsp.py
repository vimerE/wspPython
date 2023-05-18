import pyautogui, webbrowser
from time import sleep

#numero = ("948123694","986331608","940334791", "940253783", "927974275", "902468218")
numero = ("948123694","986331608","940334791")

for i in numero:
    webbrowser.open("https://web.whatsapp.com/send?phone="+i)
    sleep(20)

    for i in range(1):
        #pyautogui.typewrite(str(i) + " *Ya llegamos Alfin* " + "\n" + "¿Te gustaría recibir promociones, descuentos y tasas preferenciales en nuestros productos financieros? \n")
        pyautogui.typewrite(" *Ya llegamos Alfin* " + "\n" + "¿Te gustaría recibir promociones, descuentos y tasas preferenciales en nuestros productos financieros? \n")
        pyautogui.typewrite("responde Si, si estás interesado y en breve nos comunicaremos contigo \n https://www.google.com/")
        pyautogui.press("enter")
        sleep(5)
        #print(pyautogui.position())
        pyautogui.click(x=288, y=70, button='left')


# Nos da la posición del ratón
#print(pyautogui.position())

# Posiciones del ratón y click *Ya llegamos Alfin* 
#pyautogui.click(x=288, y=70, button='left')


#sleep(30)
"""for i in range(25):
    pyautogui.typewrite(str(i) + "*Ya llegamos Alfin*" + "\n" + "¿Te gustaría recibir promociones, descuentos y tasas preferenciales en nuestros productos financieros? \n responde Si, si estás interesado")
    pyautogui.press("enter")"""

