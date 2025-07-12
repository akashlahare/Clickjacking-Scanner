# 🕵️‍♂️ Clickjacking Vulnerability Scanner

This tool checks if a website is vulnerable to **Clickjacking attacks** by scanning for missing security headers like `X-Frame-Options` or `Content-Security-Policy`.

![Clickjacking Scanner UI](https://github.com/akashlahare/clickjacking-scanner/blob/main/Clickjacking-Scanner.png?raw=true)

---

## How to Install and Use

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/akashlahare/clickjacking-scanner.git
   cd Clickjacking-Scanner
   ```

2. **Install Dependencies**  
   ```bash
   npm install
   ```
   This will install required Node.js packages like `express`, `axios`, and `cors`.

3. **Start the Backend Server**  
   ```bash
   node server.js
   ```
   You should see:  
   ```
   🚀 Server running on port 3000
   ```

4. **Open the Frontend**  
   - Double-click the `Clickjacking-Scanner.html` file  
   - It will open in your browser

5. **Run a Scan**  
   - Enter the target website URL (e.g., `https://example.com`)  
   - Click the search icon or press **Enter**  
   - View scan results and recommendations

6. **Download Report (Optional)**  
   - Click the **Download Report** button to save the result as a PDF

---

## 💡 What is Clickjacking?

Clickjacking is a UI redress attack where attackers trick users into clicking hidden buttons or links by embedding your website in an invisible iframe. This tool helps detect whether a site is protected against such attacks.

---

## 👨‍💻 Author

**Akash Lahare**  
🔗 [LinkedIn](https://www.linkedin.com/in/akashlahare/)  
📂 [More Projects](https://github.com/akashlahare)
---

## 📄 License
 [MIT License](https://choosealicense.com/licenses/mit/)
