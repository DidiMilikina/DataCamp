'''
Connect to a database
In order to get data from a database with pandas, you first need to be able to connect to one. In this exercise, you'll practice creating a database engine to manage connections to a database, data.db. To do this, you'll use sqlalchemy's create_engine() function.

create_engine() needs a string URL to the database. For SQLite databases, that string consists of "sqlite:///", then the database file name.

Instructions 1/2
50 XP
1
Import the create_engine() function from sqlalchemy.

2
Use create_engine() to make a database engine for data.db.
Run the last line of code to show the names of the tables in the database.
'''
SOLUTION

1
# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine

2
# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine('sqlite:///data.db')

# View the tables in the database
print(engine.table_names())