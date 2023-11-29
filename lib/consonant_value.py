def main():
    solve('strength')

def solve(string):
    # initialize empty list for storing the totals
    totals_list = []
    current_total = 0
    # iterate over the string while getting the total
    for letter in str(string):
        if letter not in ['a','e','i','o','u']:
            # convert current letter to its unicode representation and subtract 96
            current_total += ord(letter.lower()) - 96
        else:
            totals_list.append(current_total)
            current_total = 0

    totals_list.append(current_total)
        
    print(max(totals_list))
    return max(totals_list)
    
if __name__ == '__main__':
    main()
    