import os
import subprocess
import sys

VERSION = "1.1.2"

PURPLE = "\033[95m"
RESET = "\033[0m"


def show_help():
    print("Commands:")
    print("  help              Show available commands")
    print("  version           Show BlendTwril version")
    print("  cmd               Open Windows Command Prompt")
    print("  cmd <command>     Run a Windows CMD command")
    print("  python            Open the Python interpreter")
    print("  python <code>     Run Python code")
    print("  exit              Exit BlendTwril")


def main():
    os.system("")

    print(PURPLE + f"BlendTwril {VERSION}" + RESET)
    print(PURPLE + 'Type "help" for commands.' + RESET)
    print()

    while True:
        try:
            command = input(PURPLE + "blendtwirl>>> " + RESET).strip()

            if not command:
                continue

            lower = command.lower()

            if lower == "help":
                show_help()

            elif lower in ("version", "--version"):
                print(PURPLE + f"BlendTwril {VERSION}" + RESET)

            elif lower == "cmd":
                print(PURPLE + "Opening Command Prompt..." + RESET)
                subprocess.Popen(["cmd.exe"])

            elif lower.startswith("cmd "):
                cmd_command = command[4:]
                subprocess.run(cmd_command, shell=True)

            elif lower == "python":
                print(PURPLE + "Opening Python..." + RESET)
                subprocess.Popen([sys.executable])

            elif lower.startswith("python "):
                code = command[7:]
                try:
                    exec(code, {"__name__": "__main__"})
                except Exception as error:
                    print(PURPLE + f"Python error: {error}" + RESET)

            elif lower in ("exit", "quit"):
                print(PURPLE + "Goodbye!" + RESET)
                break

            else:
                print(PURPLE + f"Unknown command: {command}" + RESET)
                print(PURPLE + 'Type "help" for available commands.' + RESET)

        except KeyboardInterrupt:
            print("\n" + PURPLE + "Goodbye!" + RESET)
            break

        except EOFError:
            print("\n" + PURPLE + "Goodbye!" + RESET)
            break


if __name__ == "__main__":
    main()
