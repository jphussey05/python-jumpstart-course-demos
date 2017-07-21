import collections

lookup = {}
lookup = dict()
lookup = {'age': 42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')


class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name


gandalf = Wizard('Gandalf', 42)

print(gandalf.__dict__)

print(lookup)
print(lookup['loc'])

lookup['cat'] = 'Fun code demo'

if 'cat' in lookup:
    print(lookup['cat'])

User = collections.namedtuple('User',
                              'id, name, email')
users = [
    User(1, 'user1', 'user1@aol.com'),
    User(2, 'user2', 'user2@aol.com'),
    User(3, 'user3', 'user3@aol.com'),
    User(4, 'user4', 'user4@aol.com'),
]

lookup = dict()

for u in users:
    lookup[u.id] = u

print(lookup[3])