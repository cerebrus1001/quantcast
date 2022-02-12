from most_active_cookie import get_most_active_cookie
import datetime
import random

def generate_random_dates(num_generate, test_file='test.txt', range1=(2020,1,1), 
range2=(2020,1,2), chosen_test_date='2020-01-01'):
    ''' 
    Generates a .txt file to be used for testing with
    A,B,C as cookies within date range (M,D,Y) 1/1/2020 -> 1/5/2020
    params: 
    num_generate - number of dates to generate
    test_file - name of test file
    range1 - date start in format YYYY, M, D
    range2 - date end in format YYYY, M, D
    chosen_test_date - date to test with the date in get_most_active_cookie
    returns: dictionary of cookies to frequency
    '''
    start_date = datetime.date(*range1)
    end_date = datetime.date(*range2)

    cookie_choices = ['A', 'B', 'C']
    cookie_freq_dict = {'A': 0, 'B': 0, 'C': 0}
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    with open(test_file, 'w') as file:
        for _ in range(num_generate):
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            choice = random.choice(cookie_choices)
            if str(random_date) == chosen_test_date:
                cookie_freq_dict[choice] += 1
            file.write(choice + ',' + str(random_date) + '\n')
    return cookie_freq_dict

cookie_freq_dict = generate_random_dates(1)
assert(get_most_active_cookie('test.txt', '2020-01-01') 
== max(cookie_freq_dict, key=cookie_freq_dict.get))

cookie_freq_dict = generate_random_dates(1000, range1=(2020,1,1), range2=(2020,1,10))
assert(get_most_active_cookie('test.txt', '2020-01-01')
== max(cookie_freq_dict, key=cookie_freq_dict.get))

cookie_freq_dict = generate_random_dates(10000)
assert(get_most_active_cookie('test.txt', '2020-01-01') 
== max(cookie_freq_dict, key=cookie_freq_dict.get))
