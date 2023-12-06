// Part-1: 178159714
// Part-2: 100165128

package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"regexp"
	"strconv"
	"sync"
	"sync/atomic"
)

var map_data [][][]int64
var part_2_ans atomic.Int64

func getNums(line string) []int64 {
	r := regexp.MustCompile(`\d+`)
	matches := r.FindAllString(line, -1)
	nums := make([]int64, 0, len(matches))
	for _, num := range matches {
		conv_num, err := strconv.ParseInt(num, 10, 64)
		if err != nil {
			log.Fatal(err)
		}
		nums = append(nums, conv_num)
	}
	return nums
}

func readData(filename string) []int64 {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	seeds := getNums(scanner.Text())
	scanner.Scan()
	map_data = make([][][]int64, 0)
	cur_part_data := make([][]int64, 0)

	for scanner.Scan() {
		line := scanner.Text()
		if len(line) == 0 && len(cur_part_data) > 0 {
			map_data = append(map_data, cur_part_data)
			cur_part_data = make([][]int64, 0)
		} else {
			nums := getNums(line)
			if len(nums) > 0 {
				cur_part_data = append(cur_part_data, nums)
			}

		}
	}
	if len(cur_part_data) > 0 {
		map_data = append(map_data, cur_part_data)
	}
	return seeds
}

func abs(x int64) int64 {
	if x < 0 {
		return -x
	}
	return x
}

func find_location(seed int64) int64 {
	check_value := seed
	for _, row := range map_data {
		// fmt.Print64ln(row)
		for _, part := range row {
			x1 := part[1]
			y1 := part[1] + part[2]
			x2 := part[0]

			if check_value >= x1 && check_value <= y1 {
				new_value := x2 + abs(x1-check_value)
				check_value = new_value
				break
			}
		}
	}
	return check_value
}

func part_1(seeds []int64) int64 {
	min_location := int64(math.MaxInt64)
	for _, seed := range seeds {
		min_location = min(min_location, find_location(seed))
	}
	return min_location
}

func part_2(seeds []int64) {
	part_2_ans.Store(math.MaxInt64)

	for i := 0; i < len(seeds); i += 2 {
		wg := sync.WaitGroup{}
		wg.Add(int(seeds[i+1]))
		for cur_seed := seeds[i]; cur_seed < seeds[i]+seeds[i+1]; cur_seed++ {
			go func(wg *sync.WaitGroup, seed int64) {
				defer wg.Done()
				part_2_ans.Store(min(part_2_ans.Load(), find_location(seed)))
			}(&wg, cur_seed)
		}
		wg.Wait()
	}
}

func main() {

	filename := os.Args[1]
	seeds := readData(filename)
	part_1_ans := part_1(seeds)
	fmt.Println(part_1_ans)
	part_2(seeds)
	fmt.Println(part_2_ans.Load())
}
