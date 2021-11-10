from random import randint

from game_data import data
from art import logo, vs

FINAL_SCORE = "Sorry, that's wrong. Final score:"
USER_INPUT = "Who has more followers? Type 'A' or 'B: "


def get_data_str(single_element):
    return f" {single_element['name']}, a {single_element['description']}, from {single_element['country']}."


def get_random_element_from_list(list_of_elements):
    return list_of_elements[randint(0, len(list_of_elements) - 1)]


def calculate_correct_answer(person_a_followers, person_b_followers):
    return 'A' if person_a_followers > person_b_followers else 'B'


def game_core(followers_a, followers_b):
    score = 0
    # while
    if calculate_correct_answer(followers_a, followers_b):
        score += 1
        return


def print_challenge(person_a, person_b):
    print('\nCompare A:' + get_data_str(person_a))
    print(vs)
    print('\nAgainst B:' + get_data_str(person_b))


def prompt():
    score = 0
    list_data = data
    
    person_a = get_random_element_from_list(data)
    list_data.remove(person_a)

    person_b = get_random_element_from_list(list_data)
    list_data.remove(person_b)

    print(logo)

    while True:
        print_challenge(person_a, person_b)

        answer = input(USER_INPUT)
        correct_answer = calculate_correct_answer(person_a['follower_count'], person_b['follower_count'])

        if answer != correct_answer:
            print(f"{FINAL_SCORE} {score}")
            exit(0)
        else:
            score += 1
            person_a = person_a if correct_answer == 'A' else person_b

            if len(list_data) == 0:
                list_data = data
                list_data.remove(person_a)
                list_data.remove(person_b)

            person_b = get_random_element_from_list(list_data)
            list_data.remove(person_b)


if __name__ == '__main__':
    prompt()

