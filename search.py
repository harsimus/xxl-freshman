import billboard

"""
Ok! I need to:
1. Insert an artist name
2. Insert an end date for how far I want to go back
3. Insert a starting date
4. A chart category
5. Then need to iterate through chart looking for artist name, chart will be built new each time with chart.previousDate

"""

name = '2 Chainz'
category = 'hot-100'
start = '2017-07-15'
end = '2017-07-01'

def count(name, chart):
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

def search(name, category, start, end):
    current = start

    while current != end:
        chart = billboard.ChartData(category, current)
        current = chart.previousDate

    return count

print search(name, category, start, end)
# print chart.previousDate
# print chart[1]
# print chart[1].weeks

# should print 3!



#
# def search():
#     if done:
#         return counter
#     else:
#         search(name, chart, chart.previousDate)
