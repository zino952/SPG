# Password Generator

## Description
This is a Python-based password generator that creates strong, randomized passwords for different social media and app accounts. Each password is saved in `password.txt` along with the corresponding social app name.

## Features
- Generates strong 32-character passwords with a mix of letters, numbers, and symbols.
- Allows the user to generate multiple passwords.
- Saves generated passwords in `password.txt` with numbering.
- Supports any social app or platform.
- Simple and easy-to-use command-line interface.

## Installation
1. Make sure you have Python installed on your system.
2. Download or clone this repository.
3. Run the script using:
   ```sh
   python spg.py
   ```

## Usage
1. Enter your name.
2. Input the social app where the password will be used.
3. The script will generate and display a strong password.
4. The password will be saved in `password.txt` in the following format:
   ```
   1. Discord
      rT8^gP!9sV&2aL@3W$eXzQY*
   ```
5. The program will ask if you want to generate another password for a different social app or restart with a new name.
6. Repeat as needed.

## Example Output
```
Enter your name: John
Which social app are you going to use this password for? Facebook
Generated Password: Ab@9qP%yW3#sV!8zQXe*2L4T
Saved to password.txt
Generate another password for a different social app? (y/n): y
Which social app are you going to use this password for? Twitter
Generated Password: 7*LpQ@xYs#T3zW!8V2Ae9qP%
Saved to password.txt
```

## Notes
- Passwords are randomly generated each time.
- Make sure to keep `password.txt` safe and secure.

## License
This project is free to use and modify.

