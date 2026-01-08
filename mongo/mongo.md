---
title: Mongo DB
---

## Mongo DB

---

### Overview

- A history of Mongo DB
- How Mongo DB is different from traditional databases
- How Mongo DB works
- Mongo DB Shell

---

### Learning Objectives

- To Explain what Mongo DB is
- How to interact with Mongo DB
- Setup your own Mongo DB

---

### A brief history of Mongo DB

Mongo DB was founded in 2007 by Dwight Merriman, Eliot Horowitz and Kevin Ryan – the team behind DoubleClick.

Originally released in 2009 as part of a platform as a service product, then it was changed to an open source model.

It was created in response to the frustration of using standard RDBMS that meant a single large instance holding all the data in one place.

---

### What is Mongo DB

Mongo DB is a Database with the following features.

- Cross Platform
- NoSQL Based
- Document Oriented

Mongo DB can be run on a variety of platforms. It also works with multiple languages eg. Java, Python, NodeJS and this allows it to be used in any application.

Notes:
Ask if anyone knows what NoSQL stands for.
Cross Platform - works on Windows, Linux, Mac
NoSQL - Covered in the next slide
Document Oriented - Stores documents of data instead of rows of data

---

### NoSQL

NoSQL means _Not Only_ SQL and not _No_ SQL

It is used to generally cover any database that is not a relational database.

This covers all types including document storage, columnar storage, key-value, graph databases and so on.

Notes:
Ask if anyone can name a database that matches the other types
eg.
Document (data is stored as documents): Mongo
Columnar (data is stored in columns instead of rows): Cassandra
Key-Value (data is stored as key value pairs): Redis
Graph (data is stored in a graph structure): Neo4j

---

### NoSQL vs SQL

NoSQL :

- Dynamic, frequently changing data
- Simple Queries
- Data replicated across multiple regions
- Database works to CAP principles

SQL :

- Highly structured and rigid data
- Complex Queries
- Data is centralised in a single place.
- Database works to ACID principles

---

### Document Oriented

Mongo DB does not work like a traditional RDBMS, it does not work with rows of data in tables.

Mongo holds data in documents in Binary JSON Format or BSON.

Documents are held in collections and databases hold one or more collections of documents.

This allows a developer to store and query data in the same document-model format used in the applications.

Each document has an internal "_id" which is used by Mongo

---

### Document example

The following can be stored as document data within a Mongo DB database. It does not require new tables or schemas, all the associated data can be stored together.

```json
[
    {
        "year" : 1954,
        "title" : "Fellowship of the Ring",
        "author" : "J. R. R. Tolkien",
        "series" : {
            "series_name" : "Lord of the Rings",
            "series_number" : 1
        }
    },
    {
        "year" : 1813,
        "title" : "Pride and Prejudice",
        "author" : "Jane Austen"
    }
]
```

---

### Quiz Time! 🤓

What does NoSQL stand for?

1. _No_ SQL
1. _Nicely Organised_ SQL
1. _Not Only_ SQL
1. _Named Object_ SQL

Answer: `3`<!-- .element: class="fragment" -->

---

### Quiz Time! 🤓

What kind of database is Mongo?

1. Columnar database
1. Document Database
1. Key-Value pair database
1. Graph Database

Answer: `2`<!-- .element: class="fragment" -->

---

### Quiz Time! 🤓

What is stored in Mongo DB?

1. JSON documents
1. Text documents
1. XML documents
1. BSON documents

Answer: `4`<!-- .element: class="fragment" -->

---

## Using Mongo DB

- Mongo Shell
- Databases
- Collections
- Data

---

### Mongo Shell

Mongo comes with an interactive shell called mongosh that is used to access Mongo using javascript

The shell comes either part of a server installation or can downloaded separately

You can use it to connect to a remote server

```sh
> mongosh "mongodb://<server name>:<port>"

> mongosh "mongodb://localhost:28015"

> mongosh "mongodb://mongodb.example.com:28015"
```

