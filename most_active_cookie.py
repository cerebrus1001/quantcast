#############################
##### Author: Aaron Lee #####
#############################

'''
Run on Windows with 
python ./most_active_cookie.py <cookie csv file> -d <YYYY-MM-DD date format> 
On Linux should work with ./most_active_cookie <cookie csv file> -d <YYYY-MM-DD date format> 
but havent tested it due to unavailability of system
'''


import argparse



def get_most_active_cookie(file, date):
    '''
    Gets the most active cookie in <file> on <date>. Basic
    Solution that uses O(n) memory and O(n) time

    params: 
    file - csv file containing date in form of <cookie>,<timestamp>

    date - date argument entered from command line

    returns cookie that appears more frequently on date
    '''
    cookie_frequencies = {'error': -1}
    with open(file, 'r') as csvfile:
        for line in csvfile:
            try:
                cookie, timestamp = line.split(',')
                timestamp = timestamp[:10] # extract only date
                if timestamp == date:
                    cookie_frequencies[cookie] = cookie_frequencies.get(cookie, 0) + 1
            except Exception as emsg:
                print(emsg)
                raise
            
    return max(cookie_frequencies, key=cookie_frequencies.get)

if __name__ == '__main__':
    # create parser
    parser = argparse.ArgumentParser(description="Get most frequent cookie(s)")

    # add arguments
    parser.add_argument('log_file', help='log file to process')
    parser.add_argument('-d', type=str, required=True, help='date in YYYY-MM-DD')

    # parse argument
    args = parser.parse_args()

    file = args.log_file
    date = args.d
    print(get_most_active_cookie(file, date))