
def printName(arg1, arg2):
    print arg2

def Login(username, password):
    if type(username) is str:
        CheckDatabse(username, password)
    else:
        print "Use Letters!"


username = int(raw_input('input your name'))
password = raw_input('input your password')
Login(username, password)
