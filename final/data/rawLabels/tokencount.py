import tiktoken

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# open and read txt file
with open('data/rawLabels/0.txt', 'r') as file:
    content = file.read()
    print(content)



print(num_tokens_from_string(content, "cl100k_base"))
