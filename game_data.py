from dataclasses import dataclass


class ParseFile:
    list_riddles = []

    @staticmethod
    def open_file(file_name):
        with open(file_name, mode='r') as file:
            rare_data = file.read()
        return rare_data.split('\n')


@dataclass(frozen=True)
class Question(ParseFile):
    question: str
    answer: str
    explanation: str

    @classmethod
    def upload_questions(cls, file):
        lst = ParseFile.open_file(file)
        for i in lst:
            split_line = i.split(';')
            question = split_line[0]
            answer = split_line[1]
            explanation = split_line[2]
            ParseFile.list_riddles.append(cls(question, answer, explanation))
        return 'Instances were created!'


