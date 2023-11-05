from game import Game
from game_data import Question, ParseFile
from game_status import GameStatus

print(Question.upload_questions('Questions.csv'))
g = Game(0)
print(g.get_status())
g.start_game()
print(g.get_status())

while g.get_status() == GameStatus.IN_PROGRESS:
    g.get_current_question()
    g.set_answer()
    g.check_answer()
    g.next_question()
    print(g.get_status())


