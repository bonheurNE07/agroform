import mysql.connector as connector

def createDb(db_name:str = None) -> None:
    """
    Create a MySQL database with the provided name.

    Args:
        db_name (str): The name of the database to be created.

    Returns:
        None

    This function connects to a MySQL server and creates a new database
    with the given name. It handles exceptions and ensures proper resource
    management by closing the database connection.

    Example:
        createDb("my_new_database")
    """
    if db_name is not None and isinstance(db_name, str):
        try:
            # create the db
            # create the connector
            connection = connector.connect(
                host ="localhost",
                user = "root",
                password= "bonheurBNE37",
                port= "3306"
            ) 

            # create the cursor to the conection
            cursor = connection.cursor()

            # execute the statement tto create the db
            cursor.execute(f"CREATE DATABASE {db_name};")

            print(f"{db_name} CREATED SUCCEFULLY !")
        except connector.Error as error:
            print(f"There is an error : \n{error}")
        finally:
            if connection.is_connected():
                # Close cursor and connection
                cursor.close()
                connection.close()

                print(f"Database connection Closed {db_name}")

    else:
        print(f"Enter a valid DB name :{db_name}")
        raise TypeError("Enter a valid DB name.")
        
         
createDb("form_db")