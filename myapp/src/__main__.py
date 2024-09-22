import os
from libs.library1.main import some_function
from libs.library2.main import another_function

def main():
    print(another_function())
    print(some_function())
    print(os.getcwd())

if __name__ == "__main__":
    main()
    
