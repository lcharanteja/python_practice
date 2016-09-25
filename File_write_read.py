__author__ = 'charan'


def file_write(string):
    fw = open('sample.txt', 'w')
    fw.write(string)
    fw.write('I like bacon\n')
    fw.close()
def file_read():
    fr = open('sample.txt', 'r')
    text = fr.read()
    print(text)
    fr.close()