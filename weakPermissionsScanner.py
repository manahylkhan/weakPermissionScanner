import os
import subprocess

def find_suid_binaries():
    print("[+] Checking for SUID Binaries...")
    suid_binaries = subprocess.getoutput('find / -perm -4000 -type f 2>/dev/null').split('\n')
    if suid_binaries:
        print(f"Found {len(suid_binaries)} SUID binaries:")
        for binary in suid_binaries:
            print(f" - {binary}")
    else:
        print("No SUID binaries found.")
    print("\n")

def check_sudo_permissions():
    print("[+] Checking for Weak Sudo Permissions...")
    try:
        sudo_result = subprocess.getoutput('sudo -l')
        if 'NOPASSWD' in sudo_result or '(ALL)' in sudo_result:
            print("Potentially weak sudo permissions detected:\n")
            print(sudo_result)
        else:
            print("No weak sudo permissions detected.")
    except Exception as e:
        print(f"Error checking sudo permissions: {e}")
    print("\n")

def find_world_writable_services():
    print("[+] Checking for World-Writable systemd Service Files...")
    services = subprocess.getoutput('find /etc/systemd/system /lib/systemd/system -type f -perm -o+w 2>/dev/null').split('\n')
    if services and services[0]:
        print(f"Found {len(services)} world-writable services:")
        for service in services:
            print(f" - {service}")
    else:
        print("No world-writable service files found.")
    print("\n")

if __name__ == "__main__":
    print("=== Linux Weak Permissions Scanner ===\n")
    find_suid_binaries()
    check_sudo_permissions()
    find_world_writable_services()
