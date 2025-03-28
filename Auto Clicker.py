#Basic auto clicker

import pyautogui
import time
import threading

def clicker(delay, button, stop_event):
    """
    Automatically clicks the mouse at a specified interval.

    Args:
        delay (float): The time delay between clicks in seconds.
        button (str): The mouse button to click ('left', 'right', or 'middle').
        stop_event (threading.Event): An event to signal the thread to stop.
    """
    while not stop_event.is_set():
        pyautogui.click(button=button)
        time.sleep(delay)

def main():
    """
    Prompts the user for click settings and starts/stops the clicker.
    """
    try:
        delay = float(input("Enter the delay between clicks (in seconds): "))
        button = input("Enter the mouse button to click (left, right, middle): ").lower()

        if button not in ('left', 'right', 'middle'):
            print("Invalid button. Please enter 'left', 'right', or 'middle'.")
            return

        stop_event = threading.Event()
        click_thread = threading.Thread(target=clicker, args=(delay, button, stop_event))
        click_thread.daemon = True  # Allow the program to exit even if the thread is running
        click_thread.start()

        print("Clicker started. Press Enter to stop...")
        input()  # Wait for Enter key press

        stop_event.set() #Signal the thread to stop
        click_thread.join() #Wait for the thread to actually finish.
        print("Clicker stopped.")

    except ValueError:
        print("Invalid input. Please enter a valid number for the delay.")

if __name__ == "__main__":
    main()