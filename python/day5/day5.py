def read_map(lines):
    mapping = []
    if len(lines) == 0:
        return mapping
    lines.pop(0)

    while len(lines) > 0 and len(lines[0]) > 0:
        line = lines.pop(0)
        [dest, init, length] = [int(val) for val in line.split()]
        mapping.append((range(init, init + length), dest))

    if len(lines) > 0:
        lines.pop(0)
    return mapping


def find(val, mapping):
    for range, end in mapping:
        if val in range:
            return val - range.start + end
    else:
        return val


def part_1():
    lines = []
    f = open("input.txt", "r")
    for line in f:
        line = line.strip()
        lines.append(line)


    seeds_line = lines.pop(0).split("seeds: ")[1]
    seeds = []
    for val in seeds_line.split():
        seeds.append(int(val))

    lines.pop(0)

    mappings = []
    for _ in range(7):
        mappings.append(read_map(lines))

    smallest = seeds[0]
    for curr in seeds:
        for map in mappings:
            curr = find(curr, map)
        smallest = min(smallest, curr)

    print(smallest)

def part_2():
    lines = []
    f = open("input.txt", "r")
    for line in f:
        line = line.strip()
        lines.append(line)

    seeds_line = lines.pop(0).split("seeds: ")[1]
    seeds = []
    part_two_itx = 0
    part_two_seeds_line = seeds_line.split()
    while part_two_itx < len(part_two_seeds_line):
        start = int(part_two_seeds_line[part_two_itx])
        length = int(part_two_seeds_line[part_two_itx + 1])
        seeds.append(range(start, start + length))
        part_two_itx += 2

    lines.pop(0)

    mappings = []
    for _ in range(7):
        mappings.append(read_map(lines))

    smallest = seeds[0][0]
    for seed_range in seeds:
        ranges = [seed_range]
        for mapping in mappings:
            new_ranges = []
            while ranges:
                current_range = ranges.pop()
                for map_range, new_start in mapping:
                    new_range_start = max(map_range.start, current_range.start)
                    new_range_stop = min(map_range.stop, current_range.stop)

                    if range(new_range_start, new_range_stop):
                        offset = new_start - map_range.start
                        new_range = range(new_range_start + offset, new_range_stop + offset)
                        new_ranges.append(new_range)

                        if new_range_start > current_range.start:
                            ranges.append(range(current_range.start, new_range_start))

                        if new_range_stop < current_range.stop:
                            ranges.append(range(new_range_stop, current_range.stop))

                        break
                else:
                    new_ranges.append(current_range)
            ranges = new_ranges

        smallest = min(smallest, min([r.start for r in ranges]))

    print(smallest)


part_1()
part_2()

