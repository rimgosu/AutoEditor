import os

def create_directory(directory):
    """
    This function creates a new directory if it does not already exist
    :param directory: the directory path
    """
    # check if the directory exists
    if not os.path.exists(directory):
        # create the directory
        os.makedirs(directory)
        print(f"{directory} has been created.")
    else:
        print(f"{directory} already exists.")

create_directory()