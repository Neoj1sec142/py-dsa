from collections import deque

def search(lines, pattern, history=5):
    '''Searches for the 5 previous lines
    from the search qeury'''
    prev_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prev_lines
        prev_lines.append(line)
        
def main():
    print("Welcome to the file searcher")
    query = input("Enter the string you are searching for: ")
    file_path = input("Enter the path of the file you are searching: ")
    if query and file_path:
        with open(file_path, 'r') as f:
            for line, prevlines, in search(f, query, 5):
                for pline in prevlines:
                    print(pline, end='')
                    print('-'*20)

if __name__ == '__main__':
    main()
    