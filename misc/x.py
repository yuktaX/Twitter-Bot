def has_replied(file_name, id):
    f_read = open(file_name, 'r')
    lines = f_read.readlines()
    lines = [line[0:len(line) - 1] for line in lines]
    f_read.close()
    #print(lines, id)
    if str(id) in lines:
        return 1
    return 0

def add_id(file_name, id):
    f_write = open(file_name, 'a')
    f_write.write(str(id) + '\n')
    f_write.close()
    return

