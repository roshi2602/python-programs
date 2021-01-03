from threading import *
def test():pass
t= Thread(target = test)
t.start()
print("Ff",current_thread().ident)
print("dd", t.ident)
