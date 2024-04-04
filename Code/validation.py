import re
from datetime import datetime

class parameterValidator:
    
    def validateEmail(self, email: str) -> bool:
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(email_regex, email) != None:
            return True
        else:
            return False

    def validateNames(self, name: str) -> str:    #returns whether name is valid length, returns None if valid
        if len(name) < 8:
            return "Username too short: "
        elif len(name) > 64:
            return "Username too long: "
        return None
    
    def validatePassword(self, password: str) -> bool:
        return (len(password) > 64)
    
    def validateAge(self, dob) -> str:
        currentDate = datetime.today().strftime('%Y-%m-%d')
        minYear = int(currentDate[:4]) - 18
        minDate = str(minYear) + currentDate[4:]
        return dob <= minDate