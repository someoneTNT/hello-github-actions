import sys


def main(argv):
    if argv.__len__()<2:
        return
    else: 
        print(argv[1]) 

if __name__ == "__main__":
    main(sys.argv)