import threading

def hello():
    print("Hello Thread")

t = threading.Thread(target=hello)
t.start()
