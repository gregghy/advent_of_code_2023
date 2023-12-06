use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename1 = &args[1];
    //let filename2 = &args[2];

    let content1 = fs::read_to_string(filename1).expect("Unable to read");
    //let content2 = fs::read_to_string(filename2).expect("Unable to read");
    println!("First problem: {}", calibration1(content1));
}

fn calibration1(input: String) -> i32 {
    let mut num = 0;
    for line in input.lines() {
        let mut pair = String::new();
        for c in line.chars() {
            if c.is_numeric(){
                pair.push(c);
                break;
            }
        }
        for c in line.chars().rev() {
            if c.is_numeric(){
                pair.push(c);
                break;
            }
        }
        num = num + pair.parse::<i32>().unwrap();
    }
    return num 
}

//fn calibration2(input: String) -> i32 {
//    return 3
//}


//cargo run -- file1 file2
