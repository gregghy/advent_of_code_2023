use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename1 = args[1].clone();
    let filename2 = args[2].clone();




}

fn calibration1(filename: &String) {
    let content = fs::read_to_string(config.file_path)?;
    
}

fn calibration2(filename: &String) {

}


//cargo run -- file1 file2
