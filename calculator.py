# Program make a simple calculator

import calcFunction as cf

def isContinued():

    continued = None  # 진행 여부에 대한 변수
    while True: 
        next_calculation = input("Let's do next calculation? (yes/no): ").lower()  # 받은 입력을 소문자로 변경
        if next_calculation == "yes":  # 계속 진행
            continued = True
        elif next_calculation == "no":
            reply = input("Are you sure? (yes/no)").lower()  # 재확인
            if reply == "yes":  # 다음 연산 진행 하지 않음
                continued = False  # 진행하지 않으므로 False 로 변경
            elif reply == "no":  # 계속 진행
                continued = True

        if continued is not None:  # 다음 진행 여부가 결정되었다면 루프 탈풀
            break
        print("Please answer yes or no.")  # yes/no 이외의 입력이 들어온 모든 경우에 출력됨

    return continued


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", cf.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", cf.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", cf.multiply(num1, num2))
        
        elif choice == '4':
            if num2 == 0:
                print("Can't divide")
            else:
                print(num1, "/", num2, "=", cf.divide(num1, num2))

        if not isContinued():  # 종료 여부를 결정할 함수, False 가 리턴되면 계산기 종료 
            break
    else:
        print("Invalid Input")
