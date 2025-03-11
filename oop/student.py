class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f'{self.name}({self.student_id})'

    @property
    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A'
        if avg >= 80:
            return 'B'
        return 'C'

    def copy_scores(self):
        # 복습: 리스트 복사 주의
        return list(self.scores)

if __name__ == '__main__':
    s = Student('민수', '2024001')
    s.add_score(88)
    s.add_score(92)
    print(s, s.average(), s.grade)
    print('copy', s.copy_scores())

# 메모: 점수 평균 반올림은 나중에
