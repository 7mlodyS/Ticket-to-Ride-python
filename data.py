colors = ['white', 'black', 'red', 'blue', 'pink', 'green', 'orange', 'yellow']

cities =['Lisboa', 'Cadiz', 'Madrid', 'Barcelona', 'Pamplona', 'Marseille', 'Paris', 'Brest', 'Dieppe', 'Bruxelles', 'Zurich', 'Munchen', 'Frankfurt', 'Essen', 'Amsterdam', 'London', 'Edinburgh', 'Berlin', 'Wien', 'Venezia', 'Roma', 'Budapest', 'Zagrab', 'Sarajevo', 'Brindisi', 'Palermo', 'Athina', 'Smyrna', 'Angora', 'Sofia', 'Constantinopole', 'Erzurum', 'Sochi', 'Sevastopol', 'Bucuresti', 'Rostov', 'Kharkov', 'Kyiv', 'Smolensk', 'Wilno', 'Warszawa', 'Danzic', 'Moskva', 'Riga', 'Petrograd', 'Stockholm', 'Kobenhavn']

routes = [{
    'city1' : 'Lisboa',
    'city2' : 'Madrid',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'pink',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Lisboa',
    'city2' : 'Cadiz',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'blue',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Cadiz',
    'city2' : 'Madrid',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'orange',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Madrid',
    'city2' : 'Barcelona',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'yellow',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Madrid',
    'city2' : 'Pamplona',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'white',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Madrid',
    'city2' : 'Pamplona',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'black',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Barcelona',
    'city2' : 'Pamplona',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Barcelona',
    'city2' : 'Marseille',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Pamplona',
    'city2' : 'Marseille',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'red',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Pamplona',
    'city2' : 'Paris',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'green',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Pamplona',
    'city2' : 'Paris',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'blue',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Pamplona',
    'city2' : 'Brest',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'pink',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Brest',
    'city2' : 'Paris',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'black',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Brest',
    'city2' : 'Dieppe',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'orange',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Paris',
    'city2' : 'Dieppe',
    'length' : 1,
    'locomotives' : 0,
    'color' : 'pink',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Paris',
    'city2' : 'Marseille',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Paris',
    'city2' : 'Bruxelles',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'yellow',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Paris',
    'city2' : 'Bruxelles',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'red',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Dieppe',
    'city2' : 'Bruxelles',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'green',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Dieppe',
    'city2' : 'London',
    'length' : 2,
    'locomotives' : 1,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Dieppe',
    'city2' : 'London',
    'length' : 2,
    'locomotives' : 1,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'London',
    'city2' : 'Amsterdam',
    'length' : 2,
    'locomotives' : 2,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'London',
    'city2' : 'Edinburgh',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'black',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'London',
    'city2' : 'Edinburgh',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'orange',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Amsterdam',
    'city2' : 'Essen',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'yellow',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Amsterdam',
    'city2' : 'Bruxelles',
    'length' : 1,
    'locomotives' : 0,
    'color' : 'black',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Amsterdam',
    'city2' : 'Frankfurt',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'white',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Bruxelles',
    'city2' : 'Frankfurt',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'blue',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Paris',
    'city2' : 'Frankfurt',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'white',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Paris',
    'city2' : 'Frankfurt',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'orange',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Frankfurt',
    'city2' : 'Essen',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'green',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Frankfurt',
    'city2' : 'Munchen',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'pink',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Paris',
    'city2' : 'Zurich',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Marseille',
    'city2' : 'Zurich',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'pink',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Zurich',
    'city2' : 'Munchen',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'yellow',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Munchen',
    'city2' : 'Venezia',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'blue',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Zurich',
    'city2' : 'Venezia',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'green',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Venezia',
    'city2' : 'Roma',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'black',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Marseille',
    'city2' : 'Roma',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Roma',
    'city2' : 'Brindisi',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'white',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Roma',
    'city2' : 'Palermo',
    'length' : 4,
    'locomotives' : 1,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Brindisi',
    'city2' : 'Athina',
    'length' : 4,
    'locomotives' : 1,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Brindisi',
    'city2' : 'Palermo',
    'length' : 3,
    'locomotives' : 1,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Palermo',
    'city2' : 'Smyrna',
    'length' : 6,
    'locomotives' : 2,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Athina',
    'city2' : 'Smyrna',
    'length' : 2,
    'locomotives' : 1,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Athina',
    'city2' : 'Sarajevo',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'green',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Zagrab',
    'city2' : 'Sarajevo',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'red',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Venezia',
    'city2' : 'Zagrab',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Athina',
    'city2' : 'Sofia',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'pink',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Sarajevo',
    'city2' : 'Sofia',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Sofia',
    'city2' : 'Constatntinopole',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'blue',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Smyrna',
    'city2' : 'Constantinopole',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Angora',
    'city2' : 'Smyrna',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'orange',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Constantinopole',
    'city2' : 'Angora',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Angora',
    'city2' : 'Erzurum',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'black',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Erzurum',
    'city2' : 'Sochi',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'red',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Erzurum',
    'city2' : 'Sevastopol',
    'length' : 4,
    'locomotives' : 2,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Constantinopole',
    'city2' : 'Sevastopol',
    'length' : 4,
    'locomotives' : 2,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Sevastopol',
    'city2' : 'Sochi',
    'length' : 2,
    'locomotives' : 1,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Sochi',
    'city2' : 'Rostov',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Sevastopol',
    'city2' : 'Rostov',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Bucuresti',
    'city2' : 'Constantinopole',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'yellow',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Bucuresti',
    'city2' : 'Sevastopol',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'white',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Sofia',
    'city2' : 'Bucuresti',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Rostov',
    'city2' : 'Kharkov',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'green',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Kharkov',
    'city2' : 'Kyiv',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Kyiv',
    'city2' : 'Bucuresti',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Budapest',
    'city2' : 'Bucuresti',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Budapest',
    'city2' : 'Kyiv',
    'length' : 6,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : True,
    'is_claimed' : False
},{
    'city1' : 'Budapest',
    'city2' : 'Sarajevo',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'pink',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Budapest',
    'city2' : 'Zagrab',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'orange',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Wien',
    'city2' : 'Budapest',
    'length' : 1,
    'locomotives' : 0,
    'color' : 'red',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Wien',
    'city2' : 'Budapest',
    'length' : 1,
    'locomotives' : 0,
    'color' : 'white',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Wien',
    'city2' : 'Zagrab',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Munchen',
    'city2' : 'Wien',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'orange',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Frankfurt',
    'city2' : 'Berlin',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'red',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Frankfurt',
    'city2' : 'Berlin',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'black',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Berlin',
    'city2' : 'Wien',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'green',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Berlin',
    'city2' : 'Essen',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'blue',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Essen',
    'city2' : 'Kobehavn',
    'length' : 3,
    'locomotives' : 1,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Essen',
    'city2' : 'Kobehavn',
    'length' : 3,
    'locomotives' : 1,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Kobehavn',
    'city2' : 'Stockholm',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'white',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Kobehavn',
    'city2' : 'Stockholm',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'yellow',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Berlin',
    'city2' : 'Danzic',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'yellow',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Berlin',
    'city2' : 'Warszawa',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'pink',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Warszawa',
    'city2' : 'Wien',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'blue',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Warszawa',
    'city2' : 'Kyiv',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Warszawa',
    'city2' : 'Wilno',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'red',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Warszawa',
    'city2' : 'Danzic',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Wilno',
    'city2' : 'Kyiv',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Kyiv',
    'city2' : 'Smolensk',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'red',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Wilno',
    'city2' : 'Smolensk',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'yellow',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Smolensk',
    'city2' : 'Moskva',
    'length' : 2,
    'locomotives' : 0,
    'color' : 'orange',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Moskva',
    'city2' : 'Kharkov',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Moskva',
    'city2' : 'Petrograd',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'white',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Danzic',
    'city2' : 'Riga',
    'length' : 3,
    'locomotives' : 0,
    'color' : 'black',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Wilno',
    'city2' : 'Riga',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'green',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Wilno',
    'city2' : 'Petrograd',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'blue',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Riga',
    'city2' : 'Petrograd',
    'length' : 4,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : False,
    'is_claimed' : False
},{
    'city1' : 'Stockholm',
    'city2' : 'Petrograd',
    'length' : 8,
    'locomotives' : 0,
    'color' : 'any',
    'is_tunnel' : True,
    'is_claimed' : False
}]

