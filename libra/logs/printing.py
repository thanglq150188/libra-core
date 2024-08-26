from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Define color print functions
def print_color(
    text: str, 
    color: Fore, # type: ignore
    end = "\n"
):
    print(f"{color}{text}{Style.RESET_ALL}", end=end)