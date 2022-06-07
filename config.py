# Enable debug mode.
DEBUG = True

# Connect to the database

# i dont know how to findmy username and password

class DatabaseURI:

    # Just change the names of your database and crendtials and all to connect to your local system
    DATABASE_NAME = "movies"
    SQLALCHEMY_DATABASE_URI = "postgresql:///{}".format(
        DATABASE_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
