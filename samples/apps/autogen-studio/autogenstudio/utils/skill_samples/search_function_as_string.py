# This skill is used to search for a function in codebase and get similar functions
# Args:
#     function_name (str): The name of the function to search for.

# Returns:
#     list[dict]: A list of dictionaries containing the search results. Each dictionary
#     contains the following keys:
#         - "filename": The filename of the document.
#         - "method_name": The name of the method.
#         - "content": The content of the page.

import autogens


def search_function_as_string(function_name: str) -> str:
    return str(autogens.search_function(function_name))