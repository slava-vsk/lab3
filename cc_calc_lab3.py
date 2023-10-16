print(" !!! ВІТАЮ !!! Це примітивний калькулятор! "
     "\n...вмію додавати, віднімати, множити, ділити...\n"
       "\n_Для виходу з програми напишить 0_\n"
      "\n_коли запитаю ввести знак оперцїї_\n")
ddod_arg = lambda a, b: a + b
vid_arg = lambda a, b: a - b
mnz_arg = lambda a, b: a * b
dil_arg = lambda a, b: a / b

 

Fl_exit = 0

while Fl_exit != 1:
    if Fl_exit == 0:
        a = float(input("a = "))
        b = float(input("b = "))
        s = input("Дія (+, -, *, /): ")
        if s == '0':
            print(" !!! На все добре !!! ")
            break
        if s in ('+', '-', '*', '/'):
            if s == '+':
                print("%.2f" % dod_arg(a,b))
            elif s == '-':
                print("%.2f" % vid_arg(a,b))
            elif s == '*':
                print("%.2f" % mnz_arg(a,b))
            elif s == '/':
                if b != 0:
                    print("%.2f" % dil_arg(a,b))
                else:
                    print("Ділення на нуль !!!")
    else:
        print("Невірна дія! Введіть + або - або * або /")
