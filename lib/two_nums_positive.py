def main():
    check_positives(-1,3,4)

def check_positives(*args):
    if len(args) == 3:
        count = 0
        for num in args:
            if num > 0:
                count += 1
                
        print(True if count == 2 else False)
        return True if count == 2 else False
    
if __name__ == '__main__':
    main()