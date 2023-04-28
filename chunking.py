from os import path
from completions import get_summary

# filename = './data/data.txt'


def save_to_file(text: str, filename: str):
    # append a chunk to the end of the file
    file = open(filename, "a")
    file.write(text)
    file.close()

    return


def clear_file(filename: str):
    # clear the file
    file = open(filename, "w")
    file.close()

    return


def read_file(filename: str):
    # read the entire file into a string and return it
    file = open(filename, "r")
    string = file.read()
    file.close()

    return string


def token_to_char_count(token_count):
    return token_count * 4


MAX_TOKENS = 2096
MAX_CHARS = token_to_char_count(MAX_TOKENS)


def split_string_to_chunks(string: str, chunk_size: int = MAX_CHARS):
    # split string to chunks and return it as a list of strings of size chunk_size
    chunks = [string[i:i + chunk_size]
              for i in range(0, len(string), chunk_size)]

    return chunks

def file_is_empty(filename: str):
    #check if the file exists
    if not path.exists(filename):
        return True

    # check if the file is empty
    file = open(filename, "r")
    string = file.read()
    file.close()

    return string == ""



def summarize_long_text(text: str, max_summary_size: int = 2000):

    summary_version = 0
    filename = f"./data/original.txt"
    clear_file(filename)
    save_to_file(text, filename)

    while (len(text) >= max_summary_size):
        summary_version += 1
        filename = f"./data/summary_{summary_version}.txt"

        # take a long piece of text and split it into chunks
        chunks = split_string_to_chunks(text)
        
        print(f"Summary no. {summary_version}:\nNumber of chunks: {len(chunks)}")

        # clear the file
        if not file_is_empty(filename):
            clear_file(filename=filename)

        # save the chunks summaries to a file
        for chunk in chunks:
            print(f"Summarizing chunk number {chunks.index(chunk) + 1}...")
            summary = get_summary(chunk)
            save_to_file(summary, filename)

        text = read_file(filename)
        # once all of the chunks have been summarized, read the file check if it is below the max size
        # if it is, then return the text
        # if it is not, then clear the file and repeat the process
    return text
