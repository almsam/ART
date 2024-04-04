import re
from dateutil.parser import parse
from datetime import datetime

class parameterValidator:
    
    def validateEmail(self, email: str) -> bool:    #confirms email format
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
    
    def validateDate(self, date: str) -> bool:  #confirms it is a valid date format (does not check if it is in future)
        try:
            parse(date)
            return True
        except ValueError:
            return False

    def validateAge(self, dob: str) -> bool:    #validate user is 18 or older, also prevents dates from being in future
        if self.validateDate(dob) is False:
            return False
        currentDate = datetime.today().strftime('%Y-%m-%d')
        minYear = int(currentDate[:4]) - 18
        minDate = str(minYear) + currentDate[4:]
        return dob <= minDate