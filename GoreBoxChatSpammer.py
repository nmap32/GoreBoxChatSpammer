import keyboard
import random
import time

print("Press Insert To Start")

start_time = time.time()
while True:
    if keyboard.is_pressed('insert'):
        keyboard.press('c')
        time.sleep(0.1)  # задержка после нажатия клавиши "C"
        keyboard.release('c')
        time.sleep(0.1)  # задержка перед вводом случайного текста
        random_text = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=random.randint(128, 256)))
        keyboard.write(random_text)
        time.sleep(0.1)
        keyboard.press('enter')
        keyboard.release('enter')
        keyboard.release_all()
        time.sleep(0.1)