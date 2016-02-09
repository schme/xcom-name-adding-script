import sys

def usage():
    print("Usage: {0} [xcom_file] [wordlist]".format( sys.argv[0]))

def main(argv):
    if( len(argv) < 2):
        usage()
        sys.exit(0)

    # Last + 1, aka where we start adding from. These are the defaults found
    # at this time
    firstOpWord = 33
    secondOpWord = 49
    firstOpName = 113
    secondOpName = 127

    xcom_list = argv[0]
    word_list = argv[1]

    with open(xcom_list, 'a') as xcom, open(word_list, 'r') as words:
        for line in words.readlines():
            xcom.write( "m_aFirstOpWord[{0}]={1}".format(firstOpWord, line))
            xcom.write( "m_aSecondOpWord[{0}]={1}".format(secondOpWord, line))
            xcom.write( "m_aFirstOpName[{0}]={1}".format(firstOpName, line))
            xcom.write( "m_aSecondOpName[{0}]={1}".format(secondOpName, line))

            firstOpWord += 1
            secondOpWord += 1
            firstOpName += 1
            secondOpName += 1

if __name__ == '__main__':
    main( sys.argv[1:])
