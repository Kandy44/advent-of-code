from itertools import permutations
distances = {}
cities = set()
total_distances = []

def generate_adjacency_list():
    global distances
    global cities
    with open('../inputs/9.in','r') as fp:
        for line in fp:
            from_city,to_city,distance = line.replace(" to "," ").replace(" = "," ").split(" ")
            distance = int(distance)
            distances[(to_city,from_city)],distances[(from_city,to_city)] = distance,distance
            cities.update([from_city,to_city])

def generate_path_distance(cities):
    global total_distances,distances
    city_list = list(cities)
    cur_distance = 0
    i,j,n=0,1,len(city_list)
    while i < n - 1:
        cur_distance += distances[(city_list[i],city_list[j])]
        i += 1
        j += 1
    total_distances.append(cur_distance)
    
    

def main():
    generate_adjacency_list()
    for city_perm in permutations(cities):
        generate_path_distance(city_perm)
    print(min(total_distances))
    print(max(total_distances))
main()
