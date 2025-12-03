import sys
import time
import importlib.util
import pathlib
import os

def measure_runtime(module_name, function_name):
    module_path = pathlib.Path(os.path.join(module_name, "main.py"))
    spec = importlib.util.spec_from_file_location("mymodule", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    func = getattr(module, function_name)

    input = module.file_reader("input.txt")

    start_time = time.time()
    func(input)
    end_time = time.time()

    return end_time - start_time

def main():
    module_name = sys.argv[1] if len(sys.argv) == 2 else input("Enter the folder name: ")

    try:
        solver1_runtimes = []
        solver2_runtimes = []

        for _ in range(10):
            solver1_runtimes.append(measure_runtime(module_name, "solver1"))
            solver2_runtimes.append(measure_runtime(module_name, "solver2"))

        avg_solver1 = sum(solver1_runtimes) / len(solver1_runtimes)
        avg_solver2 = sum(solver2_runtimes) / len(solver2_runtimes)

        print(f"Average runtime for Solver 1: {avg_solver1:.6f} seconds")
        print(f"Average runtime for Solver 2: {avg_solver2:.6f} seconds")

    except ModuleNotFoundError:
        print(f"Error: Module {module_name} not found.")
    except AttributeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
