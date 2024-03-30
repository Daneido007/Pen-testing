import subprocess

def execute_command(command, url):
    print("[*] Executing command:", " ".join(command))
    try:
        output = subprocess.check_output(command + [url])
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e)

def main():
    url = input("Enter the URL of the website to check: ")

    # Check for WAF presence using wafw00f
    execute_command(['wafw00f'], url)

    # Perform a basic Nmap scan
    execute_command(['nmap', '-F'], url)

    # Check WordPress vulnerabilities using WPScan
    wpscan_command = [
        'wpscan', 
        '--url', url, 
        '--enumerate', 'vp,vt,tt,cb,dbe,u,m,t', 
        '--plugins-detection', 'aggressive', 
        '--themes-detection', 'aggressive', 
        '--enumerate-vulnerable-themes', 
        '--enumerate-vulnerable-plugins', 
        '--enumerate-t', 
        '--random-user-agent', 
        '--detection-mode', 'aggressive', 
        '--max-threads', '10', 
        '--output', 'wpscan_output.txt'
    ]
    execute_command(wpscan_command, url)

if _name_ == "_main_":
    main()