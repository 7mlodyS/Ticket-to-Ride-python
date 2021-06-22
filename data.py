colors = ['white', 'black', 'red', 'blue', 'pink', 'green', 'orange', 'yellow', 'any']

cities =['Berlin', 'Warszawa', 'Danzic', 'Kyiv', 'Wilno', 'Wien', 'Essen', 'Kobehavn', 'Pampelona']

routes = [{
    'city1' : 'Warszawa',
    'city2' : 'Berlin',
    'length' : 4,
    'locomotives' : 0,
    'data' : [['yellow', False], ['pink', False]],
    'is_tunnel' : False
},
{
    'city1' : 'Berlin',
    'city2' : 'Wien',
    'length' : 3,
    'locomotives' : 0,
    'data' : [['green', False]],
    'is_tunnel' : False
},
{
    'city1' : 'Warszawa',
    'city2' : 'Wien',
    'length' : 4,
    'locomotives' : 0,
    'data' : [['blue', False]],
    'is_tunnel' : False
},
{
    'city1' : 'Warszawa',
    'city2' : 'Kyiv',
    'length' : 4,
    'locomotives' : 0,
    'data' : [['any', False]],
    'is_tunnel' : False
},
{
    'city1' : 'Warszawa',
    'city2' : 'Wilno',
    'length' : 3,
    'locomotives' : 0,
    'data' : [['red', False]],
    'is_tunnel' : False
},
{
    'city1' : 'Warszawa',
    'city2' : 'Danzic',
    'length' : 2,
    'locomotives' : 0,
    'data' : [['any', False]],
    'is_tunnel' : False
},
{
    'city1' : 'Danzic',
    'city2' : 'Berlin',
    'length' : 4,
    'locomotives' : 0,
    'data' : [['any', False]],
    'is_tunnel' : False
},
{
    'city1' : 'Kyiv',
    'city2' : 'Wilno',
    'length' : 2,
    'locomotives' : 0,
    'data' : [['any', False]],
    'is_tunnel' : False
},
{
    'city1' : 'Essen',
    'city2' : 'Kobehavn',
    'length' : 3,
    'locomotives' : 1,
    'data' : [['any', False]],
    'is_tunnel' : False
},
{
    'city1' : 'Madrid',
    'city2' : 'Pampelona',
    'length' : 3,
    'locomotives' : 0,
    'data' : [['black', False], ['white', False]],
    'is_tunnel' : True
}]

tickets = [{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'points' : 5
},
{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'points' : 5
},
{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'points' : 5
},
{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'points' : 5
},
{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'points' : 5
},
{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'points' : 5
},
{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'points' : 5
},
{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'points' : 5
},
{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'points' : 5
},
{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'points' : 5
},
{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'points' : 5
},
{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'points' : 5
}]


class GameData():
    def __init__(self):
        self.colors = colors
        self.cities = cities
        self.routes = routes
        self.tickets = tickets