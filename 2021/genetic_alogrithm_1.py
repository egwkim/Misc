import random, copy

class Route:
    length = 10
    
    def __init__(self, route):
        self.route = route
        self.evaluate()

    def __lt__(self, other):
        return self.fitness < other.fitness

    def evaluate(self):
        e = 0
        
        e += ((1 - self.route[0]) ** 2 + 0.1) ** 0.5
        for i in range(Route.length - 1):
            e += ((self.route[i] - self.route[i+1]) ** 2 + 0.1) ** 0.5
        e += (self.route[-1] ** 2 + 0.1) ** 0.5

        if 0.25 < self.route[6] < 0.5:
            e += 2
        
        '''
        for i in self.route:
            e += i
        '''

        self.fitness = e

    def crossover(self, route):
        r = []
        for i in range(Route.length):
            if random.randint(0, 1):
                r.append(self.route[i])
            else:
                r.append(route.route[i])
        return Route(r)

    def mutation(self):
        self.route[random.randrange(0, Route.length)] = random.random()
        self.evaluate()


routes = []

for i in range(1000):
    route = []
    for i in range(Route.length):
            route.append(random.random())
    routes.append(Route(route))

routes.sort()


for i in range(500):
    new_routes = []

    best = copy.deepcopy(routes[:20])
    new_routes += random.sample(routes, counts=range(len(routes), 0, -1), k=100)
    new_routes += routes[:100]


    for i in range(780):
        new_routes.append(random.choice(routes).crossover(random.choice(routes)))

    for i in range(250):
        random.choice(new_routes).mutation()

    new_routes += best

    new_routes.sort()
    

    routes = new_routes
    
    print(routes[0].fitness)

print(routes[0].route)
