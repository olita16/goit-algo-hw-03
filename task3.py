from colorama import Fore, Style, init

init(autoreset=True)

def hanoi(n, source, target, auxiliary, state):
    if n == 1:
        disk = state[source].pop()
        state[target].append(disk)
        print(f"{Fore.YELLOW}Перемістити диск з {source} на {target}: {disk}")
        print(f"{Fore.CYAN}Проміжний стан: {state}")
        return

    hanoi(n-1, source, auxiliary, target, state)

    disk = state[source].pop()
    state[target].append(disk)
    print(f"{Fore.GREEN}Перемістити диск з {source} на {target}: {disk}")
    print(f"{Fore.CYAN}Проміжний стан: {state}")

    hanoi(n-1, auxiliary, target, source, state)

def main():
    n = int(input("Введіть кількість дисків: ")) 
    state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}  
    print(f"{Fore.MAGENTA}Початковий стан: {state}")
    hanoi(n, 'A', 'C', 'B', state) 
    print(f"{Fore.MAGENTA}Кінцевий стан: {state}")

if __name__ == "__main__":
    main()
