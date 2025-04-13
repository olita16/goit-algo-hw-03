from colorama import init, Fore, Style
import turtle

init(autoreset=True)

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def main():
    print(Fore.CYAN + Style.BRIGHT + "🎨 Програма малює сніжинку Коха!")
    try:
        level = int(input(Fore.YELLOW + "🔢 Введіть рівень рекурсії для сніжинки Коха: "))
    except ValueError:
        print(Fore.RED + "❌ Будь ласка, введіть ціле число.")
        return

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    length = 300
    koch_snowflake(t, length, level)

    print(Fore.GREEN + "✅ Сніжинка намальована. Закрийте вікно після перегляду.")
    window.mainloop()

if __name__ == "__main__":
    main()
