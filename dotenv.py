
values = {}

def init():
    with open(".env") as f:
        for x in f:
            foo = x.split(" = ")
            values[foo[0]] = foo[1].replace('\n', '')

def getKey(name):
    try:
        if not values[name].isnumeric():
            return values[name]
        else:
            return int(values[name])
    except KeyError:
        return None

def isKey(name):
    try:
        if values[name]:
            return True
        else:
            return False
    except KeyError:
        return False

def setKey(name, value):
    values[name] = value
    with open(".env", "w") as f:
        for v in values:
            f.write(f"{v} = {values[v]}\n")
