# Clickjacking Scanner  
A tool to check if a website is vulnerable to clickjacking attacks.  

## Installation & Setup  
Follow these steps to install and run the tool on your local machine.  

### Step 1: Clone the Repository  
Clone the GitHub repository to your system:  

git clone https://github.com/akashlahare/clickjacking-scanner.git
cd clickjacking-scanner
### Step 2: Install Dependencies
Install the required dependencies using:

npm install
This will install all necessary packages listed in package.json.

### Step 3: Start the Server
Run the following command to start the backend server:

node server.js
The server will start and listen for requests at http://localhost:3000.

### Step 4: Open the Clickjacking Scanner
Open the clickjackingweb.html file in your browser.
Enter the URL of the website you want to scan.
Click the "Scan" button to check for vulnerabilities.

### Step 5: Perform Bulk Scanning (Optional)
Upload a .txt file containing multiple URLs (one per line).
The tool will process each URL and check for vulnerabilities.

### Step 6: Download the Scan Report
After scanning, click on "Download Report" to generate a PDF summary of the results.

### Step 7: Notes & Recommendations
Ensure Node.js is installed before running the server.
If you encounter issues, check the console logs for debugging.
To deploy this tool online, you may use Heroku, Vercel, or AWS.
