use std::fs::File;
use std::io::{BufRead, BufReader};

const TREE: char = '#';

fn get_input() -> Vec<String> {
    let mut area: Vec<String> = Vec::new();

    let filename = "input.txt";

    // Open the file in read-only mode (ignoring errors).
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    // Read the file line by line using the lines() iterator from std::io::BufRead.
    for line in reader.lines() {
        let line = line.unwrap();

        area.push(line);
    }

    return area;
}

fn get_tree_encountered(area: &Vec<String>, right: usize, down: usize) -> usize {
    let mut index = 0;
    let mut down_index = down-1;
    let mut count = 0;

    for row in area {
        down_index = (down_index + 1) % down;

        if down_index != 0 {
            continue;
        }

        let encountered = row.as_bytes()[index] as char;

        if encountered == TREE {
            count += 1
        }

        index = (index + right) % row.len();
    }

    return count;
}

#[allow(dead_code)]
fn part_1() {
    let area = get_input();

    let answer = get_tree_encountered(&area, 3, 1);

    println!("Encountered {} trees", answer);
}

#[allow(dead_code)]
fn part_2() {
    let area = get_input();

    let case1 = get_tree_encountered(&area, 1, 1);
    let case2 = get_tree_encountered(&area, 3, 1);
    let case3 = get_tree_encountered(&area, 5, 1);
    let case4 = get_tree_encountered(&area, 7, 1);
    let case5 = get_tree_encountered(&area, 1, 2);

    println!("The answer is {}", case1 * case2 * case3 * case4 * case5);
}

fn main() {
    // part_1();
    // part_2();
}
