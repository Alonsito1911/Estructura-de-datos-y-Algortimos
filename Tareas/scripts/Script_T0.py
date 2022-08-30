import os
import filecmp
from pathlib import Path


def simple_compare(file1: str, file2: str) -> bool:
    return filecmp.cmp(file1, file2, shallow=False)


def specific_compare(file1: list, file2: list) -> None:
    i = 0
    with open("diff.txt", "w") as file:
        for line1 in file1:
            i += 1
            for line2 in file2:
                if line1 == line2:
                    file.write(f"Line {i}: IDENTICAL\n")
                else:
                    file.write(f"Line {i}:\n")
                    file.write(f"\tFile 1: {line1}")
                    file.write(f"\tFile 2: {line2}")
                break


def read_file(filename) -> list:
    with open(filename, "r") as file:
        return file.readlines()


def check_output(input: str, student_output: str, correct_output: str, report: bool) -> bool:
    if simple_compare(student_output, correct_output):
        print(f"{input} - CORRECT")
    else:
        print(f"{input} - WRONG OUTPUT")
        if report:
            print("Generating diff.txt")
            specific_compare(read_file(student_output), read_file(correct_output))
            return False
    return True


if __name__ == '__main__':
    # PARAMETROS A MODIFICAR
    PATH_GENERAL_TEST = "T0"  # RUTA A LA CARPETA CONTENEDORA DE LOS TESTS
    EXECUTABLE = "dccomics"  # NOMBRE DEL EJECUTABLE
    # Poner en True si se quiere que el script se detenga en el primer error y genere un reporte
    REPORT = False

    # NO MODIFICAR
    path_solutions = os.path.join(PATH_GENERAL_TEST, "solutions")  # EJ: "T0/solutions"
    path_inputs = os.path.join(PATH_GENERAL_TEST, "tests")
    path_output = "output.txt"
    lista_sol = []
    lista_input = []
    for archivo in Path(path_solutions).glob("**/*.txt"):
        lista_sol.append(archivo)
    for archivo in Path(path_inputs).glob("**/*.txt"):
        lista_input.append(archivo)

    for i, path_input in enumerate(lista_input):
        os.system(f"./{EXECUTABLE} {path_input} {path_output}")
        result = check_output(path_input, path_output, lista_sol[i], REPORT)
        if not result:
            break
