use std::fs::File;
use std::io::{BufRead, BufReader};
use regex::Regex;

static FILENAME: &str = "input.txt";

struct Policy {
    num1: usize,
    num2: usize,
    letter: char,
    password: String,
}

fn get_input() -> Vec<Policy> {
    let mut policies: Vec<Policy> = Vec::new();

    let re = Regex::new(r"(\d+)-(\d+) ([a-z]): (\w+)").unwrap();

    // Open the file in read-only mode (ignoring errors).
    let file = File::open(FILENAME).unwrap();
    let reader = BufReader::new(file);

    // Read the file line by line using the lines() iterator from std::io::BufRead.
    for line in reader.lines() {
        let line = line.unwrap();

        policies.push(
            re.captures(&line).and_then(|cap| {
                let groups = (cap.get(1), cap.get(2), cap.get(3), cap.get(4));
                match groups {
                    (Some(num1), Some(num2), Some(letter), Some(password)) => Some(Policy {
                        num1: num1.as_str().parse::<usize>().unwrap(),
                        num2: num2.as_str().parse::<usize>().unwrap(),
                        letter: letter.as_str().chars().next().unwrap(),
                        password: password.as_str().to_string(),
                    }),
                    _ => None,
                }
            }).unwrap()
        );
    }

    return policies;
}

fn part_1() {
    let policies = get_input();
    let mut count = 0;

    for policy in policies {
        let mut count_letter = 0;

        for ch in policy.password.chars() {
            if ch == policy.letter {
                count_letter += 1;
            }
        }

        if policy.num1 <= count_letter && count_letter <= policy.num2 {
            count += 1;
        }
    }

    println!("There are {} valid passwords", count);
}

fn part_2() {
    let policies = get_input();
    let mut count = 0;

    for policy in policies {
        let l1 = policy.password.as_bytes()[policy.num1-1] as char;
        let l2 = policy.password.as_bytes()[policy.num2-1] as char;

        if (l1 == policy.letter && l2 != policy.letter) || (l1 != policy.letter && l2 == policy.letter) {
            count += 1;
        }
    }

    println!("There are {} valid passwords", count);
}

fn main() {
    part_1();
    part_2();
}
