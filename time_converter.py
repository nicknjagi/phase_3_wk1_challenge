def main():
    while True:
        # get input from user
        time = input('12-hour Time: ')
        # print if time is in the correct format otherwise reprompt
        if len(time.split(' ')) == 2:
            if is_valid(time):
                print(convert_time(time))
                return convert_time(time)
            else:
                print('Please enter a valid time')
        else:
            print('Please use this format - 8:30 pm')

#  converts time to 24 hr format
def convert_time(time):
    period = time.split(' ')[1]
    time_list = time.split(' ')[0].split(':')
    hour = time_list[0] if len(time_list[0]) > 1 else '0' + time_list[0]
    minutes = time_list[1] if len(time_list[1]) > 1 else '0' + time_list[1]
    
    if period == 'am':
        hour = hour if int(hour) < 12 else '00'
        return hour + minutes
    else: 
        hour = (int(hour) + 12) if hour != '12' else 12
        return str(hour) + minutes
    
def is_valid(time):
    time_list = time.split(' ')[0].split(':')
    hour = time_list[0] 
    minutes = time_list[1] 
    
    if int(hour) in range(1,13) and int(minutes) in range(0,60):
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()