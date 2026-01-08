# ETL Solutions

- The file `solution-with-sql.py`
    - This file solves the exercise by using a sequence of sql tables
    - It loads the info into a `sales_data` table
    - Then uses a sequence of `INSERT/SELECT` statements to fullfil the following asks
- The file `solution-in-memory.py`
    - This solves the exercise by loading the data into memory
    - Then in-memory working out the next ask
    - Then saves the data in the same tables as above
    - The functions in this file are written in a very "Jupyter Notebooks" style, i.e everything is global variable

Notes on the information/insights they should see from the data transformations:

- `2194` - low frequency spends, large amounts, buys the same product each time
- `5632` - medium frequency spends, medium amounts, buys three products
- `7365` - high frequency spends, small amounts, buys a different product each time
