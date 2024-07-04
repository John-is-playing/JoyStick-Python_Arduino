from gserc import get_serial_port
import serial
import pyautogui
import keyboard
import vgamepad


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01
gamepad = vgamepad.VX360Gamepad()
A = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A
port = get_serial_port()
ser = serial.Serial(port, 9600, timeout=1)
dp = False

while True:
    if ser.is_open:
        while True:
            try:
                data = ser.readline().decode('utf-8')
            except UnicodeDecodeError:
                print("UnicodeDecodeError")
                continue
            else:
                break
        if data:
            data = data.strip()
        if data.startswith("x"):
            data = data.split("x")[1]
            data = data.split("y")
            new = []
            for d in data:
                d = int(d)
                new.append(d)
            x, y = new
            if x != 0 and y != 0:
                if x > 0 and y == 0:
                    pyautogui.moveRel(x - 40, -y - 40, duration=0.05)  # move right 
                elif x < 0 and y == 0:
                    pyautogui.moveRel(x - 40, -y - 40, duration=0.05)  # move left
                elif x == 0 and y > 0:
                    pyautogui.moveRel(x - 40, -y - 40, duration=0.05)  # move down
                elif x == 0 and y < 0:
                    pyautogui.moveRel(x - 40, -y - 40, duration=0.05)  # move up
                elif x > 0 and y > 0:
                    pyautogui.moveRel(x - 40, -y - 40, duration=0.05)  # move right and down
                elif x < 0 and y > 0:
                    pyautogui.moveRel(x - 40, -y - 40, duration=0.05)  # move left and down
                elif x > 0 and y < 0:
                    pyautogui.moveRel(x - 40, -y - 40, duration=0.05)  # move right and up
                elif x < 0 and y < 0:
                    pyautogui.moveRel(x - 40, -y - 40, duration=0.05)  # move left and up
            else:
                pyautogui.moveRel(x, -y, duration=0.05)  # stop
        else:
            if data == "D":
                pyautogui.leftClick()
            elif data == "B":
                pyautogui.rightClick()
            elif data == "E":
                pyautogui.press("e")                
            elif data == "A":
                pyautogui.scroll(-3)
            elif data == "C":
                pyautogui.scroll(6)
            elif data == "F_":
                gamepad.press_button(A)
                gamepad.update()
            elif data == "F-":
                gamepad.release_button(A)
                gamepad.update()
    else:
        break
    print(data)
