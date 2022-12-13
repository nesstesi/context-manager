class ContexIterator:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __iter__(self):
        self.line = 0
        return self

    def __next__(self):
        if self.line < len(self.mode):
            self.line += 1
            return self.line
        else:
            raise StopIteration

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ValueError:
            print('error')
        self.file.close()
        return True

if __name__ == '__main__':

    with ContexIterator('namefile.txt', 'r') as file:
        for line in file:
            print(line)

