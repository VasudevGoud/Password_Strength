import re
import random
import string

class Strength:
    def __init__(self, password, filename):
        self.password = password
        self.filename = filename
        self.result = []
        self.score = 0
        self.common_passwords = self.load_common_passwords()

    def load_common_passwords(self):
       
        try:
            with open(self.filename, 'r') as file_object:
                return file_object.read().splitlines()
        except FileNotFoundError:
            print("Common passwords file not found. Proceeding without it.")
            return []

    def evaluate(self):
       
        if self.password in self.common_passwords:
            self.result.append("Don't use common passwords. Try something unique!")
        else:
            self.score += 2

        
        if len(self.password) < 16:
            self.result.append("Password must be at least 16 characters long.")
        else:
            self.score += 1

        
        if not re.search(r'[A-Z]', self.password):
            self.result.append("Password should include at least one uppercase letter.")
        else:
            self.score += 1

        
        if not re.search(r'[a-z]', self.password):
            self.result.append("Password should include at least one lowercase letter.")
        else:
            self.score += 1

       
        if not re.search(r'''[!"#\u20ac%&/()=+?:;,.'\-@$*]''', self.password):
            self.result.append("Password should include at least one special character.")
        else:
            self.score += 1

       
        if not re.search(r'[0-9]', self.password):
            self.result.append("Password should include at least one number.")
        else:
            self.score += 1

        
        if self.score >= 5:
            strength = "Strong :)"
        elif 4 <= self.score < 5:
            strength = "Moderate :|"
        else:
            strength = "Weak :("

        return strength, self.result

    def strengthen_password(self):
        
        while self.score < 5 or len(self.password) < 16:
           
            if len(self.password) < 16:
                self.password += random.choice(string.ascii_letters + string.digits + "!@#$%^&*")
            if not re.search(r'[A-Z]', self.password):
                self.password += random.choice(string.ascii_uppercase)
            if not re.search(r'[a-z]', self.password):
                self.password += random.choice(string.ascii_lowercase)
            if not re.search(r'''[!"#\u20ac%&/()=+?:;,.'\-@$*]''', self.password):
                self.password += random.choice("!@#$%^&*")
            if not re.search(r'[0-9]', self.password):
                self.password += random.choice(string.digits)

            
            self.result = []
            self.score = 0
            self.evaluate()

        return self.password


filename = "common_passwords.txt"  

while True:
    password = input("Enter your password (or type 'exit' to quit): ")
    if password.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    strength_checker = Strength(password, filename)
    strength, suggestions = strength_checker.evaluate()

    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions for improvement:")
        for suggestion in suggestions:
            print(f"  - {suggestion}")

    if strength != "Strong :)":
        print("\nStrengthening your password...")
        strong_password = strength_checker.strengthen_password()
        print(f"Your new strong password: {strong_password}")
        


