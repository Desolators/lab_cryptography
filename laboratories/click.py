import time

import keyboard
import win32api
import win32con
import win32gui


def set_cursor_pos(x, y):
    win32api.SetCursorPos((x, y))


def click(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.02)


def click_1(x, y):
    set_cursor_pos(x, y)
    click(x, y)


def double_click(x, y):
    set_cursor_pos(x, y)
    click(x, y)
    click(x, y)


def find_window(hwnd):
    return win32gui.FindWindow(None, hwnd)


def show_window(hwnd):
    name = find_window(hwnd)
    win32gui.ShowWindow(name, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(name)


def find_coord_window(hwnd):
    name = find_window(hwnd)
    return win32gui.GetWindowRect(name)


def find_coords_x():
    coords_window = find_coord_window("Дифференциальный криптоанализ")  # Дифференциальный/Линейный
    x_const = int(coords_window[0])
    return x_const


def find_coords_y():
    coords_window = find_coord_window("Дифференциальный криптоанализ")  # Дифференциальный/Линейный
    y_const = int(coords_window[1])
    return y_const


def window_checker(false_name, true_name, x, y):
    set_cursor_pos(x, y)
    click(x, y)
    if find_window(false_name):
        keyboard.send("escape")
    elif find_window(true_name):
        exit()
