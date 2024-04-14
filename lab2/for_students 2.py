from itertools import compress
import random
import time
import matplotlib.pyplot as plt

from data import *

def initial_population(individual_size, population_size):
    return [[random.choice([True, False]) for _ in range(individual_size)] for _ in range(population_size)]

def fitness(items, knapsack_max_capacity, individual):
    total_weight = sum(compress(items['Weight'], individual))
    if total_weight > knapsack_max_capacity:
        return 0
    return sum(compress(items['Value'], individual))

def population_best(items, knapsack_max_capacity, population):
    best_individual = None
    best_individual_fitness = -1
    for individual in population:
        individual_fitness = fitness(items, knapsack_max_capacity, individual)
        if individual_fitness > best_individual_fitness:
            best_individual = individual
            best_individual_fitness = individual_fitness
    return best_individual, best_individual_fitness


def get_fitness_score(individual):
    return fitness(items, knapsack_max_capacity, individual)

def selection_tournament(population, n_selection):
    selected_population = []
    for i in range(n_selection):
        walka = random.sample(population, 2)
        if get_fitness_score(walka[0]) > get_fitness_score(walka[1]):
            selected_population.append(walka[0])
        else:
            selected_population.append(walka[1])
    return selected_population

def roulette_selection(items, knapsack_max_capacity, population, n_selection):

    fitness_scores = []
    for individual in population: #obliczenie wartosci funkcji celu dla kazdego osobnika
        score = fitness(items, knapsack_max_capacity, individual)
        fitness_scores.append(score)
    total_fitness = 0
    for score in fitness_scores: #obliczenie sumy wartosci funkcji celu dla wszystkich osobnikow
        total_fitness += score
    probabilities = []
    for score in fitness_scores: #obliczenie prawdopodobienstwa wyboru kazdego osobnika
        probability = score / total_fitness
        probabilities.append(probability)
    selected_population = []
    for _ in range(n_selection): #wybor 20 osobnikow z populacji
        selected_individual = random.choices(population, weights=probabilities)[0]
        selected_population.append(selected_individual)
    return selected_population

def crossover_doublePoint(selected_pop):
    children = []
    for _i in range(n_selection//2): #wybor 45 dzieci //tutaj zmienic !!!!
        parent1 = random.choice(selected_pop)
        parent2 = random.choice(selected_pop)
        while parent1 == parent2:
            parent2 = random.choice(selected_pop)
        crossover_point1 = random.randint(0, len(parent1))
        crossover_point2 = random.randint(0, len(parent1))
        while crossover_point2 < crossover_point1:
                crossover_point2 = random.randint(0, len(parent1))
        child1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
        child2 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:]   
        children.append(child1)
        children.append(child2)
    return children
    
def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = not individual[i]
    return individual

def get_fitness_score(individual):
    return fitness(items, knapsack_max_capacity, individual)

items, knapsack_max_capacity = get_big()
print(items)

population_size = 100
generations = 300
n_elite = 10
n_selection = population_size - n_elite

probability_of_mutation = 0.05

start_time = time.time()
best_solution = None
best_fitness = 0
population_history = []
best_history = []
population = initial_population(len(items), population_size)
for _ in range(generations):
    population_history.append(population)

    # TODO: implement genetic algorithm
    #selected_pop = roulette_selection(items, knapsack_max_capacity, population, n_selection) #wybor 20 najlepszych osobnikow z populacji
    
    selected_pop = selection_tournament(population, n_selection)
    
    children = crossover_doublePoint(selected_pop) #poprawnic krzyzowanie
    
    for child in children:
        mutation(child, probability_of_mutation) 
    
    sorted_population = sorted(population, key=get_fitness_score, reverse=True) 
    elites = sorted_population[:n_elite] 
    population = elites + children 
    
    
    best_individual, best_individual_fitness = population_best(items, knapsack_max_capacity, population)
    if best_individual_fitness > best_fitness:
        best_solution = best_individual
        best_fitness = best_individual_fitness
    best_history.append(best_fitness)

end_time = time.time()
total_time = end_time - start_time
print('Best solution:', list(compress(items['Name'], best_solution)))
print('Best solution value:', best_fitness)
print('Time: ', total_time)

# plot generations
x = []
y = []
top_best = 100
for i, population in enumerate(population_history):
    plotted_individuals = min(len(population), top_best)
    x.extend([i] * plotted_individuals)
    population_fitnesses = [fitness(items, knapsack_max_capacity, individual) for individual in population]
    population_fitnesses.sort(reverse=True)
    y.extend(population_fitnesses[:plotted_individuals])
plt.scatter(x, y, marker='.')
plt.plot(best_history, 'r')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.show()
