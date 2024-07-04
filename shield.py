import vgamepad as vg
import time
from gserc import get_serial_port
import serial


port = get_serial_port()
ser = serial.Serial(port, 9600, timeout=1)
# 创建一个虚拟手柄
gamepad = vg.VX360Gamepad()

def process_joystick_data(joystick_data):
    x_data = int(joystick_data[0]) / 100  # 缩放
    y_data = int(joystick_data[1]) / 100  # 缩放
    print(x_data, y_data)
    
    # 设置摇杆数据
    gamepad.left_joystick_float(x_data, y_data)
    gamepad.update()

def process_button_data(button_data):
    button_map = {
        'A': vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
        'B': vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
        'C': vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
        'D': vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
        'E': vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
        "F_": vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK
    }
    
    if button_data in button_map:
        gamepad.press_button(button=button_map[button_data])
        gamepad.update()
        time.sleep(0.2)  # 按键按下后稍微等待
        gamepad.release_button(button=button_map[button_data])
        gamepad.update()

def main():
    while True:
        # 模拟获取输入数据
        while True:
            try:
                input_data = ser.readline().decode().strip()
            except UnicodeDecodeError as e:
                print(e)
                continue
            else:
                break
        if input_data.startswith("x"):
            input_data = input_data[1:].split("y")
            if '' in input_data:
                continue
            input_data = list(map(int, input_data))
            process_joystick_data(input_data)      
            print("a")      
        else:
            process_button_data(input_data)
            print("b")
        print(input_data)
        time.sleep(0.01)  # 稍微等待，避免过于频繁的更新

if __name__ == "__main__":
    main()
