import pysftp

# Replace these with your SFTP server details
hostname = '127.0.0.1'
username = 'Service'
password = 'T@R63dis.'

# Connect to the SFTP server
with pysftp.Connection(hostname, username=username, password=password) as sftp:
    # List the files in the remote directory
    remote_directory = 'configuration'
    files = sftp.listdir(remote_directory)
    print("Files in remote directory:")
    for file in files:
        print(file)

    # Download a file from the remote server
    remote_file_path = "configuration\config"
    local_file_path = "F:\new\config"
    sftp.get(remote_file_path, local_file_path)
    print(f"Downloaded {remote_file_path} to {local_file_path}")

    # Upload a file to the remote server
    # local_file_path = 'local_file.txt'
    # remote_file_path = '/path/to/remote/uploaded_file.txt'
    # sftp.put(local_file_path, remote_file_path)
    # print(f"Uploaded {local_file_path} to {remote_file_path}")