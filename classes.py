
class CricketPlayer:
    def __init__(self, name, last_name, birth_year,):
        self.first_name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.scores = []
    
    def add_score(self, score):
        self.scores.append(score)

    


rohit = CricketPlayer("ANANTH", 'Sagar', 2000)
rohit.add_score(40)
print(rohit)