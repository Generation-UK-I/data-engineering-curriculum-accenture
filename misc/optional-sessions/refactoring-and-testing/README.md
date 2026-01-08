## Application Refactoring and Testing

This optional session was delivered as a code along session to show how to break down a more complicated program into smaller functions and how the individual parts could be tested.

The goal is to highlight the difference between how difficult it can be to test a larger program than a smaller one made of many components.

There are no pre-requisites for running this other than to read through the files and understand how they are broken down.

The session should focus on splitting down the `full.py` file, so that all the functions are moved into the `functions.py` file and the user calls the `app.py` file.

The commented numbers are to highlight the complexity and number of functions that the original program has.

As the function are broken out, the testing should also be incorporated showing how simple unit tests can be created to fully test

Initially, the functions can be simply tested using basic asserts with a more complex version uses Testcase.
