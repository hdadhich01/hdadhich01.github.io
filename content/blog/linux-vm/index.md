---
title: "Lightweight Linux VM + GUI on MacOS"
date: 2025-01-20
description: "Set up a fast + light Linux VM using OrbStack with GUI on MacOS"
---

Fed up with clunky **Multipass**, **UTM**, or **VirtualBox** setups for school/work?

Let's get set up in minutes with a much faster, lighter alternative!

- Works on **Apple Silicon** (M1...)
  - emulate both `arm` and `x86_64` arch
- copy/paste between Mac and VM
- setup in <5m, instant bootup

{{< alert >}}
Looking for a <b>CSE 13S/101/130/150</b> setup guide? Do [prereqs](#prerequisites) and skip to [here](#ucsc-class-labs-setup)
{{< /alert >}}

## Prequisites

Very simple, caveman clicks button and installs:

- Install XQuartz (GUI): [xquartz.org](https://www.xquartz.org/)
- Install OrbStack (VM): [orbstack.dev](https://orbstack.dev)
- Visual Studio Code
  - Install [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

Please drag to `/Applications` folder

## Create the OrbStack Instance

![ubuntu](ubuntu.png)

## Connect to the Instance

Either `ssh mininet@orb` from a terminal or double-click **mininet** in OrbStack

## Installation

Inside the VM, run this:

**Note**: Please select yes on purple screen prompt

```bash
sudo apt install -y openssh-server xauth x11-apps nscd
```

**What is this doing?**

- `openssh-server`: Enables remote SSH access
- `xauth`: Manages X11 forwarding auth
- `x11-apps`: Provides basic X11 GUI tools
- `nscd`: Grants browsers access to the internet

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

Let's also allow browsers to use the GUI:

```
echo 'export XAUTHORITY=$HOME/.Xauthority' >> $HOME/.profile
```

## Connect to the VM with GUI

**Important**: Make sure you're doing this inside a MacOS terminal, not VM

Connect with X11 (`-X`) forwarding:

```bash
ssh -X mininet.orb.local
```

## GUI Usage

Now that you're `ssh -X`'d into the VM, you can run GUI apps!

Run apps (in background):

```bash
app &
```

Replace `app` with the app you want to run, e.g. `wireshark`, `firefox`, `code`, etc.

Also note, bidirectional clipboard is supported!

- <kbd>Command</kbd> + <kbd>C</kbd> to copy on MacOS
- <kbd>Ctrl</kbd> + <kbd>V</kbd> to paste on GUI
- and vice versa

### **Code in VSCode**

Below stuff is optional, it's just to edit stuff in VSCode

1. Install [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
2. Install [Remote X11](https://marketplace.visualstudio.com/items?itemName=spadin.remote-x11-ssh)
3. Open VSCode, click TV icon on left sidebar **or** bottom & left-most icon

#### Default VM

If you only have 1 VM, it should already show up as `orb`, just click it and you're in

#### Multiple VMs

If you have multiple, for the default just connect to `orb`, but for another do:

1.  Connect to Host
2.  Add New SSH Host
3.  `ssh vmname@orb`
4.  <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>, type in "**Install code PATH**" and enter
5.  Now just open up a fresh terminal
6.  Do as you please, use `code <filepath>` to open stuff in VSCode

#### with GUI

Now sometimes, you want to avoid having a seperate terminal, and separate VSCode

- Why?
  - The seperate terminal is where you `ssh -X ...`
    - this means **GUI enabled**
  - VSCode's connection is just a regular `ssh ...`

So let's just replace **#3** above with `ssh -X vmname.orb.local`

Only caveat is you have to input your password every time you open VSCode

## UCSC Classes Setup

Many lab assignments require a VM setup, let's get set up quickly

### CSE 13S, 101, 130

Doesn't require a GUI, so set up like done [here](#create-the-orbstack-instance) (default settings are fine)

Simply `ssh orb`, then run the following:

```bash
sudo apt install clang clang-format clang-tools make net-tools valgrind
```

Now let's set up SSH to allow access to [git.ucsc.edu](https://git.ucsc.edu)

```bash
ssh-keygen -t rsa -b 4096 -C "OrbStack" -N ""
```

Add the key to ssh agent:

```bash
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
```

Now add the output of below to **Preferences > SSH Keys > Add new key** on [git.ucsc.edu](https://git.ucsc.edu)

```bash
cat ~/.ssh/id_rsa.pub
```

Now you're done, you should see `orb` in your SSH hosts on VSCode

Simply connect, and install these to make your life easier:

- [C/C++ Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools-extension-pack) Syntax highliting
- [Clang-Format](https://marketplace.visualstudio.com/items?itemName=xaver.clang-format)
  - <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> and type in "**Format Document With**"
  - **Configure Default Formatter** > Set to **clang-format**
- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)

### CSE 150

The labs for this class require a GUI for wireshark + browser. Since it's a lot of install steps, here's a [cloud-init](https://cloudinit.readthedocs.io/en/latest/) script I made to speed it up:

{{< button href="https://gist.github.com/hdadhich01/5dd1e00b79f1611b3a79337395d493d8" target="_blank" >}}
Setup Script
{{< /button >}}

- Click **Raw** and then <kbd>Command</kbd> + <kbd>S</kbd>
- Save as `cloud-init.yml` under `~/Desktop` (make sure to add the `.yml`)

Once done, open up a terminal and run:

```bash
cd ~/Desktop
orb create -a amd64 -c cloud-init.yml ubuntu:focal mininet
```

What's happening here?

- `orb create`: Creates a new instance
- `-a amd64`: Specifies the architecture (arm64 or amd64 for x86-64)
  - **Why not latest?** The labs seem to x86 arch, so I'm matching it
- `-c cloud-init.yml`: Specifies the cloud-init file to use
- `ubuntu:focal`: Specifies the Ubuntu version (focal for 20.04)
  - **Why not latest?** The labs seem to use 20.04 (as of W25), so I'm matching it
- `mininet`: Specifies the name of the instance

It'll take <5m to install, then SSH into it:

```bash
ssh mininet@orb
```

We need to change the password to `ssh -X` into it later:

```bash
sudo passwd $USER
```

Almost done, just need to install wireshark:

```
sudo apt install -y wireshark
```

Select **yes** on **purple screen prompt** with left arrow key + enter

Almost there, just need to adjust perms and clone the POX controller:

```bash
sudo usermod -aG wireshark $(whoami)
git clone https://github.com/noxrepo/pox.git
chmod +x ~/pox/pox.py
```

All done, now connect using the instructions [here](#connect-to-the-vm-with-gui)

And also, read entirely through [GUI Usage](#gui-usage)

#### FAQ

- Note that instead of `chromium`, this script uses `firefox` for the browser

  - doesn't make a difference, it's just faster

- For OpenFlow labs, use this filter in Wireshark:

```
openflow_v1
```

- Sometimes your POX controller might be already binded to a port on a re-reun:

```
sudo kill -9 $(sudo lsof -ti :6633)
```
