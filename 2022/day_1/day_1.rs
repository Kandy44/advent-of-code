use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn read_data() -> Vec<i32> {
    let mut calories: Vec<i32> = Vec::new();
    if let Ok(lines) = read_lines("../inputs/1.in") {
        let mut cur_calories = 0;
        for line in lines {
            if let Ok(ip) = line {
                let current_line = ip.replace('\n', "");
                if current_line.len() > 0 {
                    cur_calories = cur_calories + ip.parse::<i32>().unwrap();
                } else {
                    calories.push(cur_calories);
                    cur_calories = 0;
                }
            }
        }

        if cur_calories != 0 {
            calories.push(cur_calories);
        }

        calories.sort_by(|c1, c2| -> std::cmp::Ordering { c2.cmp(c1) });
        return calories;
    } else {
        return calories;
    }
}

fn day_1(calories: &Vec<i32>, n: usize) -> i32 {
    let mut res = 0;
    let mut i: usize = 0;
    while i < n {
        res += calories[i];
        i += 1;
    }
    return res;
}

fn main() {
    let calories = read_data();
    println!("{}", day_1(&calories, 1));
    println!("{}", day_1(&calories, 3));
}
