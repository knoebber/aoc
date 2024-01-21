import time

start_time = time.time()

seeds = {}
maps = []


with open('input.txt', 'r') as f:
    seeds = {int(n) for n in f.readline()[7:].split(' ')}

    for line in f:
        line = line.strip()
        first_char = line[0] if line else None
        should_read_numbers = first_char and first_char.isnumeric()

        if not should_read_numbers and first_char:
            maps.append([])

        if should_read_numbers:
            maps[len(maps) -1].append(tuple(int(n) for n in line.split(' ')))

valid_resources_set = seeds
for resource_map in maps:
    next_valid_resource_set = set()
    for map_line in resource_map:
        dest_range_start, source_range_start, n = map_line
        diff = dest_range_start - source_range_start
        for item in tuple(valid_resources_set):
           if item >= source_range_start and item <= source_range_start+n:
               next_valid_resource_set.add(item+diff)
               valid_resources_set.remove(item)

    valid_resources_set = valid_resources_set | next_valid_resource_set

print('answer:', sorted(valid_resources_set)[0], 'in', time.time() - start_time, 'seconds')
