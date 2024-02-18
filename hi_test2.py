import subprocess

# Command and arguments
command = "./TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llama"
args = ["--server", "--nobrowser", "--port", "8084"]

# Combine command and arguments
cmd = [command] + args

# Run the command as a subprocess
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Wait for the process to complete and get output and errors
stdout, stderr = process.communicate()

# Print output and errors
print("Output:", stdout)
print("Errors:", stderr)

# Check process status
if process.returncode == 0:
    print("Process completed successfully")
else:
    print("Process failed with return code", process.returncode)
