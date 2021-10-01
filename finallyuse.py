def process_file():
    try:
        f=open("c:\\data\\mou.txt")
        x=1/0
    except FileNotFoundError as e:
           print("inside ecxeption")
    finally:
        print("i am cleaning up the file")
        f.close()


process_file()
