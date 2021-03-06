# * Tuples are not just immutable lists

# ** Tuples as records

# Example 2.7 - Tuples used as records
lax_coordinates = (33.9435, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s%s' % passport)

for country, _ in traveler_ids:
    print(country)

# ** Tuple unpacking
lax_coordinates = (33.9435, -118.408056)
latitude, longitude = lax_coordinates
latitude
longitude

divmod(20, 8)

t = (20, 8)
divmod(*t)

quotient, remainder = divmod(*t)
quotient, remainder

# ** Using * to grab excess items
a, b, *rest = range(5)
a, b, rest
a, b, *rest = range(3)
a, b, rest
a, b, *rest = range(2)
a, b, rest

a, *body, c, d = range(5)
a, body, c, d

*head, b, c, d = range(5)
head, b, c, d

# ** Nested tuple unpacking

# Example 2.8 - Unpacking nested tuples to access the longitude
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

# ** Named tuples

# Example 2.9 - Defining and using a named tuple type
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
tokyo
tokyo.population
tokyo.coordinates

# Example 2.10 - Named tuple attributes and methods
City._fields
LatLong = namedtuple('Latlong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
delhi._asdict()

for key, value in delhi._asdict().items():
    print(key + ':', value)
