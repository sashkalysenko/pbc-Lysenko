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


## *app.py*
To run any application from my_app (fibonacci or unique pairs) you can use module app.py
Example how to run fibonacci:
* `app.py -fib 10` - prints first 10 numbers of Fibonacci sequence
* `app.py -up 3 7 4 6 8 9` - prints unique pairs which sum is equal to 10  

NOTE: you can use both parameters in the same time to run fibonacci and unique pairs. 


## my_app
Main module with such modules:
* fibonacci.py - prints [Fibonacci's sequence](https://en.wikipedia.org/wiki/Fibonacci_number) - `fibonacci.py --length 3` --> `[0, 1, 1, 2]`
* log_wrapper.py - decorator which prints function name and input before execution.
* unique_pairs.py - returns unique pairs which sum is equal to 10 from sequence `unique_pairs.py --numbers 4 7 6 3 5 1` --> `4+6\n3+7`


## *Tests*

To run all tests:
* `pytest tests` - runs all the created unit tests
* `pytest tests -m pairs/fib` - runs tests for pairs/fibonacci functions accordingly.

Run tests w/o parameters leads to performing them all.


## *Fixtures*

Contains module with class ConnectorSSH, which helps connect to VM via SSH.
To initiate an object, set ip, name and password of VM.
Also, the class has method to set_up selenium grid standalone server v 3.8.0 on connected VM.
*NOTE* - currently the fixture is used in "test/test_sel_grid.py". Test does nothing, just sets up grid server.



