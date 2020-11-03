# imports go here
import parser
import time


def main():
   """Main entry"""
   pass


if __name__ == '__main__':
   main()

start = time.time()
theFile = parser.FileManager("example.txt")
theFile.showresult()
end = time.time()
print(f"The total time to execute the program was {end-start}")