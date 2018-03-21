#Task 3 - Singleton 

def UniqueObject(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@UniqueObject
class Star():
    def __init__(self, num):
        self.heart = num

a = Star(123)
b = Star(123)
print(a.heart)
print(a is b)

a.heart = 43534
print(b.heart)