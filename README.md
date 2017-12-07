# pbc-Lysenko
Repository was created for completing home tasks in PBC course.

## *Environment*

The python 2.7 should be installed to run this application and unit tests properly.
All needed modules/packages you can installed using pip and attached requirements.txt in root of this repo:
* `python virtualenv venv` - creates a virtual environment
* `source venv/bin/activate` - activates virtual environment
* `pip install -r requirements.txt` - installing packages from requirements.txt


## *Vagrantfile*
Attached Vagrantfile in root helps configure and run VM - `ubuntu/trusty64`
You can connect to VM using `ssh vagrant@192.168.33.10`, password - `vagrant`. 
[Short tutorial how to deal with vagrant](https://www.sitepoint.com/getting-started-vagrant-windows/)


## my_app
Main module with such modules:
* fibonacci.py - prints [Fibonacci's sequence](https://en.wikipedia.org/wiki/Fibonacci_number) - `fibonacci.py --length 3` --> `[0, 1, 1, 2]`
* log_wrapper.py - decorator which prints function name and input before execution.
* unique_pairs.py - returns unique pairs which sum is equal to 10 from sequence `unique_pairs.py --numbers 4 7 6 3 5 1` --> `4+6\n3+7`


## *Tests*

Tests per each function are located in one file. So, to run them separately:
* `pytest tests/BDD_tests.py -m fib` - runs tests for fibonacci-function.
* `pytest tests/BDD_tests.py -m pairs` - runs tests for pairs-function.

Run tests w/o parameters leads to performing them all.


