# IP Crawler

**A simple Python tool for scraping proxy IP addresses from websites.**

---

## 🎯 Project Purpose

This project is designed to:
- Scrape proxy IP addresses, ports, and locations from a free proxy provider website.
- Save the extracted information into a well-formatted text file for further use.
- Provide a starting point for building your own proxy pool or learning web scraping.

---

## 🚀 Features

- **Scrapes Multiple Pages**: Extracts data from multiple pages of the target website.
- **Customizable**: The code can be easily adapted to scrape other proxy websites.
- **Formatted Output**: Saves results in a structured `.txt` file for easy usage.
- **Browser Simulation**: Mimics browser headers to bypass basic anti-scraping measures.

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Requests**: For sending HTTP requests.
- **lxml**: For parsing and extracting data from HTML using XPath.

---


---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/idonthav/IP-Crawler.git
   cd IP-Crawler

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows

4. Install dependencies:
   ```bash
   pip install -r requirements.txt

## 🏃 Usage
Open the ip_crawler.py file and customize the target website or number of pages if needed.
```bash
Run the script:
python ip_crawler.py

View the results in the IP_agent.txt file, which will look like this:
IP地址: 101.42.237.144       port端口号: 7890       地址: SSL高匿_北京市腾讯云       
IP地址: 101.37.31.191        port端口号: 80         地址: 高匿_浙江省杭州市阿里云    
IP地址: 219.129.167.82       port端口号: 2222       地址: 高匿_广东省汕尾市电信     

## 🔧 Configuration
Headers: The script uses a default User-Agent to simulate browser requests. You can modify it in the headers dictionary.
Target Pages: The script is set to scrape pages 1-7 by default. You can modify this range in the for loop.

## 📖 Examples of Extension
Modify the script to scrape other proxy websites.
Save the output to a database instead of a .txt file.
Integrate the proxy pool into a larger project.

## 🛡️ Common Issues and Solutions
Connection Error: Ensure the target website is accessible and not blocking your requests.
Empty Results: Double-check the XPath expressions for extracting data.

## 📃 License
This project is licensed under the MIT License. Feel free to use and modify it for your projects.

## ✨ Acknowledgments
Thanks to IP3366.net for providing free proxy data.
