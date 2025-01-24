---
title: "Lightweight Networking VM on MacOS"
date: 2025-01-20
description: "Set up a lightweight VM with networking toolsusing OrbStack on MacOS"
---

Set up a lightweight VM using OrbStack to use for CSE 150 labs

- Works on **Apple Silicon** (M1...2...)
- no **UTM**/**Multipass** needed
- done in about ~10m
- <2GB storage, quick launch

## Install XQuartz and OrbStack

- Install XQuartz (GUI): [xquartz.org](https://www.xquartz.org/)
- Install OrbStack (VM): [orbstack.dev](https://orbstack.dev)

## Create the OrbStack Instance

Shown in the thumbnail above

## Connect to the Instance

Either `ssh mininet@orb` from a terminal or double-click **mininet** in OrbStack

## Installation

Inside the VM, run this:

**Note**: Please select yes on purple screen prompt

```bash
sudo apt install openssh-server xauth x11-apps
sudo apt install mininet openvswitch-testcontroller traceroute wireshark -y
sudo apt install chromium firefox ncsd -y
sudo usermod -aG wireshark $(whoami)
```

**What is this doing?**

- `openssh-server`: Enables remote SSH access
- `xauth`: Manages X11 forwarding authentication
- `x11-apps`: Provides basic X11 GUI tools
- `mininet`: Simulates virtual networks
- `openvswitch-testcontroller`: OpenFlow controller for Mininet
- `wireshark`: Captures and analyzes network traffic
- `chromium`: Install chromium browser
- `firefox`: Install firefox browser
- `ncsd`: Grants chrome access to the internet
- `usermod ...`: Grants user permissions to capture packets

## GUI Setup

Still in the VM, run this:

```bash
sudo vim /etc/ssh/sshd_config
```

This brings up config, find and ensure these lines are set like this:

helpful: `i` to edit, `:wq` to save + exit, `:q!` to force quit without save if you mess up

```plaintext
X11Forwarding yes
X11DisplayOffset 10
X11UseLocalhost yes
```

Now saved, let's reload:

```bash
sudo systemctl restart ssh
```

Let's set a password (anything is fine, just remember it):

```bash
sudo passwd $USER
```

Let's also allow Chrome to use the GUI:

```
echo 'export XAUTHORITY=$HOME/.Xauthority' >> $HOME/.profile
```

## Connect to the VM with GUI

Pretty much done atp, let's connect!

**Important**: Close the VM's terminal tab, and open a new one (MacOS, not VM)

### **Quick Option**

Connect with X11 (`-X`) forwarding):

```bash
ssh -X mininet.orb.local
```

### **Better Option**

1. Edit SSH config:

```bash
vim ~/.ssh/config
```

2. Add (make sure to add your username):

```
Host mininet
    HostName mininet.orb.local
    User <your-username>
    ForwardX11 yes
```

3. Connect!

```bash
ssh mininet
```

## Doing Labs

### **Run Commands**

Run wireshark (in background):

```bash
wireshark &
```

Run browser (in background):

```bash
# FF seems to run faster
# but included both since
# that's what the lab docs use

chromium &
# or
firefox &
```

Run mininet scripts:

```bash
sudo python3 <script_name>.py
```

Also if you re-run mininet script and get an error, try wiping env:

```
sudo mininet -c
```

### **Edit Python Files in VSCode**

Below stuff is optional, it's just to edit stuff in VSCode

1. Install [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh).
2. Open VSCode, click TV icon on left sidebar **or** bottom & left-most icon
   1. Connect to Host
   2. Add New SSH Host
   3. `ssh mininet@orb`
3. Cmd+Shift+P, type in "Install code PATH" and enter
4. Now just open up a fresh terminal
5. Do as you please, use `code <filepath>` to open stuff in VSCode
