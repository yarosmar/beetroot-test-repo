class Team:
    def __init__(self):
        self.members = list()
        self.counter = 0

    def __iter__(self):
        return self
    
    def addMembers(self, members):
        self.members.extend(members)

    def __getitem__(self, index):
        return self.members[index]

    def __next__(self):
        if self.counter < len(self.members):
            result = self.members[self.counter]
            self.counter += 1
            return result
        raise StopIteration

team = Team()
team.addMembers(["John", "Bob", "Kate"])
for member in team:
    print(member)
