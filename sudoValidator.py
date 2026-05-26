import subprocess
import sys

def run_and_get_exit_code():
    # The command requested
    command = "sudo echo $?"
    
    try:
        # Run the command. 
        # shell=True is required to interpret the shell variable '$?'
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        
        # The exit code of the 'sudo echo $?' command itself
        exit_code = result.returncode

        #print(exit_code)  # Print the exit code to stdout for the caller to capture
        return exit_code

    except Exception as e:
        print(f"An error occurred while executing the command: {e}")
        return 1

if __name__ == "__main__":

    final_code = run_and_get_exit_code()
    sys.exit(final_code)