class demo:
    def sum(a,b):
        return a+b;
class sub(demo):
    def pro(a,b):
        return a*b;

class run(sub):
    def pro(a,b):
        return a-b;
print(issubclass(sub,demo))
print(issubclass(run,demo))
