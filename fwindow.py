import ctypes
import pyautogui
import win32console
import win32gui
import threading
def fetch_application_name(window_title):
    """
    :param window_title: the title of the window
    :return: a string with the name of the application or the website's name.
    """
    if " — Mozilla Firefox" in window_title:
            return "SITE: "+window_title.replace(" — Mozilla Firefox", "")
    elif " - Google Chrome" in window_title:
        return "SITE: "+window_title.replace(" - Google Chrome", "")
    else:
        return window_title;

def get_active_window_title():
    """
    Gets the current window if there is any, if not, returns just None.
    :return: the title of the active window, if none, returns None
    """
    try:
        title = pyautogui.getActiveWindow().title
        return title
    except Exception as e:
        return None

def escape_from_reality():
    """
    Escapes tf out of reality by hiding the window, goes in the shadow realm.
    """
    win32gui.ShowWindow(win32console.GetConsoleWindow(), 0)

def show_message(title, message):
    """
    This uses a different thread because the user has to click "OK" in order for the code to continue,
    however, if we just use a different thread, we don't have to wait, and we can continue the code.
    :param title: What we want the title of the window to be.
    :param message: The message inside the window, trollface?
    """
    def message_thread(title, message):
        ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)
    thread = threading.Thread(target=message_thread, args=(title, message))
    thread.start()