This will give a command line prompt to access the Mongo DB instance that is running.

To exit the command prompt type

```sh
> quit()
```

---

### Databases

To show which database you are accessing:

```sh
> db
```

You access a database in Mongo as follows:

```sh
> use myDB
```

If that database does not exist, then Mongo will create it when you first store data in that database.

To see all the databases that exist in the current Mongo installation:

```sh
> show dbs
```

---

### Collections

Collections sit inside a Database and are analogous to tables in an RDBMS

To see all the collections in a database.

```sh
> show collections
```

To create an empty collection, you can use the following

```sh
> myDB.createCollection("myCollection");
```

---

### Accessing Data

To find data in a collection.

database.collection.fund(query)

So to get all the data in a collection

```sh
> myDB.myCollection.find().forEach(printjson)
```

To get data from a collection using a query

```sh
> myDB.myCollection.find({year : "1954"}).forEach(printjson)
```

A query will be a filter to find the data you are looking for like a SQL query.

The forEach(printjson) part prints out the results.

---

### Inserting Data

To insert a single JSON document

```sh
> myDB.myCollection.insertOne(<json document>)
```

To insert an array of JSON documents

```sh
> myDB.myCollection.insertOne(array(<json document>))
```

---

### Updating Data

To update data within the database.

database.collection.update(query, update)

```sh
> myDB.myCollection.update({year:"1954"},
    {
        $set :
        {
            "name" : "The Fellowship of the Ring",
        }
    }
)
```

The **$set** keyword is used to modify the field name
If the field does not exist, then the set command will append the new field and value to the end of the document.

---

### More Updating Data

```sh
database.collection.updateOne(filter, update)
```

This will update a single document with the update. If more then one document if found by the filter, it will only update the first document found.

```sh
database.collection.updateMany(filter, update)
```

This will update all the rows which match the filter.

---

### Deleting Data

```sh
database.collection.deleteOne(filter)
```

This will delete a single document that matches the filter. If more then one document if found by the filter, it will only delete the first document found.

```sh
database.collection.deleteeMany(filter)
```

This will delete all the rows which match the filter.

To get precision when deleting use the unique "_id" field for the document.

---

### Exercise

Instructor to distribute exercises.

---

### Overview - recap

- A history of Mongo DB
- How Mongo DB is different from traditional databases
- How Mongo DB works
- Mongo DB Shell

---

### Learning Objectives - recap

- To Explain what Mongo DB is
- How to interact with Mongo DB
- Setup your own Mongo DB

---

### Further Reading

[Mongo DB] (https://www.Mongo DB.com/)

[Mongo DB CLI] (https://www.Mongo DB.com/docs/mongocli/master/install/)

[Mongo DB Documentation] (https://www.Mongo DB.com/docs/)

---

### Emoji Check:

On a high level, do you think you understand the main concepts of this session? Say so if not!

1. 😢 Haven't a clue, please help!
2. 🙁 I'm starting to get it but need to go over some of it please
3. 😐 Ok. With a bit of help and practice, yes
4. 🙂 Yes, with team collaboration could try it
5. 😀 Yes, enough to start working on it collaboratively

Notes:
The phrasing is such that all answers invite collaborative effort, none require solo knowledge.

The 1-5 are looking at (a) understanding of content and (b) readiness to practice the thing being covered, so:

1. 😢 Haven't a clue what's being discussed, so I certainly can't start practising it (play MC Hammer song)
2. 🙁 I'm starting to get it but need more clarity before I'm ready to begin practising it with others
3. 😐 I understand enough to begin practising it with others in a really basic way
4. 🙂 I understand a majority of what's being discussed, and I feel ready to practice this with others and begin to deepen the practice
5. 😀 I understand all (or at the majority) of what's being discussed, and I feel ready to practice this in depth with others and explore more advanced areas of the content
