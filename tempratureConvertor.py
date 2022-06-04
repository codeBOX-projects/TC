#!/bin/env python3

class TempratureConvertor:
    @staticmethod
    def discruption():
        info = """        
    ████████╗░█████╗░
    ╚══██╔══╝██╔══██╗
    ░░░██║░░░██║░░╚═╝
    ░░░██║░░░██║░░██╗
    ░░░██║░░░╚█████╔╝
    ░░░╚═╝░░░░╚════╝░
    
    [*] [code]BOX - Andrei A.Abd 2022.
    [*] Temperature converter Celsius to Fahrenheit or vice versa.
    [*] Source: https://www.github.com/codeBOX-projects
        
        """
        print(info)
        
    @staticmethod
    def celsuis_to_fehranhiet(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fehranhiet_to_celsuis(f):
        return 5 * (f - 32) / 9

if __name__ == ('__main__'):
    TempratureConvertor.discruption() 
    print("\n1 : Celsuis (convert celsuis into fehranhiet).\n2 : Fehranhiet (convert fehranhiet into celsuis).\n")
    getOption = input("> select convert type: ")
    try:
        if getOption == "1":
            getNumber = input("> type value: ")
            if getNumber != "": 
                result = TempratureConvertor.celsuis_to_fehranhiet(int(getNumber))
                print(f"\n[*] Result = {result} Fehranhiet.")
            else:
                print(f"Error {getNumber}: not correct value")
        
        elif getOption == "2":
            getNumber = input("> type value: ")
            if getNumber != "":
                result = TempratureConvertor.fehranhiet_to_celsuis(int(getNumber))
                print(f"\n[*] Result = {result} Celsuis.")
            else:
                print(f"Error {getNumber}: not correct value")
                
        else:
            print(f"Error {getOption}: not found!")
    except:
        pass