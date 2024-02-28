import subprocess

def execute_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return None, e.stderr

# import fterminal
# print(fterminal.execute_command(["ping", "google.com"]))