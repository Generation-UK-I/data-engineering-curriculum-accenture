## Build a simple API with Flask

This optional sessions was delivered as a live demo / code-along to show people some of the basis of how APIs work. It creates a very simple 'to-do list' style app with a (fat) controller and and a database handler.

There are some pre-requisites for running this:

- Spin up a virtual env and install all requirements from requirements.txt
- Use the docker compose file to spin up docker containers with MySQL and adminer
- Installing and using Postman made calling our api simpler, but can equally use CURL from the command line

The sessions should focus on building up the `app.py` file - starting with an empty version (or just start with a simple 'hello world' GET endpoint) and building it endpoint by endpoint, until it resembles the current `app.py` in this directory

The code isn't particularly elegant, and is completely untested, but the purpose of this exercise is more around getting learners to understand endpoints, and how to build them up, and use of the different HTTP verbs etc
