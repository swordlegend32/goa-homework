

def FindNumbers():
    s = []
    count = 0
    for x in range(1,200):
        count = 13 * x
        int(count)
        s.insert(len(s),count)
    print(len(s))
    print(s)

FindNumbers()