tickets = [{
    'city1' : 'Lisboa',
    'city2' : 'Danzic',
    'points' : 20
},
{
    'city1' : 'Edinburgh',
    'city2' : 'Athina',
    'points' : 21
},
{
    'city1' : 'Palermo',
    'city2' : 'Moskva',
    'points' : 20
},
{
    'city1' : 'Brest',
    'city2' : 'Petrograd',
    'points' : 20
},{
    'city1' : 'Kobehavn',
    'city2' : 'Erzurum',
    'points' : 21
},{
    'city1' : 'Cadiz',
    'city2' : 'Stockholm',
    'points' : 21
},{
    'city1' : 'Berlin',
    'city2' : 'Roma',
    'points' : 9
},{
    'city1' : 'Barcelona',
    'city2' : 'Bruxelles',
    'points' : 8
},{
    'city1' : 'Amsterdam',
    'city2' : 'Pamplona',
    'points' : 7
},{
    'city1' : 'Brest',
    'city2' : 'Venezia',
    'points' : 8
},{
    'city1' : 'London',
    'city2' : 'Wien',
    'points' : 10
},{
    'city1' : 'Warszawa',
    'city2' : 'Smolensk',
    'points' : 6
},{
    'city1' : 'Angora',
    'city2' : 'Kharkov',
    'points' : 10
},{
    'city1' : 'Athina',
    'city2' : 'Wilno',
    'points' : 11
},{
    'city1' : 'Palermo',
    'city2' : 'Constatntinopole',
    'points' : 8
},{
    'city1' : 'Budapest',
    'city2' : 'Sofia',
    'points' : 5
},{
    'city1' : 'Sofia',
    'city2' : 'Smyrna',
    'points' : 5
},{
    'city1' : 'Paris',
    'city2' : 'Wien',
    'points' : 8
},{
    'city1' : 'London',
    'city2' : 'Berlin',
    'points' : 7
},{
    'city1' : 'Roma',
    'city2' : 'Smyrna',
    'points' : 8
},{
    'city1' : 'Paris',
    'city2' : 'Zagrab',
    'points' : 7
},{
    'city1' : 'Zurich',
    'city2' : 'Brindisi',
    'points' : 6
},{
    'city1' : 'Stockholm',
    'city2' : 'Wien',
    'points' : 11
},{
    'city1' : 'Frankfurt',
    'city2' : 'Kobehavn',
    'points' : 5
},{
    'city1' : 'Essen',
    'city2' : 'Kyiv',
    'points' : 10
},{
    'city1' : 'Kyiv',
    'city2' : 'Petrograd',
    'points' : 6
},{
    'city1' : 'Frankfurt',
    'city2' : 'Smolensk',
    'points' : 13
},{
    'city1' : 'Venezia',
    'city2' : 'Constantinopole',
    'points' : 10
},{
    'city1' : 'Amsterdam',
    'city2' : 'Wilno',
    'points' : 12
},{
    'city1' : 'Berlin',
    'city2' : 'Moskva',
    'points' : 12
},{
    'city1' : 'Athina',
    'city2' : 'Angora',
    'points' : 5
},{
    'city1' : 'Kyiv',
    'city2' : 'Sochi',
    'points' : 8
},{
    'city1' : 'Marseille',
    'city2' : 'Essen',
    'points' : 8
},{
    'city1' : 'Bruxelles',
    'city2' : 'Danzic',
    'points' : 9
},{
    'city1' : 'Madrid',
    'city2' : 'Dieppe',
    'points' : 8
},{
    'city1' : 'Zurich',
    'city2' : 'Budapest',
    'points' : 6
},{
    'city1' : 'Riga',
    'city2' : 'Bucuresti',
    'points' : 10
},{
    'city1' : 'Erzurum',
    'city2' : 'Rostov',
    'points' : 5
},{
    'city1' : 'Brest',
    'city2' : 'Marseille',
    'points' : 7
},{
    'city1' : 'Sarajevo',
    'city2' : 'Sevastopol',
    'points' : 8
},{
    'city1' : 'Barcelona',
    'city2' : 'Munchen',
    'points' : 8
},{
    'city1' : 'Berlin',
    'city2' : 'Bucuresti',
    'points' : 8
},{
    'city1' : 'Edinburgh',
    'city2' : 'Paris',
    'points' : 7
},{
    'city1' : 'Smolensk',
    'city2' : 'Rostov',
    'points' : 8
},{
    'city1' : 'Madrid',
    'city2' : 'Zurich',
    'points' : 8
},{
    'city1' : 'Zagrab',
    'city2' : 'Brindisi',
    'points' : 6
}]


class GameData():
    def __init__(self):
        self.colors = colors
        self.cities = cities
        self.routes = routes
        self.tickets = tickets