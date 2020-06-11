import sys

print('sys.argv', sys.argv)
def count_lines(name):
    f = open(name, 'r')
    lines_count = len(f.readlines())
    f.close()
    return lines_count
    
def count_chars(name):
    f = open(name, 'r')
    char_count = len(f.read())
    f.close()
    return char_count

def test(name):
    print('Lines: {} '.format(count_lines(name)))
    print('Characters: {} '.format(count_chars(name)))


if __name__ == '__main__':
    print('Using sys.argv')
    test(sys.argv[1])


    
