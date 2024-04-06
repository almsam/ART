from validation import parameterValidator
from datetime import datetime

class validationTesting:

    Validator = parameterValidator()

    def testDateValidation(self):
        print("\nvalidateDate tests...")

        test = "2001-01-01"
        result = "True"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateDate(test)))
        
        test = "abc"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateDate(test)))
        
        test = "2001-01-000"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateDate(test)))

        test = "2001-00-00"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateDate(test)))
        
        test = "9999-01-01"
        result = "True"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateDate(test)))
        
        test = "2001-01-99"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateDate(test)))
        
        test = "2001-99-01"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateDate(test)))

        test = "1000-09-30"
        result = "True"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateDate(test)))

        test = "2018-11-20"
        result = "True"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateDate(test)))
        
        test = 2
        result = "False"
        print("Value: " + str(test) + "  Should return: " + result + "... Returned: " + str(self.Validator.validateDate(test)))

    def testValidateInt(self):
        print("\nvalidateInt test...")

        test = "2018-11-20"
        result = "False"
        print("Value: " + str(test) + "  Should return: " + result + "... Returned: " + str(self.Validator.validateInt(test)))
        
        test = 2
        result = "True"
        print("Value: " + str(test) + "  Should return: " + result + "... Returned: " + str(self.Validator.validateInt(test)))
         
        test = 2.14
        result = "False"
        print("Value: " + str(test) + "  Should return: " + result + "... Returned: " + str(self.Validator.validateInt(test)))

    def testValidateNames(self):
        print("\nvalidateNames test...")

        test = "2018-11-20"
        result = "True"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestValidateNames(test)))
        
        test = "Confirmed"
        result = "True"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestValidateNames(test)))
        
        test = "Actually a name is really a name"
        result = "True"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestValidateNames(test)))
        
        test = "no"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestValidateNames(test)))
        
        test = 2
        result = "False"
        print("Value: " + str(test) + "  Should return: " + result + "... Returned: " + str(self.auxTestValidateNames(test)))
        
        test = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestValidateNames(test)))
        
    def auxTestValidateNames(self, name) -> bool:
        if (self.Validator.validateNames(name) is None):
            return True
        return False

    def testValidateAge(self):
        print("\nvalidateAge test...")

        test = "2002-12-12"
        result = "True"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateAge(test)))
        
        test = "1012-12-12"
        result = "True"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateAge(test)))
        
        test = "2030-12-12"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateAge(test)))
        
        test = "2020-12-12"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateAge(test)))
        
        test = "9999-12-12"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateAge(test)))
        
        test = "20022-12-12"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateAge(test)))
        
        test = "2002-14-12"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateAge(test)))
        
        test = "2002-12-99"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateAge(test)))
        
        test = "2002-012-12"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateAge(test)))
        
        test = "2002-12-102"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateAge(test)))
        
        test = 2
        result = "False"
        print("Value: " + str(test) + "  Should return: " + result + "... Returned: " + str(self.Validator.validateAge(test)))
        
        test = "abd2"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.Validator.validateAge(test)))
        
    def testValidateString(self):
        print("\nvalidateString test...")

        test = "AAAAAA"
        result = "True"
        maxLength = 32
        print("Value: " + test + " With max length: " + str(maxLength) + "  Should return: " + result + "... Returned: " + str(self.Validator.validateString(test, maxLength)))
        
        test = "Maranda Allison"
        result = "True"
        maxLength = 32
        print("Value: " + test + " With max length: " + str(maxLength) + "  Should return: " + result + "... Returned: " + str(self.Validator.validateString(test, maxLength)))
        
        test = "Ashar"
        result = "False"
        maxLength = 4
        print("Value: " + test + " With max length: " + str(maxLength) + "  Should return: " + result + "... Returned: " + str(self.Validator.validateString(test, maxLength)))
        
        test = 2
        result = "False"
        maxLength = 32
        print("Value: " + str(test) + " With max length: " + str(maxLength) + "  Should return: " + result + "... Returned: " + str(self.Validator.validateString(test, maxLength)))
        
        test = "Ashar Allison Trinity"
        result = "False"
        maxLength = 16
        print("Value: " + test + " With max length: " + str(maxLength) + "  Should return: " + result + "... Returned: " + str(self.Validator.validateString(test, maxLength)))
        

def runValidationTesting():
    tester = validationTesting()

    tester.testDateValidation()
    tester.testValidateInt()
    tester.testValidateNames()
    tester.testValidateAge()
    tester.testValidateString()

runValidationTesting()