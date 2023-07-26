from time_window_constructors.time_window_constructor import TimeWindowConstructor




if __name__ == "__main__":

    test_window = TimeWindowConstructor(sequence_length = 10)
    print(test_window._sequence_length)