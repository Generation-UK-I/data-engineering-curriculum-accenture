## Data Cleansing Exercise

Needs Docker running - see also the Docker session.

### Introduction

Often times, data folk will need to deal with 'messy' data. This can mean it can have missing values, inconsistent formatting, malformed data or other outliers.

We now want to apply cleaning steps to fix some of the problems in the dirty data we looked at earlier. The business has decided to focus on the following five issues to correct:

- Ensuring integer columns do not contain anything other than numbers
- Ensuring teacher names are only from a valid list of options
- Ensuring student IDs are not duplicated
- Ensuring dates are in the correct format
- Ensuring that there are no nulls in any of the columns

(_Note: these are not necessarily rules to be applied all the time when performing data cleansing. What steps you take to clean data depends on the data and the business decisions._)

In the `handouts` folder, the file `etl_with_cleansing.py` has been half-written with some functions to let us correct these issues.

**HINT**: _Reading the unit tests will tell you what each function needs to do._

**HINT**: _Running the unit tests will tell you if your functions do the right thing!_

## Prep

Before running the `etl_with_cleansing.py` file:

1. Ensure your Adminer and MySQL containers are running.
    - If not, inside the handouts folder run the command: `docker compose up -d`
1. In Adminer, create a new database called `data_cleansing` with the command:
    - `CREATE DATABASE data_cleansing;`
1. Make sure you have an active `venv`
1. Install the `requirements.txt` file from the handouts using the command:
    - `py -m pip install -r requirements.txt` (Windows)
    - `python3 -m pip install -r requirements.txt` (MacOS / Unix)
    - `python -m pip install -r requirements.txt` (GitBash)

### Provided unit tests

There are some provided unit tests you can run to validate your function code!

You can test your functions by running the following command from within the `handouts` folder:

```sh
# Mac/Unix
$ python3 -m pytest -v
# or on Windows
$ py -m pytest -v
```

### Part 1

Open `etl_with_cleansing.py` and finish the functions with the following requirements:

1. `check_integer_columns`:
    - For each dictionary in the argument `list_of_dicts`, check each column in the argument `int_cols`
    - Convert the value found at that dictionary key to integer
    - If there is a ValueError, set the value to `None`
    - Return the updated list of dictionaries

2. `check_values_in_valid_list`:
    - For each dictionary in the argument `list_of_dicts`, check if the value found at the dictionary key given in the argument `valid_items`
    - If the value is in the list, leave the value as is
    - If the value is NOT in the list, set the value to `None`
    - Return the updated list of dictionaries

3. `drop_duplicate_ids`:
    - For each dictionary in the argument `list_of_dicts`, check if the value found at the dictionary key `id` already exists
    - If the `id` value is new, append the dictionary to a new list
    - If the value is NOT new, ignore the dictionary and move on to the next
    - Return the new list of dictionaries
    Hint: you can use another list to track the `id` values

4. `drop_rows_with_null`:
    - If there are no null/None or empty string values in the dictionary, append it to a new list
    - Return the new list of dictionaries

### Part 2

For each of the four functions you updated, write down which of the five elements of data quality was corrected, i.e.:

- Validity
- Accuracy
- Consistency
- Completeness
- Uniformity

### Bonus

Have a look at the function `convert_all_dates`. What is it doing?

Can you think of any examples where this function will fail to catch an incorrect date?
