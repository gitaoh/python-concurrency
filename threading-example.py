from threading import Thread
from time import perf_counter


def replace(filename, substr, new_substr):
    print(f"Processing the file {filename}")

    # get the contents of the file
    with open(filename, "r") as file:
        content = file.read()

    # Replace the substr by new_substr
    content = content.replace(substr, new_substr)

    # Write data into the file
    with open(filename, "w") as file:
        file.write(content)


def main():
    filenames = [
        "./temp/test1.txt",
        "./temp/test2.txt",
        "./temp/test3.txt",
        "./temp/test4.txt",
        "./temp/test5.txt",
        "./temp/test6.txt",
        "./temp/test7.txt",
        "./temp/test8.txt",
        "./temp/test9.txt",
        "./temp/test10.txt",
    ]

    # Create Threads
    threads = [Thread(target=replace, args=(filename, "dakia", "ids")) for filename in filenames]
    
    # Start the threads
    for t in threads:
        t.start()
    
    # Wait for the thread to complete
    for t in threads:
        t.join()


    # for filename in filenames:
    #     replace(filename, "ids", "dakia")


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print(f"Duration: {end_time - start_time}(s)")
