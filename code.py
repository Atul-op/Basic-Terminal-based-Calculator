class code:
    def main():
        a = int(input("Enter a : "))
        b = int(input("Enter b : "))
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