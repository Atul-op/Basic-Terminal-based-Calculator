class code:
    def main():
        a = float(input("Enter a : "))
        b = float(input("Enter b : "))
        operator = input("Enter Operator : ")
        if(operator == '+'):
            print("Answer :",(a+b))
        elif(operator == '-'):
            print("Answer :",(a-b))
        elif(operator == '*'):
            print("Answer :",(a*b))
        elif(operator == '/'):
            print("Answer :",(a/b))
        elif(operator == '//'):
            print("Answer :",(a//b))
        elif(operator == '%'):
            print("Answer :",(a%b))
        elif(operator == '**'):
            print("Answer :",(a**b))
        else:
            print("Invalid Operator!!")

    if __name__ == "__main__":
        main()