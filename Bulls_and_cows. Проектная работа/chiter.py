import game

answers = game.get_all_answers()
counter = 0
while len(answers) > 1:
    counter += 1
    print('Ход номер: ', counter)
    print('Возможных вариантов ответа: ', len(answers))
    ans = game.get_one_answer(answers)
    print('Назови комбинацию: ', ans)
    bulls = int(input('Сколько быков? '))
    if bulls == 4:
        break
    cows = int(input('Сколько коров? '))
    answers = game.del_bad_answers(answers, ans, bulls, cows)
print('Ответ: ', answers)

# 1234