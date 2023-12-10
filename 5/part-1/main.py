def main():
    with open('input.txt', 'r') as input_file:
        sections = input_file.read().split('\n\n')
        seeds = [int(num) for num in sections[0].split(':')[-1].strip().split(' ')]
        section_map = {
            section.split(':')[0].split(' ')[0].split('-to-')[0]: {
                'dest_category': section.split(':')[0].split(' ')[0].split('-to-')[-1],
                'ranges': [{
                    'dest_start': int(line.split(' ')[0]),
                    'source_start': int(line.split(' ')[1]),
                    'range_length': int(line.split(' ')[2]),
                } for line in section.split(':')[-1].strip().split('\n')],
            }
            for section in sections[1:]
        }
        return min([recursive_thing('seed', seed, section_map) for seed in seeds])


def recursive_thing(key, source_value, section_map):
    dest_value = None
    dest_category = section_map[key]['dest_category']
    for map_range in section_map[key]['ranges']:
        start = map_range['source_start']
        range_length = map_range['range_length']
        end = start + range_length
        dest_start = map_range['dest_start']
        if start <= source_value < end:
            dest_value = (source_value - start) + dest_start
        else:
            pass
    dest_value = source_value if not dest_value else dest_value
    if dest_category == 'location':
        return dest_value
    else:
        return recursive_thing(dest_category, dest_value, section_map)


if __name__ == '__main__':
    print(main())