import random
import string

# Define the target string and the genetic algorithm parameters
target = "Hello, World!"
population_size = 1000
generations = 1000

# Define the fitness function
def fitness(individual):
    return sum([1 for i, j in zip(individual, target) if i == j])

# Generate the initial population
population = [''.join(random.choices(string.ascii_letters + ' ', k=len(target))) for _ in range(population_size)]

# Run the genetic algorithm
for generation in range(generations):
    # Evaluate the fitness of each individual
    scores = [fitness(individual) for individual in population]
   
    # Select individuals to reproduce based on their fitness
    parents = random.choices(population, weights=scores, k=population_size)
   
    # Create the next generation through crossover and mutation
    population = [parent[:len(target)//2] + random.choice(parents)[len(target)//2:] for parent in parents]
    population = [''.join([char if random.random() > 0.01 else random.choice(string.ascii_letters + ' ') for char in individual]) for individual in population]
   
    # Print the best individual from each generation
    print(max(population, key=fitness))

# Print the final best individual
print("Final best individual: ", max(population, key=fitness))