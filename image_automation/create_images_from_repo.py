from time import perf_counter


def main():
    # Record the starting time
    start_time = perf_counter()
    ###############################################
    # Main Code goes here
    ###############################################
    # Record the ending time
    end_time = perf_counter()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the elapsed time
    print(f"Elapsed time: {elapsed_time} seconds")


if __name__ == "__main__":
    main()