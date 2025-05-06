# 🐱‍💻 Kali Linux Installation Guide (VirtualBox)

This document walks through the installation and setup of **Kali Linux (2025.1c)** in a VirtualBox environment using the official pre-built image.

---

## 📥 Step 1: Download Kali Linux VirtualBox Image

- Go to the [official Kali download page](https://www.kali.org/get-kali/#kali-virtual-machines).
- Or directly download:  
  👉 [`kali-linux-2025.1c-virtualbox-amd64.7z`](https://cdimage.kali.org/kali-2025.1c/kali-linux-2025.1c-virtualbox-amd64.7z)

> ⚠️ This file is compressed in `.7z` format. Use [7-Zip](https://www.7-zip.org/) or another extractor to unpack it.

---

## 🖥️ Step 2: Import into VirtualBox

1. Open **VirtualBox**.
2. Go to `File → Import Appliance`.
3. Select the extracted `.ova` file.
4. Click `Next`, then `Import`.

---

## ⚙️ Step 3: Initial Setup

- Start the VM.
- Default credentials (can change later):
  - Username: `kali`
  - Password: `kali`
- Update packages:
  ```bash
  sudo apt update && sudo apt upgrade
  ```

---

## 🌐 Step 4: Network Configuration

1. Ensure the network adapter is set to `NAT` or `Bridged Adapter` in VirtualBox settings.
2. Inside the VM, verify network connectivity:
   ```bash
   ping google.com
   ```
3. If no connectivity, restart the network service:
   ```bash
   sudo systemctl restart networking
   ```

---

## 🛠️ Step 5: Install Essential Tools

1. Install common tools:
   ```bash
   sudo apt install -y net-tools curl git vim
   ```
2. Install additional penetration testing tools:
   ```bash
   sudo apt install -y metasploit-framework nmap wireshark
   ```

---

## 🔒 Step 6: Secure the Installation

1. Change the default password:
   ```bash
   passwd
   ```
2. Enable the firewall:
   ```bash
   sudo ufw enable
   ```
3. Check firewall status:
   ```bash
   sudo ufw status
   ```

---

## 📄 Step 7: Create a Snapshot

1. In VirtualBox, go to `Machine → Take Snapshot`.
2. Name the snapshot (e.g., `Fresh Install`).
3. Use this snapshot to revert to a clean state if needed.

---

## 🎯 Final Notes

- Always keep the system updated:
  ```bash
  sudo apt update && sudo apt upgrade
  ```
- Refer to the [Kali Documentation](https://www.kali.org/docs/) for advanced configurations.
