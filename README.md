# API_SQL_NOSQL
*Here's an API connecting to a SQLSERVER DB and SQLITE DB
SQLServer Database works as a SQL DB and SQLite works as a NOSQL DB
SQLite DB located inside the project, for SQLserver DB open model/customer and modify to your current sql server settings, connect and run SQLQuery.sql for DB creation.
-------------------------------------------------------------------------------------------------------------------------------------------
*Used Model-View-Controller design pattern, this project was build with Python 3.11.3 and installed the following libraries.
-flashapi
-uvicorn
-pyodbc
-sqlite3
-pydantic
-random
-json
-------------------------------------------------------------------------------------------------------------------------------------------
*to run, open a terminal in dir ".../API_SQL_NOSQL" and use uvicorn command "-m uvicorn main:app --reload" to start the server.
-------------------------------------------------------------------------------------------------------------------------------------------
*Documentation located at localhost:"your default port"/docs for tests.
-------------------------------------------------------------------------------------------------------------------------------------------
*Backend is completed and functional. Frontend is not implementated as of now.
-------------------------------------------------------------------------------------------------------------------------------------------
*file named "operacion.py" simulates a use case for this API.
-------------------------------------------------------------------------------------------------------------------------------------------