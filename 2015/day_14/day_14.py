import sys
import re

REINDEER_REG = r"(.+) can .+ (\d+) .+ (\d+) seconds.+ (\d+)"


class Reindeer:
    def __init__(self, name, fly_speed, fly_time, rest_duration):
        self.name = name
        self.fly_speed = fly_speed
        self.fly_time = fly_time
        self.rest_duration = rest_duration
        self.distance_covered = 0
        self.points = 0
        self.wait_time = 0
        self.t = 1

    def fly(self):
        if self.wait_time == 0 and self.t == self.fly_time:
            self.distance_covered += self.fly_speed
            self.t = 1
            self.wait_time = self.rest_duration
        elif self.wait_time > 0:
            self.wait_time -= 1
        else:
            self.distance_covered += self.fly_speed
            self.t += 1

    def inc_point(self):
        self.points += 1

    def __str__(self):
        return f"Reindeer({self.name},{self.fly_speed},{self.fly_time},{self.rest_duration},{self.distance_covered},{self.points},{self.wait_time})"


def solve_day_14(data, total_seconds):
    reindeers = []
    for reindeer in data:
        name, fly_speed, fly_time, rest_duration = re.findall(REINDEER_REG, reindeer)[0]
        fly_speed, fly_time, rest_duration = map(
            int, [fly_speed, fly_time, rest_duration]
        )
        reindeers.append(Reindeer(name, fly_speed, fly_time, rest_duration))

    for _ in range(total_seconds):
        for r in reindeers:
            r.fly()

        max_distance = max(reindeer.distance_covered for reindeer in reindeers)
        for r in reindeers:
            if r.distance_covered == max_distance:
                r.inc_point()

    max_distance = max(reindeer.distance_covered for reindeer in reindeers)
    max_points = max(reindeer.points for reindeer in reindeers)
    return [max_distance, max_points]


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        lines = [line.strip("\n") for line in fp.readlines()]
        return lines


def main():
    filename = sys.argv[1]
    data = read_data(filename)
    total_seconds = 2503

    part_1_ans, part_2_ans = solve_day_14(data, total_seconds)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
