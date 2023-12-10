import bisect


def main():
    with open('input.txt', 'r') as input_file:
        sections = input_file.read().split('\n\n')
        raw_seeds = [int(num) for num in sections[0].split(':')[-1].strip().split(' ')]
        seed_range_starts = raw_seeds[::2]
        seed_range_lengths = raw_seeds[1::2]
        seed_ranges = tuple(sorted(zip(seed_range_starts, seed_range_lengths), key=lambda x: x[0]))
        section_map = {
            section.split(':')[0].split(' ')[0].split('-to-')[-1]: {
                'source_category': section.split(':')[0].split(' ')[0].split('-to-')[0],
                'ranges': sorted([{
                    'dest_start': int(line.split(' ')[0]),
                    'source_start': int(line.split(' ')[1]),
                    'range_length': int(line.split(' ')[2]),
                } for line in section.split(':')[-1].strip().split('\n')], key=lambda x: x['dest_start']),
            }
            for section in sections[1:]
        }
        location_num = -1
        seed_in_range = False
        while not seed_in_range:
            location_num += 1
            seed_value = reverse_search('location', location_num, section_map)
            seed_in_range = seed_is_in_range(seed_value, seed_ranges)
        return location_num


def seed_is_in_range(seed_value: int, seed_ranges: tuple[tuple[int, int]]) -> bool:
    index = bisect.bisect_left(seed_ranges, seed_value, key=lambda x: x[0]) - 1
    lower_bound = seed_ranges[index][0]
    upper_bound = lower_bound + seed_ranges[index][1]
    if lower_bound <= seed_value < upper_bound:
        return True
    return False


def reverse_search(key, dest_value, section_map):
    source_category = section_map[key]['source_category']
    ranges = section_map[key]['ranges']
    index = bisect.bisect_right(ranges, dest_value, key=lambda x: x['dest_start']) - 1
    range = ranges[index]
    lower_bound = range['dest_start']
    upper_bound = lower_bound + range['range_length']
    source_start = range['source_start']
    if lower_bound <= dest_value < upper_bound:
        source_value = (dest_value - lower_bound) + source_start
    else:
        source_value = dest_value
    if source_category == 'seed':
        return source_value
    else:
        return reverse_search(source_category, source_value, section_map)


if __name__ == '__main__':
    print(main())
