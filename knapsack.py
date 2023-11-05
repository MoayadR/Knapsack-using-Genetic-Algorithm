from random import randint

n = int(input())
c = int(input())
w = [0] * (n)
v = [0] * (n)

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


#evaluate teh fitness of each chromosomes
chromosomes = [c1, c2, c3, c4]
def cumulative_fitness  (chromosomes, v):
    arr_cum = [0] * len(chromosomes)
    sum = 0
    for i in range(len(chromosomes)):
        sum += get_value(chromosomes[i], v)
        arr_cum[i] = sum
    return arr_cum  

chromosomes_cumulative_sum = cumulative_fitness(chromosomes, v)
def get_rand(chromosomes_cumulative_sum):
    random_num = randint(0,chromosomes_cumulative_sum[-1])
    return random_num


