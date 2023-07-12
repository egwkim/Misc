# Use genetic algorithm to get the best initial state

import numpy as np
import matplotlib.pyplot as plt

G = 1
M = 3000000
duration = 10
dt = 0.01
frequency_factor = 4
max_frequency = 440
min_frequency = 110
max_d = 250
gene_factor = 150
small_mutation_factor = 0.5


class Sun:
    def __init__(self, m):
        self.x = 0
        self.y = 0
        self.m = m


class Planet:
    def __init__(self, x, y, vx, vy, sun):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.v = None
        self.sun: Sun = sun
        self.d = np.sqrt(self.get_d2())
        self.update_v()

    def update_v(self):
        self.v = np.sqrt(self.vx**2 + self.vy**2)

    def get_d2(self):
        dx = self.x - self.sun.x
        dy = self.y - self.sun.y
        d2 = dx**2 + dy**2
        return d2

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Apply gravity caused by the sun
        dx = self.x - self.sun.x
        dy = self.y - self.sun.y
        d2 = dx**2 + dy**2
        d = np.sqrt(d2)
        self.d = d
        if d2 == 0:
            return
        a = G * self.sun.m / d2
        self.vx -= a * dt * dx / d
        self.vy -= a * dt * dy / d
        self.update_v()


# TODO Improve ratio sweetness function
def ratio_sweetness(ratio):
    if ratio <= 0:
        return -1
    if ratio < 1:
        ratio = 1 / ratio

    fitness = 1 - abs(ratio - 1.5)

    return fitness


class Gene:
    def __init__(self, gene=np.random.rand(6) * gene_factor):
        self.gene_length = 6
        self.gene = gene
        self._fitness = None

    # TODO Improve fitness function
    @property
    def fitness(self):
        if self._fitness is not None:
            return self._fitness

        fitness_sum = 0

        s = Sun(M)
        p1 = Planet(100, 0, self.gene[0], self.gene[1], s)
        p2 = Planet(self.gene[2], self.gene[3], self.gene[4], 0, s)

        for i in np.arange(0, duration, dt):
            fitness_sum += ratio_sweetness(p1.v / p2.v)
            fitness_sum -= (max(frequency_factor * p1.v - max_frequency, 0)) / 400
            fitness_sum -= (max(frequency_factor * p2.v - max_frequency, 0)) / 400
            fitness_sum -= (max(min_frequency - frequency_factor * p1.v, 0)) / 100
            fitness_sum -= (max(min_frequency - frequency_factor * p2.v, 0)) / 100
            fitness_sum -= max(p1.d - max_d, 0) / 100
            fitness_sum -= max(p2.d - max_d, 0) / 100
            p1.move(dt)
            p2.move(dt)

        return fitness_sum

    def debug(self):
        s = Sun(M)
        p1 = Planet(0, self.gene[0], self.gene[1], self.gene[2], s)
        p2 = Planet(self.gene[3], self.gene[4], self.gene[5], 0, s)
        x1 = []
        y1 = []
        x2 = []
        y2 = []
        for i in np.arange(0, duration, dt):
            x1.append(p1.x)
            y1.append(p1.y)
            x2.append(p2.x)
            y2.append(p2.y)
            p1.move(dt)
            p2.move(dt)
        plt.plot(x1, y1, "o")
        plt.plot(x2, y2, "o")
        plt.savefig("data.png")


class GeneticAlgorithm:
    def __init__(self, population):
        self.population = population
        self.genes = [Gene() for _ in range(population)]
        self.sorted = False

    def sort(self):
        self.genes.sort(key=lambda x: x.fitness, reverse=True)
        self.sorted = True

    def next_generation(self):
        if not sorted:
            self.sort()
        top = self.population // 8
        crossover = self.population * 2 // 8
        mutation1 = self.population * 2 // 8
        mutation2 = self.population - top - crossover - mutation1

        top_genes = self.genes[:top]
        new_genes = []
        new_genes += top_genes

        for i in range(crossover):
            parents = np.random.choice(top_genes, 2, replace=False)
            gene = []
            for j in range(parents[0].gene_length):
                gene.append(parents[np.random.randint(2)].gene[j])
            new_genes.append(Gene(np.array(gene)))

        for i in range(mutation1):
            mutate_gene = Gene(np.array([*np.random.choice(new_genes, 1)[0].gene]))
            for j in range(mutate_gene.gene_length):
                if np.random.rand() < 0.5:
                    mutate_gene.gene[j] = np.random.rand(1)[0] * gene_factor
            new_genes.append(mutate_gene)

        for i in range(mutation2):
            mutate_gene = Gene(np.array([*np.random.choice(new_genes, 1)[0].gene]))
            mutate_gene.gene += (
                np.random.rand(mutate_gene.gene_length) * small_mutation_factor
            )
            new_genes.append(mutate_gene)

        self.genes = new_genes
        self.sorted = False


def main():
    ga = GeneticAlgorithm(100)
    for i in range(100):
        ga.next_generation()
        ga.sort()
        print(ga.genes[0].fitness)

    ga.genes[0].debug()
    print(list(ga.genes[0].gene))


if __name__ == "__main__":
    main()
