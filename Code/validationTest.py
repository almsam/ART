from validation import parameterValidator

class validationTesting:

    Validator = parameterValidator()

    def testDateValidation(self) -> bool:
        test = "2001-01-01"
        result = "True"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestDateValidation(test)))
        
        test = "abc"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestDateValidation(test)))
        
        test = "2001-01-000"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestDateValidation(test)))

        test = "2001-00-00"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestDateValidation(test)))
        
        test = "9999-01-01"
        result = "True"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestDateValidation(test)))
        
        test = "2001-01-99"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestDateValidation(test)))
        
        test = "2001-99-01"
        result = "False"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestDateValidation(test)))

        test = "1000-09-30"
        result = "True"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestDateValidation(test)))

        test = "2018-11-20"
        result = "True"
        print("Value: " + test + "  Should return: " + result + "... Returned: " + str(self.auxTestDateValidation(test)))

    def auxTestDateValidation(self, date) -> bool:
        return self.Validator.validateDate(date)
    
def runValidationTesting():
    tester = validationTesting()

    tester.testDateValidation()

runValidationTesting()