import subprocess
import openpyxl
import time
commands = [
    'lastlog',
    'qwinsta',
    'date +""%Z %z',
    'top -n 1 -b',
    'cat /etc/hosts',
    'wmic os',
    'groups',
    'netstat -anop',
    'reg.exe query HKCU /f password /t REG_SZ /s',
    'cat /etc/crontab',
    'net localgroup',
    'lscpu',
    'ip ro show',
    'arch',
    'net config server',
    'cat /home/*/.bash_history',
    'reg.exe save HKLM\\sam {sam_dump_path},reg.exe save HKLM\\security {security_dump_path},reg.exe save HKLM\\system {system_dump_path},%temp%\\security,%temp%\\system',
    'ip addr show',
    'wmic startup',
    'route -n',
    'iptables -t nat -L -n -v',
    'netsh firewall show state',
    'df -k',
    'wmic share get /ALL',
    'net accounts',
    'wmic path win32_logicaldisk get caption,filesystem,freespace,size,volumename',
    #'tree',
    'whoami',
    'powershell -ExecutionPolicy Bypass -Command ""Get-EventLog security -instanceid 4625',
    'uptime',
    'cat /etc/inittab',
    'perl -v',
    'netstat -nltupw',
    'file /bin/pwd',
    'mount',
    'powershell -ExecutionPolicy Bypass -Command ""Get-EventLog security -instanceid 4624',
    'systemctl',
    'wmic bios',
    'locale -k LC_TIME',
    'crontab -l',
    'where /R {root_directory} *.pst',
    'ls /usr/sbin/setenforce',
    'ps aux',
    'cat /etc/passwd',
    'ifconfig -a',
    'dmesg',
    'net session',
    'ip6tables -L -n -v',
    'ls -la /',
    'wmic qfe get hotfixid',
    'find /proc/net/* -maxdepth 0 -type f -exec cat {} +',
    'arp -a',
    'cat /etc/issue',
    'cat /etc/resolv.conf',
    'cat /etc/sudoers',
    'history',
    'lsscsi',
    'hostname -f',
    'locale',
    'cat /proc/meminfo',
    'nltest.exe /domain_trusts 1> nul',
    'net user',
    'lshw',
    'cut -d: -f1 /etc/passwd',
    'netstat -r',
    'lspci',
    'uname -a',
    'net share',
    'chage -l',
    'service --status-all',
    'ipconfig /all',
    'net group "domain admins" /domain',
    'cat /etc/shadow',
    'who -a',
    'cat /tmp/krb5cc_*',
    'uname -m',
    'net time \\\\localhost',
    'route print'
]


def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode().strip()
    except subprocess.CalledProcessError as e:
        return f"Error executing command '{command}': {e.output.decode().strip()}"

def write_to_excel(outputs):
    wb = openpyxl.Workbook()
    ws = wb.active
    for command, output in outputs.items():
        ws.append([command])
        ws.append([output])
    wb.save(r"C:\Users\danz\Desktop\output1.xlsx")

def main():
    outputs = {}
    for command in commands:
        output = execute_command(command)
        outputs[command] = output
        if "Error executing command" in output:
            print(output)
            print("--------------------------------------------------------")
        else:
            print(f"Endpoint is affected by command '{command}'")
            print(output)
            write_to_excel(outputs)
    

if _name_ == "_main_":
    main()
    print('finished')
