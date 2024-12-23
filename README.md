# Password_Strength

# Password Strength Checker and Enhancer

This project is a Python-based application that evaluates the strength of a password and provides suggestions to improve it. If a password does not meet the strength criteria, the program can automatically enhance it by adding random characters to meet the required strength.

## Features

- **Password Strength Evaluation:**
  - Checks for common passwords.
  - Validates password length (minimum 16 characters).
  - Ensures inclusion of uppercase letters, lowercase letters, special characters, and numbers.

- **Automatic Password Enhancement:**
  - Adds random characters (letters, numbers, and symbols) to strengthen weak passwords.
  - Ensures the enhanced password meets all strength criteria and is at least 16 characters long.

## How to Use

1. **Install Python:**
   Ensure Python 3.x is installed on your system. Download it from [python.org](https://www.python.org/).

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/VasudevGoud/Password_Strength.git
   cd Password_Strength
   ```

3. **Add Common Passwords File:**
   Ensure the file `common_passwords.txt` is present in the project directory. This file should contain a list of commonly used passwords, one per line.

4. **Run the Program:**
   Execute the script:
   ```bash
   python Strength.py
   ```

5. **Input a Password:**
   - Enter your password to check its strength.
   - If the password is weak or moderate, the program will provide suggestions and optionally enhance the password automatically.

6. **Exit the Program:**
   Type `exit` when prompted to quit the program.

## Example

### Input
```plaintext
Enter your password (or type 'exit' to quit): vasudev
```

### Output
```plaintext
Password Strength: Weak :(
Suggestions for improvement:
  - Password must be at least 16 characters long.
  - Password should include at least one uppercase letter.
  - Password should include at least one special character.
  - Password should include at least one number.

Strengthening your password...
Your new strong password: vasudevA!2kp93xyF
```

## Project Structure

- **`Strength.py`**: The main script containing the password evaluation and enhancement logic.
- **`common_passwords.txt`**: A file with a list of commonly used passwords.

## Dependencies

This project uses Python's built-in modules:
- `re`: For regex operations.
- `random`: For generating random characters.
- `string`: For handling character sets.

No external dependencies are required.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contribution

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## Author

[Vasudev Goud](https://github.com/VasudevGoud)
