import sys

class error:
    pass

def get_file_contents(filename):
    try:
        f = open(filename, 'r')
    except: 
        return error 

    contents = f.read()
    f.close()

    return contents 

def replace_all_files(files, change_this, to_this):
    for dat in files:
        if dat == 'change_this' or dat == 'to_this' or dat == sys.argv[0]:
            continue

        try:
            f = open(dat, 'r');
            print "Replacing in " + dat + "\n"
            contents = f.read()
            f.close()

            contents = contents.replace(change_this, to_this)

            f = open(dat, 'w')
            f.write(contents)
            f.close()
        except:
            print "Can not open '" + dat + "', skipping..."

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "No files to change specified, exiting..."
        sys.exit()

    # The default filename for the ct and tt file
    ct_filename = 'change_this'
    tt_filename = 'to_this'

    change_this = get_file_contents(ct_filename)
    if change_this == error:
        print "No change_this file specified, exiting..."
        sys.exit()

    to_this = get_file_contents(tt_filename)
    if to_this == error:
        print "No to_this file specified, exiting..."
        sys.exit()

    if sys.argv[1] == '-r':
        pass
    else:
        files = sys.argv[1:]
        replace_all_files(files, change_this, to_this)
