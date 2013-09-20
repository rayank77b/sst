from random import randint, choice

def integer():
    return randint(1,10000)

def text(cnt):
    s=__B()
    for x in range(randint(1,cnt)):
        s=s+__b()
    return s

def __B():
    return choice("WRTZPLKHGFSXVBNMYJ")+choice("aeuio")

def __b():
    return choice("wrtzpsdfghklxycvbnm")+choice("aeuio")

def name():
    s=__B()
    for x in range(randint(1,5)):
        s=s+__b()
    return s

def gender():
    g=('Male','Female')
    return g[randint(0,1)]

def age():
    return randint(20,60)

def date():
    month=randint(1,12)
    if month==2:
        return str(randint(1970,2011))+"-"+str(month)+"-"+str(randint(1,28))
    else:
        return str(randint(1970,2011))+"-"+str(month)+"-"+str(randint(1,30))

addresscnt=10
def set_address_cnt(cnt):
    global addresscnt
    addresscnt=cnt

def address():
    global addresscnt
    return randint(1,addresscnt)

def street():
    return text(10)

def street_nr():
    return randint(1,100)

def zipcode():
    return integer()

def town():
    return text(6)

def state():
    s=('USA', 'Russia', 'Germany', 'Afganistan', 'UK', 'France', 'Luxemburg', 'Italya')
    return s[randint(0,len(s)-1)]

