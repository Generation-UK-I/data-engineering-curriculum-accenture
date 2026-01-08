# Databases Exercise

To create a Postgres server and client, we will be using `docker`.

## Prep (duplicated from the slides)

1. Ensure you have Docker Desktop installed and running (you can check with `docker -v`).
1. Ensure you have the `databases-exercise.zip` directory provided by your instructor.
1. Make sure docker is started with `docker --version`
1. Run `docker images ls` - you should have "postgres" and "adminer" in the list
1. Stop any running containers from previous sessions with `docker stop <container_name>`
1. Stop any running containers from previous sessions with `docker rm <container_name>`
1. Remove any running containers from previous sessions
1. Run the following command **inside** the `handouts` directory in a terminal.
    1. This will create both the client and server for us, running on localhost.

  ```sh
  $ docker compose up -d
  ```

  You should get the following output:

  ```sh
 ✔ Container my-postgres   Started
 ✔ Container adminer       Started
  ```

1. Navigate to <http://localhost:8080/> in a browser to see the `Adminer` interface.
1. Log in with the credentials from the slides.
1. Select `SQL Command` on the left.

## Part 1 - using DDL

Ensure you are in the Adminer "SQL Command" page (see above).

1. We'll create our own database with:

  ```sql
  CREATE DATABASE test;
  ```

1. Select `test` in the DB dropdown on the left.
1. Now we'll create our first table with:

  ```sql
  CREATE TABLE person (
    person_id INTEGER GENERATED ALWAYS AS IDENTITY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age INTEGER,
    PRIMARY KEY(person_id)
  );
  ```

1. Let's alter the table by adding a new field:

  ```sql
  ALTER TABLE person
  ADD email varchar(255);
  ```

You now have your very own database, with a single table called `person`.

There's no data in there yet, but you can verify it exists by navigating to <http://localhost:8080/?pgsql=db&username=postgres&db=test&ns=public&table=person>.

---

## Part 2 - Using DML

### Part 2.1 - INSERT

- Insert rows into the `person` table
    - Insert a variety of records
- Use a bulk insert with many values at once

### Part 2.2 - UPDATE

- Try and update some of the rows in the `person` table
    - Update all rows
    - Update only some rows
        - Do this using different conditional selectors (`where` clauses)

### Part 2.3 - DELETE

- Try and delete some rows you created.
    - Delete only some rows
    - Do this using different conditional selectors (`where` clauses)

### Part 2.4 - SELECT

- Build up a SELECT statement one part at a time and start to refine your query
    - Use all of the keywords `SELECT, FROM, WHERE, ORDER BY, LIMIT`

---

## Part 3 - Joins

### Part 3.1 - Database setup

Copy and paste the sql queries from `handouts/join_exercises_setup.sql` into the `Adminer` SQL command window and click the 'execute' button.

Make sure you do all the following exercises in the new `join_exercises` database.

### Part 3.2 - Inner Join

Perform an Inner Join on the customers table with the complaints table.

### Part 3.3 - Left Join

Perform a Left Join on the customers table with the complaints table.

### Part 3.4 - Right Join

Perform a Right Join on the customers table with the complaints table.

### Part 3.5 - Full Outer Join

- Perform a Full Outer Join on the customers table with the complaints table showing the duplicates
- Now adjust the query a little such that duplicates are not shown

---

## Part 4 - Python

This assumes you have a `person` table with at least one row already in it.

The instructor will have provided you with the `solutions/person_database.sql` file for that.

You can either use the above, or any test database and table you have created in this session so far.

### Part 4.1 - requirements

1. Activate a virtual environment (refer back to the Python Ecosystem module if you forgot).
1. Open a terminal in the `handouts` folder.
1. Install the dependencies from `requirements.txt` with:
    1. `python3 -m pip install -r requirements.txt` (MacOS / Unix);
    1. `py -m pip instal -r requirements.txt` (Windows)
    1. `python3 -m pip install -r requirements.txt` (GitBash)

### Part 4.2 - add more code

1. Check your `handouts/.env` file has values matching your database name and table name
    1. If not, update it to match, or run the sample sql given out by the instructor (as in "Part 4 - Python", above)
1. Open a terminal in the `handouts` folder
1. Run the `my_db_app.py` file
1. Inspect the file contents to get an understanding of how it works
1. Using the slides as inspiration:
    1. Fill in the TODO for the connection. Use "with". Code after that will need indenting!
        1. After the "with" is added the file should compile and run but do nothing
    1. Fill in the TODO for the cursor
    1. Fill in the TODO for the insert
    1. Fill in the TODO for the commit
    1. Fill in the TODO for the select
    1. Fill in the TODO for the print out of the rows
    1. Fill in the TODO for closing the cursor
1. Run the file again to check it works
1. You can verify the insert works by running `SELECT * FROM person` in the Adminer web page

### Optional extra

- Change your `INSERT` code to do a bulk (multi-value) insert
