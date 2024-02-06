# This skill is used to search for a query in the repository
# Args:
#     search_pattern (str): The search pattern to be used for similarity search.

# Returns:
#     list[dict]: A list of dictionaries containing the search results. Each dictionary
#     contains the following keys:
#         - "filename": The filename of the document.
#         - "method_name": The name of the method.
#         - "content": The content of the page.

import autogens

def search_in_repo_as_string(query: str) -> str:
    return str(autogens.similarity_search(query))