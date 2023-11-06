from random import random , randint

n = int(input())
c = int(input())
w = [0] * (n)
v = [0] * (n)
Pc = 0.7
Pm = 0.02

for i in range(0, n):
    w[i] = int(input())
    v[i] = int(input())

#intialization
c1 = [0] * n
c2 = [0] * n
c3 = [0] * n
c4 = [0] * n

for i in range(n):
    c1[i] = randint(0, 1) 
    c2[i] = randint(0, 1) 
    c3[i] = randint(0, 1) 
    c4[i] = randint(0, 1)

print(c1)
print(c2)
print(c3)
print(c4)


def get_weight(chromosome, w):
    weight = 0
    for i in range (n):
        if (chromosome[i]):
            weight += w[i]
    return weight

def get_value(chromosome, v):
    value = 0
    for i in range (n):
        if (chromosome[i]):
            value += v[i]
    return value

def is_feasble(chromosome, w, c):
    return get_weight(chromosome, w) <= c


chromosomes = [c1, c2, c3, c4]
def get_all_value_index_pair(chromosomes , v):
    result = []
    for i in range(len(chromosomes)):
        result.append([get_value(chromosomes[i] , v) , i])

    result = sorted(result , key=lambda x: x[0])
    return result

def rank_chromosomes(chromosomes,v):
    values_indecies = get_all_value_index_pair(chromosomes,v)
    ranks = [1] * len(chromosomes)
    for i in range(len(values_indecies)):
        ranks[values_indecies[i][1]] = i + 1
    return ranks

def cummulative_rank(rank_chromosomes):
    sum_of_ranks = sum(rank_chromosomes)
    current_cummulative = 0
    cummulative = []
    for rank in rank_chromosomes:
        cummulative.append(current_cummulative + (rank/ sum_of_ranks))
        current_cummulative = cummulative[-1]
    return cummulative


def get_rand():
    random_num = random()
    return random_num

# selection 
def rank_selection(n , cummulative_rank):
    for i in range(n):
        num = get_rand()
        for i in range(len(cummulative_rank)):
            if num <= cummulative_rank[i] :
                print(f"We Have Selected Chromosome:{i+1}" , f"The random Number was:{num}")
                break

pairs = get_all_value_index_pair(chromosomes,v)
ranks = rank_chromosomes(chromosomes,v)
cumm_ranks = cummulative_rank(ranks)

print(pairs)
print(ranks)
print(cumm_ranks)
rank_selection(2 , cumm_ranks)