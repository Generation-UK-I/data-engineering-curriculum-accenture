# Intro To Unit testing

This code-along introduces learners to the basic concept of unit testing. It's designed to build their confidence and help them understand how to write unit tests.

## Prep

Copy the `app.py`, `tests.py`, and `example.txt` file locally.

- `app.py` - 4 basic CRUD functions
- `tests.py` - 8 suggested tests based on functions in `app.py`
- `example.txt` - text file containing 3 separate values

Have `unittest-answers.py` open on a separate screen.

## Session

- Along with help from the learners, write and run each of the suggested unit tests
- As you go, introduce:

    ```py
    print(f'Expected value = {expected}')
    print(f'Actual value = {actual}')
    ```

- The final test will fail, this is an opportunity to demo some basic Test Driven Development. Use the code above to print the expected and actual values, the learners will see that the whitespace makes the test fail
- Ask the learners how they would adapt the code in the `read_txt()` function to make it pass the test
- One solution is to put the code below into the `for loop` in the `read_txt()` function.

    ```py
        line = line.strip()
    ```

- Once the suggested tests are complete, ask the learners for more test suggestions
