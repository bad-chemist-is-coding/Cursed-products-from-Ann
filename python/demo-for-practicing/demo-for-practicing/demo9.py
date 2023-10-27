"""
# Practice 1
student_scores ={
    'Ánh': 80,
    'Đức': 84,
    'Huy': 82,
    'Yên': 77,
    'Thương': 69,
}
student_grade = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grade[student] = 'Outstanding'
    elif score > 80:
        student_grade[student] = 'Exceeds expectations'
    elif score > 70:
        student_grade[student] = 'Acceptable'
    else:
        student_grade[student] = 'Fail'
print(student_grade)
"""
'''
# Practice 2:
country = input()
visits = int(input())
list_of_cities = eval(input())  # create list from formatted string
travel_log = [
    {
        'country': 'France',
        'cities': ['Paris', 'Lille', 'Dijon'],
        'visits': 12
    },
    {
        'country': 'Germany',
        'cities': ['Berlin', 'Hamburg', 'Stuttgart'],
        'visits': 5
    },
]


def add_new_country(name, time_visited, cities_visited):
    new_country = {}
    new_country['country'] = name
    new_country['visits'] = time_visited
    new_country['cities'] = cities_visited
    travel_log.append(new_country)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
'''
# Practice 3:
import time

bid = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')


while not bidding_finished:
    name = input('What is your name?\n')
    price = int(input('How is your bid?\n$'))
    bid[name] = price
    should_continue = input('Any other binders? Type "Yes" or "No".\n').lower()
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bid)
    elif should_continue == 'yes':
        print('NEXT PERSON!')
        time.sleep(1)