

def get_data():
    wires_mapping = {}
    with open("../inputs/7.in", "r") as fp:
        for line in fp:
            wire_ip,wire_op = line.strip('\n').split(" -> ")
            wires_mapping[wire_op] = wire_ip.split(' ')
    return wires_mapping

def twos_complement(num):
    return (~num) & 0xFFFF

def calculate_signal(wires_mapping,current_wire,override_wire,override_value):
    if current_wire == override_wire:
        return override_value
    if current_wire not in wires_mapping:
        return int(current_wire)
    if isinstance(wires_mapping[current_wire], int):
        return wires_mapping[current_wire]
    
    res_singal = 0
    op = wires_mapping[current_wire]
    if len(op) == 1:
        res_singal = calculate_signal(wires_mapping,op[0],override_wire,override_value)
    elif op[0] == "NOT":
        res_singal = twos_complement(calculate_signal(wires_mapping,op[1],override_wire,override_value))
    elif op[1] == 'AND':
        res_singal = calculate_signal(wires_mapping,op[0],override_wire,override_value) & calculate_signal(wires_mapping,op[2],override_wire,override_value)
    elif op[1] == 'LSHIFT':
        res_singal = calculate_signal(wires_mapping,op[0],override_wire,override_value) << calculate_signal(wires_mapping,op[2],override_wire,override_value)
    elif op[1] == 'OR':
        res_singal = calculate_signal(wires_mapping,op[0],override_wire,override_value) | calculate_signal(wires_mapping,op[2],override_wire,override_value)
    elif op[1] == 'RSHIFT':
        res_singal = calculate_signal(wires_mapping,op[0],override_wire,override_value) >> calculate_signal(wires_mapping,op[2],override_wire,override_value)
    wires_mapping[current_wire] = res_singal
    return res_singal

def main():
    wires_mapping = get_data()
    
    initial_wire_name = 'a'
    updated_wire_name = 'b'
    a_wire_signal = calculate_signal(dict(wires_mapping),initial_wire_name,None,None)
    new_wire_signal = calculate_signal(dict(wires_mapping),initial_wire_name,updated_wire_name,a_wire_signal)
    print(a_wire_signal)
    print(new_wire_signal)
    
    
main()