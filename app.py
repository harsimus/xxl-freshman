import billboard

name = '2 Chainz'
date = '2017-07-08'
cat = 'hot-100'
chart = billboard.ChartData(cat, date)

def search(name, chart):
    counter = 0
    data = chart
    dataLength = len(data)

    for x in range(dataLength):
        entry = data[x]
        nameLength = len(name)
        artist = entry.artist
        if artist[0:nameLength] == name:
            counter += 1

    return counter

print search(name, chart)
print chart[1]
print chart[1].weeks

# should print 3!




def search():
    if done:
        return counter
    else:
        search(name, chart.previousDate)
