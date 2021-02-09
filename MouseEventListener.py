import pynput, time

class MouseEventListen:
    def __init__(self):
        self.positionMessageQueue = []
        
    def on_move(x, y):
        print('Pointer moved to {0}'.format((x, y)))
    
    def on_click(self,x, y, button, pressed):
#        self.positionMessageQueue.append((x,y))
#        print("positionMessageQueue: {0}".format(self.positionMessageQueue))
#        print('{0} at {1} dumpInfo'.format(
#            'Pressed' if pressed else 'Released',
#            (x, y)))
        if pressed:
            self.positionMessageQueue.append((x,y))
            print(self.positionMessageQueue)
        if not pressed:
            # Stop listener
            return False
    
    def on_scroll(x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))
    
    def dumpInfo(self):
        print("positionMessageQueue: {0}".format(self.positionMessageQueue))
        
    def run(self):
        # Collect events until released
        with pynput.mouse.Listener(
                on_click=on_click) as listener:
            listener.join()

def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))


def main1():
    # Collect events until released
    print("hello world")
    while True:
        with pynput.mouse.Listener(
                on_click=on_click) as listener:
            listener.join()
    
        
def main2():
    with pynput.mouse.Events() as event:
        for i in event:
            if isinstance(i,pynput.mouse.Events.Move):
                print(i.x,i.y)
                
            elif isinstance(i,pynput.mouse.Events.Click):
                print(i.x,i.y,i.button,i.pressed)
                
            elif isinstance(i,pynput.mouse.Events.Scroll):
                print(i.x,i.y,i.dx,i.dy)
            
            break
    i = event.get(1)

def main3():
    mMouseEventListener = MouseEventListen()
    mMouseEventListener.run()
    

if __name__ == "__main__":
    main2()
        
