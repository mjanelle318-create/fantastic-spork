def addnumbers(a=0, b=0):
    return a + b

def subtractingnumbers(a=0, b=0):
    return a-b

def multiplyingnumbers(a=1, b=1):
    return a*b

def dividenumbers(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("error! can't divide by 0")
    except ValueError:
        print('error! not a numerical value')
    except:
        print('error!')