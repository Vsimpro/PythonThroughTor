import sys, json, socks, socket, requests

def connecTor():
    proxy_port = 9050
    proxy_host = "127.0.0.1"

    pull = requests.get("https://ipv4.wtfismyip.com/json")
    print(f"[{pull.status_code}] from wtfismyip")
    data = json.loads(pull.content)
    yourIP = data['YourFuckingIPAddress']
    
    print("[+] Connecting to TOR")
    try:
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy_host, proxy_port, True)
        socket.socket = socks.socksocket

        pull = requests.get("https://ipv4.wtfismyip.com/json")
        data = json.loads(pull.content)
        print("[IP]: ", data['YourFuckingIPAddress'])
        
        if not yourIP in data['YourFuckingIPAddress']:
            print("[+] Connected to tor.")
            return
        
        else:
            confirm = input("[!] Not connected to tor. Continue? Y/N")
            if confirm.lower() == "y":
                return
            
            sys.exit()

    except Exception as e:
        print("[!] Something went wrong, exiting.")
        sys.exit()


if __name__ == "__main__":
    # Note that Tor.exe must be running
    connecTor() # Call this before running your code. 
