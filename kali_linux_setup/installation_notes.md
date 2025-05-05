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
