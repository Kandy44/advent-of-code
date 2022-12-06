def read_data():
    with open("../inputs/6.in", "r") as fp:
        return fp.readline().strip('\n')

def get_marker_index(signal,seq_len=4):
    for j in range(0,len(signal)-seq_len-1):
        if len(set(signal[j:j+seq_len])) == seq_len:
            return j+seq_len

def main():
    signal = read_data()
    print(get_marker_index(signal,seq_len=4))
    print(get_marker_index(signal,seq_len=14))

main()