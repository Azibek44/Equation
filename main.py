import re
import sympy as sp

def parse_and_equation(equation_str):
    match = re.match(r'\(([^+]+)\^2\s*\+\s*([^=]+)\s*=\s*([^)]+)\)', equation_str)

    if not match:
        print("Неверный формат уравнения. Пожалуйста, введите уравнение вида (x^2 + y = z).")
        return None

    x_squared, y_coefficient, constant = map(sp.sympify, match.groups())
    equation = sp.Eq(x_squared + y_coefficient, constant)
    solution = sp.solve(equation, dict=True)
    return solution

if __name__ == "__main__":
    equation_str = input("Введите уравнение вида (x^2 + y = z): ")
    result = parse_and_equation(equation_str)

    if result is not None:
        print("Решение уравнения:", result)
    else:
        print("Уравнение не решено. Проверьте введенные данные.")
