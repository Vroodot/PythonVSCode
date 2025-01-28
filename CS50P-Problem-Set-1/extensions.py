    # extension.py

"""
(https://cs50.harvard.edu/python/2022/psets/1/extensions/)

Spec:
Prompt user for the name of a file
Convert file extension suffixes (.gif, .jpg, etc) into a media type regardless of case
Use (developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)
    to define the common types
For example, if given 'cat.gif' the output should be image/gif
"""
# Since endwith() returns a bool, I think its best solve this with if/elif chain
# We'll put what we think our most common input types will be uptop, 
# that way we have a greater chance of escaping the function early.


# 1st - Get the file name from the user
# Remove any excess whitespace and transfer it to lowercase to make it easier for our script to handle
file_name = input("File Name: ").lower().strip()

# image/
# Use | for "or" since both would return /jpeg
if file_name.endswith(".jpg") | file_name.endswith(".jpeg"):
    print("images/jpeg")
elif file_name.endswith(".png"):
    print("images/png")
elif file_name.endswith(".gif"):
    print("images/gif")
# text/
elif file_name.endswith(".txt"):
    print("text/plain")
# application/
elif file_name.endswith(".pdf"):
    print("application/pdf")
elif file_name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")