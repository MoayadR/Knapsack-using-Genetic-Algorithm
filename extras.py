"""Roulette Selection Method """
# # evaluate teh fitness of each chromosomes
# def cumulative_fitness  (chromosomes, v):
#     arr_cum = [0] * len(chromosomes)
#     sum = 0
#     for i in range(len(chromosomes)):
#         sum += get_value(chromosomes[i], v)
#         arr_cum[i] = sum
#     return arr_cum  

# cumulative_sum = cumulative_fitness(chromosomes, v)
# def get_rand(cumulative_sum):
#     random_num = randint(0,cumulative_sum[-1])
#     return random_num

# # selection 
# def roulette_selection(n , cumulative_sum):
#     for i in range(n):
#         num = get_rand(cumulative_sum)
#         for i in range(len(cumulative_sum)):
#             if num <= cumulative_sum[i] :
#                 print(f"We Have Selected Chromosome:{i+1}" , f"The random Number was:{num}")
#                 break