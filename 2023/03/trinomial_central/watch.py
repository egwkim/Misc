import os
import platform
import subprocess
import threading
import time
from typing import Callable


def clear():
    """Clear output."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def proc_callback(proc: subprocess.Popen, func: Callable):
    """Execute function when the process exits successfully.

    Args:
        proc (subprocess.Popen)

        func (Callable)

    Returns:
        (Any | Literal[False]):
        Returns the return of the function.
        If the process returns an error code, return False.
    """
    if proc.wait() == 0:
        return func()
    return False


def input_new_line(proc: subprocess.Popen, interval: float = 1):
    """Create a thread that inputs a new line to the process.

    Args:
        proc (subprocess.Popen): Process to input new line.

        interval (float, optional): Input interval in seconds. Should be equal to or greater than 1. Defaults to 1.
    """
    while proc.poll() == None:
        os.write(proc.stdin.fileno(), b"\n")
        time.sleep(interval)


def watch(file, command, interval: float = 1, on_exit: Callable | None = None):
    prev_stamp = 0
    stamp = os.stat(file).st_mtime
    p = None

    while True:
        # If the file is updated, create a subprocess
        # If one exists, kill it and create a new one
        if prev_stamp != stamp:
            prev_stamp = stamp
            clear()
            if p != None and p.poll() == None:
                p.terminate()
                p.wait()
            p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)

            # Print message after slide is generated
            threading.Thread(target=proc_callback, args=(p, on_exit)).start()
            # Input new line to avoid getting stuck
            threading.Thread(target=input_new_line, args=(p, 1)).start()

        time.sleep(interval)

        # Update stamp to check if the file is modified
        stamp = os.stat(file).st_mtime


def main():
    # TODO Add arg parser to set scenes
    # or input keys to change scenes
    
    #scenes = "Intro Polynomial ComplexTrigonometry ValueToCoeff Integral Outro"
    scenes = "ComplexTrigonometry"
    output = "slides.html"
    verbosity = "info"
    command = (
        f"manim -ql -v {verbosity} --progress_bar display slides.py {scenes} && "
        f"manim-slides convert {scenes} {output}"
    )

    def success_message():
        print("Slide generation completed!")
        print(f"file://{os.path.abspath(output)}")

    watch("slides.py", command, interval=5, on_exit=success_message)


if __name__ == "__main__":
    main()
