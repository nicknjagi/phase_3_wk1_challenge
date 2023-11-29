# Phase 3 Week 1(Toy Problems)

### Tech used
 - Python

#### Installations / How to use
  1. Clone the repo.
  2. ```cd``` to cloned repo and open the folder in vscode
  2. Open the terminal in vscode and run:
    - ```pipenv install``` to install dependencies.
    - ```pipenv shell``` to activate the project's virtualenv. 
    - ```pytest``` to see if all tests pass


### Challenge 1: Converting 12-hour time to 24-hour time

This function accepts an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input and returns a four-digit string that encodes that time in 24-hour time.

e.g.
```
$ 12-hour Time: 8:30 am
$ 0830
$ python time_converter.py
$ 12-hour Time: 12:30 am
$ 0030
```

### Challenge 2: Two numbers are positive.

This function takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.

e.g.

check_positives(2, 4, -3) returns True
check_positives(-4, 6, 8) returns True
check_positives(4, -6, 9) returns True
check_positives(-4, 6, 0) returns False
check_positives(4, 6, 10) returns False

### Challenge 3: Consonant value

This function accepts a string that has alphabetic characters only and no spaces and returns the highest value of the consonant substrings.

e.g.

solve('zodiacs') returns 26 
solve('strength') returns 57 

### Author

- Twitter - [@nick_njagi](https://www.twitter.com/nick_njagi)

### License
Copyright 2023 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.