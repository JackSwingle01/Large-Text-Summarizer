from completions import get_summary

filename = './data/data.txt'


def save_chunk_summary_to_file(summary: str, filename: str = filename):
    # append a chunk to the end of the file
    file = open(filename, "a")
    file.write(summary)
    file.close()

    return


def clear_file(filename: str = filename):
    # clear the file
    file = open(filename, "w")
    file.close()

    return


def read_file(filename: str = filename):
    # read the entire file into a string and return it
    file = open(filename, "r")
    string = file.read()
    file.close()

    return string


def split_string_to_chunks(string: str, chunk_size: int = 2096):
    # split string to chunks and return it as a list of strings of size chunk_size
    chunks = [string[i:i + chunk_size] for i in range(0, len(string), chunk_size)]

    return chunks


def summarize_long_text(text: str, max_size: int = 1000):
    while (len(text) >= max_size):
        clear_file()
        # take a long piece of text and split it into chunks
        chunks = split_string_to_chunks(text)
        # save the chunks summaries to a file
        for chunk in chunks:
            summary = get_summary(chunk)
            save_chunk_summary_to_file(summary)
        text = read_file()
        # once all of the chunks have been summarized, read the file check if it is below the max size
        # if it is, then return the text
        # if it is not, then clear the file and repeat the process
    return text
