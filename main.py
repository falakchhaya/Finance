# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import FFinance

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('how are, khana kha ke jaana')  # reference, Khichadi
    print("main funcion: {}".format(__name__))

    import FFinance
    from FFinance.fetch_data import fetch_data
    fetch_data.get_data()





