#계산기 기능 선택하기 (더하기, 빼기, 곱하기, 나누기, 곱셈)


print("Please, choose which calculator function you want to use")
while True:
    try:
        option = int(input("Choose which function you want to use\n"
                   "1. plus\n"
                   "2. minus\n"
                   "3. multiply\n"
                   "4. divide\n"
                   "5. power\n"
                   ": "))
# 계산기 기능 넣기
        if option < 6:
            if option == 1:
                number1 = int(input("please, put a number: "))
                number2 = int(input("please, put a another "))
                print(f"result: {number1 + number2}")
                ask = input("Do you want to continue or not? Y/N ")
# and 와 or 를 쓸때, 변수기입 잘하기. Whiletrue loop에서 FALSE or True와 같은 방식이 될수있음. 문자열이 있는것 자체가 true임.
                if ask in ["Y", "y"]:
                    continue
                elif ask in ["N", "n"]:
                    print("Good bye")
                    break
                else:
                    print("I can't understand\n")

            elif option == 2:
                number1 = int(input("please, put a number: "))
                number2 = int(input("please, put a another: "))
                print(f"result: {number1 - number2}")
                ask = input("Do you want to continue or not? Y/N ")
                if ask == "Y" or ask == "y":
                    continue
                elif ask == "N" or ask == "n":
                    print("Good bye")
                    break
                else:
                    print("I can't understand\n")

            elif option == 3:
                number1 = int(input("please, put a number: "))
                number2 = int(input("please, put a another: "))
                print(f"result: {number1 * number2}")
                ask = input("Do you want to continue or not? Y/N ")
                if ask == "Y" or ask == "y":
                    continue
                elif ask == "N" or ask == "n":
                    print("Good bye")
                    break
                else:
                    print("I can't understand\n")

            elif option == 4:
                number1 = int(input("please, put a number: "))
                number2 = int(input("please, put a another: "))
                print(f"result: {number1 / number2}")
                ask = input("Do you want to continue or not? Y/N ")
                if ask == "Y" or ask == "y":
                    continue
                elif ask == "N" or ask == "n":
                    print("Good bye")
                    break
                else:
                    print("I can't understand\n")

            elif option == 5:
                number1 = int(input("please, put a number: "))
                number2 = int(input("please, put a another: "))
                print(f"result: {number1 ** number2}")
                ask = input("Do you want to continue or not? Y/N ")
                if ask == "Y" or ask == "y":
                    continue
                elif ask == "N" or ask == "n":
                    print("Good bye")
                    break
                else:
                    print("I can't understand\n")

        else:
            print("Please choose a number in the list\n")
            continue
    except ValueError:
        print("I can't understand. You have to put a number\n")
        continue





