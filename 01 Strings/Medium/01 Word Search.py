from time_decorator import complexity_profiler

def search_char(board, word):
    if word == "":
        return True
    

@complexity_profiler
def word_search(board, word):
    n = len(board)

    return True

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
word_search(board, word)