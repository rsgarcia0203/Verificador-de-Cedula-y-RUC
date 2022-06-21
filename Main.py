from copyreg import constructor
import json
import numpy as np

class UserIdentification:

    @constructor
    def __init__(self, ProvinceDigits, RandomDigits, VerificationDigit):
        self.ProvinceDigits = ProvinceDigits
        self.RandomDigits = RandomDigits
        self.VerificationDigit = VerificationDigit
        self.UserIdentification = ProvinceDigits + RandomDigits + VerificationDigit

    @property
    def ProvinceDigits(self):  # Getter
        return self.ProvinceDigits

    @property
    def RandomDigits(self):  # Getter
        return self.RandomDigits

    @property
    def VerificationDigit(self):  # Getter
        return self.VerificationDigit

    @ProvinceDigits.setter
    def ProvinceDigits(self, ProvinceDigits):  # Setter
        if int(ProvinceDigits) > 0 and int(ProvinceDigits) <= 24 or int(ProvinceDigits) == 30:
            self.ProvinceDigits = ProvinceDigits
        else:
            raise ValueError(
                "Invalid identification number, it must be start with a number between 1 and 24 or 30")

    @RandomDigits.setter
    def RandomDigits(self, RandomDigits):  # Setter
        if len(RandomDigits) < 8:
            raise ValueError(
                "Invalid identification number, it must be 10 digits")
        else:
            self.RandomDigits = RandomDigits

    @VerificationDigit.setter
    def VerificationDigit(self, VerificationDigit):  # Setter
        if int(VerificationDigit) != verificationDigitValidation(self.UserIdentification):
            raise VerificationDigitValueError("Invalid identification number, try again")
        else:
            self.VerificationDigit = VerificationDigit

    @property
    def __str__(self):
        return "Identificaction number: " + self.ProvinceDigits + self.RandomDigits + self.VerificationDigit


# Error de verificación del ultimo digito
class VerificationDigitValueError(ValueError):
    def __init__(self, message):
        super(VerificationDigitValueError, self).__init__(message)


# Load the JSON file
def loadJSON():
    with open('provincias.json', 'r') as file:
        provincias = json.load(file)
        return provincias


# Validation of the first two digit of the identification number
def provinceDigitValidation(UserIdentification):
    if UserIdentification.isdigit() and len(UserIdentification) == 10:
        if int(UserIdentification[0:2]) > 0 and int(UserIdentification[0:2]) <= 24:
            return "Valid"

        elif int(UserIdentification[0:2]) == 30:
            return "Valid. This is a foreigner"

        else:
            return "Invalid"

    else:
        return "Invalid identification number, it must be 10 digits"


def verificationDigitValidation(UserIdentification):
    impares = []
    pares = []

    # Primero: se agrupan los primeros nueves dígitos en dos conjuntos, uno para los pares y otro para los impares.
    for i in range(9):
        if((i + 1) % 2 == 0):
            pares.append(int(UserIdentification[i]))
        else:
            impares.append(int(UserIdentification[i]))

    arr_pares = np.array(pares)
    arr_impares = np.array(impares)

    # Segundo: A los digitos de las posiciones impares se les multiplica por 2.
    arr_impares = arr_impares * 2
    for n in range(len(arr_impares)):
        if arr_impares[n] > 9:
            arr_impares[n] = arr_impares[n] - 9

    # Tercero: Se suman todos los digitos de los conjuntos pares y mas los resultados de los impares.
    sum = np.sum(arr_pares) + np.sum(arr_impares)

    # Cuarto: Se obtiene el resto de la suma anterior dividido por 10.
    rest = sum % 10

    # Quinto: Se obtiene el digito de verificación.
    if rest != UserIdentification[9]:
        rest = 10 - rest

    return rest


while True:

    try:
        userIdentification = input("Enter your identification: ")
        provincias = loadJSON()
        for i in range(len(userIdentification)):
            if userIdentification[i].isdigit() == False:
                print("Invalid identification number, it must be only digits")
        
        if provinceDigitValidation(userIdentification) != "Invalid":
            if verificationDigitValidation(userIdentification) == int(userIdentification[-1]):
                print("Valid identification number")
                print("UserID: ", userIdentification)
                print("Province: ", provincias[userIdentification[0:2]])
            else:
                print("Invalid identification number, try again")
        else:
            print("Invalid identification number, the first two digits must be between 1 and 24 or 30")
        break

    except ValueError:
        print("Invalid identification")
    except KeyboardInterrupt:
        R = input("\n\nAre you sure you want to exit? (Y/N)")

        if R.upper() == "Y":
            print("\nGoodbye.  Thank you for using this program.")
            break
        else:
            continue
