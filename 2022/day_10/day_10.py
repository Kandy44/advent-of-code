from PIL import Image

pixel_dim = (40, 6)


def read_data():
    with open("../inputs/10.in", "r") as fp:
        return [line.strip('\n').split(' ') for line in fp]


def get_signal_strength_and_crt_image(data, idxs):
    cur_reg_val = 1
    signal_strength_sum = 0
    cur_idx = 1
    pixel_idx = 0
    pixels = [0 for _ in range(pixel_dim[0]*pixel_dim[1])]

    for op in data:
        if op[0] == "noop":
            if cur_idx in idxs:
                signal_strength_sum += (cur_idx * cur_reg_val)

            if cur_reg_val-1 <= (pixel_idx % pixel_dim[0]) <= cur_reg_val+1:
                pixels[pixel_idx] = 1

            pixel_idx += 1
            cur_idx += 1

        elif op[0] == "addx":
            cur_op_val = int(op[1])

            if cur_reg_val-1 <= (pixel_idx % pixel_dim[0]) <= cur_reg_val+1:
                pixels[pixel_idx] = 1
            pixel_idx += 1

            if cur_idx in idxs:
                signal_strength_sum += (cur_idx * cur_reg_val)
            cur_idx += 1

            if cur_reg_val-1 <= (pixel_idx % pixel_dim[0]) <= cur_reg_val+1:
                pixels[pixel_idx] = 1
            pixel_idx += 1

            if cur_idx in idxs:
                signal_strength_sum += (cur_idx * cur_reg_val)

            cur_reg_val += cur_op_val
            cur_idx += 1

    img = Image.new('1', pixel_dim, "black")
    img.putdata(pixels)
    img.save('day_10_output.jpg')

    return signal_strength_sum


def main():
    data = read_data()
    idxs = [20, 60, 100, 140, 180, 220]
    print(get_signal_strength_and_crt_image(data, idxs))


main()
