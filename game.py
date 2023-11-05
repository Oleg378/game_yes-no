# Реализовать известную игру "верю не верю" (или "истина или ложь").
#
#   Смысл игры: есть файл в формате .csv, который содержит вопросы или утверждения, правильные ответы
#    к ним и пояснения к ответам. Пример файла прикреплён к лекции. Скачав файл, вы увидите его формат:
#   файл построчный, в каждой строке есть вопрос-ответ-объяснение. Компьютер задаёт игроку вопросы из файла.
#   Игрок должен отвечать "да" или "нет" ("y" or "n"). Кол-во ошибок ограничено. Если ошибок слишком много - проигрыш,
#   если игрок дошёл до конца и не превысил дозволенное кол-во ошибок - победа.
#
# Требования к реализации.
#   Разработать класс, реализующий логику игры:
#   позволяет клиентскому коду задать путь к файлу и задать максимальное кол-во ошибок
#   позволяет клиентскому коду запросить следующий вопрос
#   позволяет клиентскому коду дать ответ на вопрос
#   позволяет клиентскому коду запросить статус игры (в прогрессе, закончилась)
#
# Разработать клиентскую часть, которая  организует цикл, в котором пользуется API класса
#   (реализующего логику игры), и выводит все необходимые строки для общения с игроком, показывает
#   вопросы, поздравляет с победой и уведомляет о поражении.
from yes_no.game_data import ParseFile
from yes_no.game_status import GameStatus


class Game:
    def __init__(self, max_mistakes=3):
        self.questions = ParseFile.list_riddles
        self.game_status = GameStatus.NOT_STARTED
        self.current_question = 0
        self.current_answer = None
        self.max_mistakes = max_mistakes
        self.current_mistake = 0

    def start_game(self):
        if self.game_status != GameStatus.NOT_STARTED:
            raise Exception("You can't start game!")
        self.game_status = GameStatus.IN_PROGRESS

    def get_current_question(self):
        print(self.questions[self.current_question].question)

    def set_answer(self):
        self.current_answer = input('Fill answer (Y/N): ').lower()
        if self.current_answer == 'y':
            self.current_answer = 'Yes'
        elif self.current_answer == 'n':
            self.current_answer = 'No'
        else:
            self.current_answer = None
        print('Answer accepted')

    def check_answer(self):
        if self.current_answer == self.questions[self.current_question].answer:
            print("You're right!")
        else:
            print(f"You're wrong! rest of mistakes: {self.max_mistakes - self.current_mistake - 1}")
            self.current_mistake += 1
        print(f'explanation: {self.questions[self.current_question].explanation}')

    def next_question(self):
        if self.current_mistake > self.max_mistakes:
            self.game_status = GameStatus.LOST
            print("You've used all tries, game over!")
        if self.current_question + 1 == len(self.questions):
            self.game_status = GameStatus.WON
            print('You win!')
        else:
            self.current_question += 1
            print('___________next round!___________')

    def get_status(self):
        return self.game_status

# for i in ParseFile.list_riddles:
#     if GameStatus.LOST:
#         raise Exception("Sorry, you lost. Try again!")
