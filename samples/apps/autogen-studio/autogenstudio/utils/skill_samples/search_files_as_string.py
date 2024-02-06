# This skill is used to Search for a file in a Git repository and return its content.
# Args:
#     file_name (str): The name of the file to search for. (add extension)

# Returns:
#     keys:
#     - "filename": The filename of the document.
#     - "content": The content of the page.


# Raises:
#     ValueError: If the file name does not have a valid file extension or contains a path.


import autogens

def search_files_as_string(file_name: str) -> str:
    return str(autogens.search_files(file_name))