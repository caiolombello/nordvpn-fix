# Linux NordVPN Fix
I was getting a problem with NordVPN script, with the following message error: 

> <span style="color:red">Whoops! Connection failed. Please try again. If the problem persists, contact our customer support.</span>.

So, for solution i was need to use OpenVPN, following the [install script](https://github.com/caiolombello/nordvpn-fix/blob/main/install) i've created following this [NordVPN Article](https://support.nordvpn.com/Connectivity/Linux/1047409422/How-can-I-connect-to-NordVPN-using-Linux-Terminal.htm). And for find the best server to connect, i've made a [Python Web Scraping script](https://github.com/caiolombello/nordvpn-fix/blob/main/recommended.py) tooking the recommended server from NordVPN.

Using the OpenVPN without this script i've made, i would have to search for the best server to connect at [Server recommended by NordVPN](https://nordvpn.com/pt-br/servers/tools/), later, search for the .ovpn path file and go to [Nord Account](https://my.nordaccount.com/pt-br/dashboard/nordvpn/) take my Username and Password to Auth.

## Instructions

With this script just need follow this instructions:

### Step 1: Clone the repository
```bash
git clone https://github.com/caiolombello/nordvpn-fix.git
```

### Step 2: Go to repository folder, execute the install script and follow the instructions
```bash
cd nordvpn-fix
```
```bash
sudo ./install
```
### Step 3: Connect to VPN
```bash
vpn
```