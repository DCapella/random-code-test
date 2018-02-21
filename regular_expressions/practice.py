import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
    [\s\w,\d]*\s(?P<email>[-.+\w\d]+@[-.\w\d]+)
    [\s\w,\d]*\s(?P<phone>[\d]+-[\d]+-[\d]+)
''', string, re.X|re.M)

print(contacts.groupdict()['email'])
