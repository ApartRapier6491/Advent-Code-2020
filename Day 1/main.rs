use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;

static FILENAME: &str = "input.txt";

fn get_input() -> HashSet<i32> {
    let mut input = HashSet::new();

    // Open the file in read-only mode (ignoring errors).
    let file = File::open(FILENAME).unwrap();
    let reader = BufReader::new(file);

    // Read the file line by line using the lines() iterator from std::io::BufRead.
    for line in reader.lines() {
        let line = line.unwrap();

        input.insert(line.parse::<i32>().unwrap());
    }

    return input;
}

fn find_pair_sum(data: &HashSet<i32>, goal: i32) -> Option<(i32, i32)> {
    for num in data {
        let remaining = goal - *num;
        if data.contains(&remaining) {
            return Some((*num, remaining));
        }
    }

    None
}

fn find_triple_sum(data: &HashSet<i32>, goal: i32) -> Option<(i32, i32, i32)> {
    for num in data {
        let remaining = goal - *num;
        if let Some((a, b)) = find_pair_sum(data, remaining) {
            if a != b && a != *num && b != *num {
                return Some((a, b, *num));
            }
        }
    }

    None
}

fn part_1() {
    let input: HashSet<i32> = get_input();

    match find_pair_sum(&input, 2020) {
        Some((a, b)) => {
            println!("{} * {} == {}", a, b, a * b);
        }
        None => println!("Pair not found!"),
    }
}

fn part_2() {
    let input: HashSet<i32> = get_input();

    match find_triple_sum(&input, 2020) {
        Some((a, b, c)) => {
            println!("{} * {} * {} == {}", a, b, c, a * b * c);
        }
        None => println!("Triple not found!"),
    }
}

fn main() {
    part_1();
    part_2();
}
