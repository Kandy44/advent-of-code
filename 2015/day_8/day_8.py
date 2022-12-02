def get_data():
    with open("../inputs/8.in", "r") as fp:
        return [line.strip('\n') for line in fp.readlines()]

def get_memory_count(str_literals,expand=False):
    orig_char_count = sum(map(len,str_literals))
    memory_char_count = 0
    
    for line in str_literals:   
        if expand:
            encoded_str = '\"' + line.replace("\\","\\\\").replace("\"","\\\"").replace('\'','\\\'') + '\"'
            memory_char_count += len(encoded_str)
        else:
            memory_char_count += len(eval(line))
    return abs(orig_char_count - memory_char_count)

def main():
    str_literals = get_data()
    print(get_memory_count(str_literals,expand=False))
    print(get_memory_count(str_literals,expand=True))
main()