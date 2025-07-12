# 🕵️‍♂️ Clickjacking Vulnerability Scanner

This is a simple tool that helps you detect **Clickjacking vulnerabilities** in websites. It checks whether the target site allows itself to be embedded in an `<iframe>` and whether it uses secure headers like `X-Frame-Options` or `Content-Security-Policy (CSP)`.

## 🛠️ Features

- Detects if a website is vulnerable to Clickjacking.
- Displays live website preview.
- Shows recommendations based on headers.
- Allows downloading a PDF report.
- Simple and beautiful frontend.

---

## 📁 Project Structure
📦 Clickjacking-Scanner
├── node_modules/
├── server.js
├── Clickjacking-Scanner.html
├── package.json
├── package-lock.json

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Clickjacking-Scanner.git
cd Clickjacking-Scanner

### 2. Install Dependencies
