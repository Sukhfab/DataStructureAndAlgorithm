'''
sets: are unique (has no order)
Map is a set based data structure Map = <keys, Value>
basically keys are unique and hence we use set to store them
'''

locations = {
    'North America': {
        'USA': ['Mountain View','Atlanta'],
    },
    'Asia': {
        'India': ['zangalore'],
        'China': ['Shanghai']
    },
    'Africa': {'Egypt': ['Caira']},
    }

us_cities = sorted(locations['North America']['USA'])
print("1")
for x in us_cities:
    print(x)

asia_cities = locations['Asia'].items()
print("2")

city = []
for country, cities in asia_cities:
    city.append([cities, country])
sorted_city = sorted(city)
for country,city in sorted_city:
    print(f"{country[0]} - {city}")








"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""