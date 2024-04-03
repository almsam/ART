import re

class parameterValidator:
    
    def validateEmail(email: str) -> bool:
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(email_regex, email) != None:
            return True
        else:
            return False

    def validateNames(name: str) -> str:    #returns whether name is valid length, returns None if valid
        if len(name) < 8:
            return "Name too short! "
        elif len(name) > 64:
            return "Name too long! "
        return None
    
    def validatePassword(password: str) -> bool:
        return (len(password) > 64)