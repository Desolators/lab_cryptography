import time
import keyboard
import win32gui
import win32api
import win32con


def cursor_pos(x, y):
    win32api.SetCursorPos((x, y))


def click(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.02)


def click_0(x, y):
    cursor_pos(x, y)
    click(x, y)


def click_1(x, y):
    cursor_pos(x, y)
    click(x, y)
    click(x, y)


def find_window(hwnd):
    return win32gui.FindWindow(None, hwnd)


def show_window(hwnd):
    name = find_window(hwnd)
    win32gui.ShowWindow(name, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(name)


def coord_window(hwnd):
    name = find_window(hwnd)
    return win32gui.GetWindowRect(name)


def coords_x():
    coords_window = coord_window("Дифференциальный криптоанализ")        #Дифференциальный/Линейный
    x_const = int(coords_window[0])
    return x_const


def coords_y():
    coords_window = coord_window("Дифференциальный криптоанализ")       #Дифференциальный/Линейный
    y_const = int(coords_window[1])
    return y_const


def window_checker(false_name, true_name, x, y):
    cursor_pos(x, y)
    click(x, y)
    if find_window(false_name):
        keyboard.send("escape")
    elif find_window(true_name):
        exit()


key = 10
start_position = [0] * key
a = [0] * key

show_window("Дифференциальный криптоанализ")             #Дифференциальный/Линейный


for j in range(key):
    click_0(coords_x() + 39 + (28 * j), coords_y() + 454)    # coords_y() + 388 (Линейный) + 454 (Дифф)

for k in range(2 ** (len(a))):
    j = len(a) - 1
    while j >= 0 and a[j] == 1:
        a[j] = 0
        click_1(coords_x() + 39 + (28 * j), coords_y() + 454)   # coords_y() + 388 (Линейный) + 454 (Дифф)
        j -= 1
    if j >= 0 and a[j] == 0:
        a[j] = 1
        click_0(coords_x() + 39 + (28 * j), coords_y() + 454)   # coords_y() + 388 (Линейный) + 454 (Дифф)
    window_checker("ошибка", "информация", coords_x() + 80, coords_y() + 619)
    # window_checker coords_y() + 571 (Линейный) + 619 (Дифф)
