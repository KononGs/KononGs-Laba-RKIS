import random

def compare_numbers(number, user):
    cowbull = [0,0]
    for i in range(len(number)):
        if number[i] == user[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull

if __name__=="__main__":
    playing = True
    number = str(random.randint(0,9999))
    users = 0

    while playing:
        user = input("Введите число!")
        if user == "exit":
            break
        cowbullcount = compare_numbers(number,user)
        users+=1

        print(str(cowbullcount[0]) + " корова и " + str(cowbullcount[1]) + " бык.")

        if cowbullcount[1]==4:
            playing = False
            print("You win the game after " + str(users) + "! The number was "+str(number))
            break
        else:
            print("Ответ неверный, попробуйте еще раз!")
