from random import random , randint
from copy import deepcopy

#intialization
def initialize_chromosome(n : int) -> list:
    c = [0] * n
    for i in range(n):
        c[i] = randint(0,1)
    return c

def create_chromosomes(n:int , population_size:int) -> list[list]:
    chromosomes =[]
    for i in range(population_size):
        chromosomes.append(initialize_chromosome(n))
    return chromosomes



def get_weight(chromosome:list , w:list) -> int:
    weight = 0
    for i in range (len(chromosome)):
        if (chromosome[i]):
            weight += w[i]
    return weight

def get_value(chromosome:list, v:list) -> int:
    value = 0
    for i in range (len(chromosome)):
        if (chromosome[i]):
            value += v[i]
    return value

def is_feasible(chromosome:list, w:list, c:int) -> bool:
    return get_weight(chromosome, w) <= c


def get_all_value_index_pair(chromosomes:list[list] , v:list) ->list[list]:
    result = []
    for i in range(len(chromosomes)):
        result.append([get_value(chromosomes[i] , v) , i])

    result = sorted(result , key=lambda x: x[0])
    return result

def rank_chromosomes(chromosomes:list[list],v:list) -> list:
    values_indecies = get_all_value_index_pair(chromosomes,v)
    ranks = [1] * len(chromosomes)
    for i in range(len(values_indecies)):
        ranks[values_indecies[i][1]] = i + 1
    return ranks

def cummulative_rank(rank_chromosomes:list) -> list:
    sum_of_ranks = sum(rank_chromosomes)
    current_cummulative = 0
    cummulative = []
    for rank in rank_chromosomes:
        cummulative.append(current_cummulative + (rank/ sum_of_ranks))
        current_cummulative = cummulative[-1]
    return cummulative


def get_rand() -> float:
    random_num = random()
    return random_num

# selection 
def rank_selection(n:int , cummulative_rank:list) -> list:
    selected = []
    for i in range(n):
        num = get_rand()
        for i in range(len(cummulative_rank)):
            if num <= cummulative_rank[i] :
                selected.append(i)
                break
    return selected

# crossover
def crossover_swaper(n_point:int , chromosome1:list , chromosome2:list) -> list[list]:
    new_chromosome1 = chromosome1[0:n_point] + chromosome2[n_point:]
    new_chromosome2 = chromosome2[0:n_point] + chromosome1[n_point:]
    return [new_chromosome1 , new_chromosome2]


def crossover(selected:list , chromosomes:list[list] , Pc:float) -> list[list]:
    offsprings = []
    i = 0
    while(i < len(selected)):
        chrome1 = chromosomes[selected[i]]
        chrome2 = chromosomes[selected[i+1]]
        rand = get_rand()
        if rand <= Pc:
            offsprings.extend(crossover_swaper(randint(1 , len(chrome1)-1) , chrome1 , chrome2))
        else:
            offsprings.append(chrome1)
            offsprings.append(chrome2)
        i+=2
    return offsprings

def mutation(offsprings:list[list] , Pm:float) -> None:
    for offspring in offsprings:
        for i in range(len(offspring)-1):
            rand = get_rand()
            if rand <= Pm:
                offspring[i] = (offspring[i] + 1) % 2 

def is_population_feasiable(population:list[list] , w , c) -> bool:
    for chromosome in population:
        if is_feasible(chromosome , w , c):
            return True
    return False


def parse_input_file(file_path):
    test_cases = []
    knapsack_sizes = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    lines = list(map(lambda x: x.rstrip('\n') , lines))
    lines = list(filter(lambda x : x if x != ' ' else None , lines))

    num_of_testcases = int(lines[0])
    
    i = 1
    for test in range(num_of_testcases):
        knapsack_size = int(lines[i])
        knapsack_sizes.append(knapsack_size)
        i+=1
        num_of_items = int(lines[i])
        i+=1

        w = [0] * num_of_items
        v = [0] * num_of_items

        for j in range(num_of_items):
            temp_line = lines[i].split(' ')
            w[j] = int(temp_line[0])
            v[j] = int(temp_line[1])
            i+=1

        test_cases.append([w , v])

    return test_cases , knapsack_sizes

def main():
    Pc = 0.7
    Pm = 0.02

    # creating chromosomes

    test_cases , knapsack_sizes = parse_input_file('knapsack_input.txt')

    for test_case in range(len(test_cases)):
        print()
        print(f"Test Case:{test_case}")
        n = len(test_cases[test_case][0])
        c = knapsack_sizes[test_case]
        w = test_cases[test_case][0]
        v = test_cases[test_case][1]
        chromosomes = create_chromosomes(n , 4)
        FGBS = [0] * n # final generation feasiable solutions
        FGBS_value = 0
        OABS = [0] * n # overall best solution
        OABS_value = 0
        iteration = 0
        while(iteration <= 100):
        # print()
        # print(f"Iteration: {iteration}")
        # print(f"Chromosomes:{chromosomes}")
            
        # get Best Overall Solution
            for chromosome in chromosomes:
                if is_feasible(chromosome ,w ,c):
                    value = get_value(chromosome , v)
                    if(value > OABS_value):
                        OABS = deepcopy(chromosome)
                        OABS_value = value
            

            # assigning ranks to each chromosome
            ranks = rank_chromosomes(chromosomes,v)
            # print(f"Ranks:{ranks}")

            # getting the cummulative ranks
            cumm_ranks = cummulative_rank(ranks)
            # print(f"Cumm Ranks:{cumm_ranks}")

            # getting selected chromosomes for crossover phase
            selected = rank_selection(4 , cumm_ranks)
            # print(f"Selected{selected}")

            # getting the offsprins from the crossover
            offsprings = crossover(selected , chromosomes , Pc)
            # print(f"offSprings{offsprings}")

            # applying mutation
            mutation(offsprings , Pm)
            # print(f"offSprings after mutation :{offsprings}")

            # Generational replacement
            chromosomes = deepcopy(offsprings)

            # feisable population check
            if is_population_feasiable(chromosomes , w , c):
                iteration+=1
        
        
        # get best solution in the last generation
        for chromosome in chromosomes:
            if is_feasible(chromosome ,w ,c):
                value = get_value(chromosome , v)
                if(value > FGBS_value):
                    FGBS = deepcopy(chromosome)
                    FGBS_value = value

        print(f"Knapsack Size:{c}")
        print(f"Weight of the items:{w}" , f"Value of the items:{v}")
        print(f"Feasible Solution in last Population:{FGBS}")
        print(f"Feasible Num of Selected Items:{FGBS.count(1)}")
        print(f"Feasible Total value of Selected Items:{get_value(FGBS , v)}")
        print(f"Feasible Total weight of Selected Items:{get_weight(FGBS , w)}")
        print()
        print(f"Overall Best Solution:{OABS}")
        print(f"Feasible Num of Selected Items:{OABS.count(1)}")
        print(f"Feasible Total value of Selected Items:{get_value(OABS , v)}")
        print(f"Feasible Total weight of Selected Items:{get_weight(OABS , w)}")


        

   

if __name__ == '__main__':
    main()