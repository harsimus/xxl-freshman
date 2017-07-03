import billboard
chart = billboard.ChartData('hot-100')

def search(name, date, chart):
    counter = 0
    currentChart = billboard.ChartData(chart, date)
    currentChartLength = len(currentChart)

    for x in range(currentChartLength):
        currentSong = currentChart[x]
        nameLength = len(name)
        currentName = currentSong.artist
        if currentName[0:nameLength] == name:
            counter += 1

    return counter

print search('2 Chainz', chart.date, 'hot-100')
#
# print chart[1]
