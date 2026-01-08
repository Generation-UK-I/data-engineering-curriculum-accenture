from sql_utils import *

### SETUP THE DATABASE

connection, cursor = setup_db_connection()
create_db_tables(connection, cursor) # set up the sql tables that we will be loading to

### EXTRACT

# 1. Read the sales_data.csv

### TRANSFORM

# 2. Clean that data (minimum requirement is to remove any rows that contain null cells).
# 3. Filter data for the period 1 December 2020 - 5 December 2020
# 4. Calculate each customer's total spend
# 5. Calculate each customer's average spend
# 6. Calculate how many times each customer has purchased a specific item


### LOAD

# 7. Load the transformed data to the created tables
