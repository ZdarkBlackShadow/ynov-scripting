from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect('192.168.122.195', username='adrien', password='password')

stdin, stdout, stderr = client.exec_command('ls')

output = stdout.read().decode('utf-8')
error = stderr.read().decode('utf-8')

if output:
    print("Output:", output)
if error:
    print("Error:", error)

client.close()
