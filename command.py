import subprocess
import sys

def universal_launcher(command):
    try:
        # Execute the provided 'command' with shell=True, allowing the execution of various OS commands.
        # There's no need to list arguments; a single line of any complexity of commands will work.
        output = subprocess.run(command, shell=True, capture_output=True)

        # Decode the byte output to a string for readability.
        output_text = output.stdout.decode()

        # Check the return code to determine whether the command was successful (0) or if there was an error (non-zero).
        if output.returncode == 0:
            return output_text
        else:
            # If there was an error, capture and decode the error message from stderr.
            return output.stderr.decode()

    except:
        # If anything goes wrong, exit the program with an error code.
        sys.exit(1)

def main():
    # Prompt the user for a command, execute it, and print the output or error message.
    print(universal_launcher(input("command: ")))

    # Exit the program with a success code after everything goes well.
    sys.exit(0)

if __name__ == "__main__":
    main()

