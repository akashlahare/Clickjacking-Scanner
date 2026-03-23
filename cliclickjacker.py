import asyncio
import httpx
import pandas as pd
import argparse
import webbrowser

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def normalize_url(url):
    if not url.startswith("http"):
        return "https://" + url
    return url.strip()


# 🔍 Scan logic
async def scan_target(url):
    url = normalize_url(url)

    try:
        async with httpx.AsyncClient(timeout=8, follow_redirects=True) as client:
            res = await client.get(url)

        headers = {k.lower(): v for k, v in res.headers.items()}

        xfo = headers.get("x-frame-options", "").lower()
        csp = headers.get("content-security-policy", "").lower()

        vulnerable = True

        # XFO check
        if "deny" in xfo or "sameorigin" in xfo:
            vulnerable = False

        # CSP check
        if "frame-ancestors" in csp:
            if "none" in csp or "'self'" in csp:
                vulnerable = False
            elif "*" in csp:
                vulnerable = True

        return {
            "url": url,
            "status": "Vulnerable" if vulnerable else "Not Vulnerable"
        }

    except:
        return {
            "url": url,
            "status": "Error"
        }


# 📂 Load targets
def load_targets(file_path):
    if file_path.endswith(".txt"):
        with open(file_path) as f:
            urls = [line.strip() for line in f if line.strip()]

    elif file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
        urls = df.iloc[:, 0].dropna().tolist()

    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
        urls = df.iloc[:, 0].dropna().tolist()

    else:
        raise Exception("Unsupported file format")

    return list(set(urls))  # remove duplicates


# ⚡ Async scan
async def run_scan(urls):
    tasks = [scan_target(url) for url in urls]
    return await asyncio.gather(*tasks)


# 🖥️ Terminal output
def print_results(results, open_vuln=False):
    for r in results:
        if r["status"] == "Vulnerable":
            print(f"[🔴 VULNERABLE] {r['url']}")
            if open_vuln:
                webbrowser.open(r["url"])

        elif r["status"] == "Not Vulnerable":
            print(f"[🟢 SAFE] {r['url']}")
        else:
            print(f"[⚠️ ERROR] {r['url']}")


# 🌐 HTML report (centered + smaller table)
def generate_html(results, filename):
    html = """
    <html>
    <head>
        <title>Clickjacking Report</title>
        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                padding: 20px;
                text-align: center;
            }

            table {
                width: 60%;
                margin: 20px auto;
                border-collapse: collapse;
            }

            th, td {
                border: 1px solid white;
                padding: 10px;
                text-align: left;
            }

            th {
                background: #1e293b;
            }

            .vuln { color: red; font-weight: bold; }
            .safe { color: #4ade80; font-weight: bold; }
            .error { color: orange; font-weight: bold; }

            a { color: cyan; text-decoration: none; }
        </style>
    </head>
    <body>

    <h2>Clickjacking Scan Report</h2>

    <table>
        <tr>
            <th>Target URL</th>
            <th>Status</th>
        </tr>
    """

    for r in results:
        if r["status"] == "Vulnerable":
            status_html = '<span class="vuln">Vulnerable</span>'
            url_html = f'<a href="{r["url"]}" target="_blank">{r["url"]}</a>'

        elif r["status"] == "Not Vulnerable":
            status_html = '<span class="safe">Safe</span>'
            url_html = r["url"]

        else:
            status_html = '<span class="error">Error</span>'
            url_html = r["url"]

        html += f"""
        <tr>
            <td>{url_html}</td>
            <td>{status_html}</td>
        </tr>
        """

    html += """
    </table>
    </body>
    </html>
    """

    with open(filename, "w") as f:
        f.write(html)

    print(f"[+] Report saved: {filename}")


# 🎯 Main
def main():
    parser = argparse.ArgumentParser(description="Clickjacking Scanner CLI")

    parser.add_argument("-u", "--url", help="Single URL")
    parser.add_argument("-f", "--file", help="File with URLs")
    parser.add_argument("-o", "--output", help="Save report (example: report.html)")
    parser.add_argument("--open", action="store_true", help="Open vulnerable sites in browser")

    args = parser.parse_args()

    if not args.url and not args.file:
        print("[-] Provide --url or --file")
        return

    if args.url:
        urls = [args.url]
    else:
        urls = load_targets(args.file)

    results = asyncio.run(run_scan(urls))

    print_results(results, args.open)

    # Save only if -o provided
    if args.output:
        generate_html(results, args.output)


if __name__ == "__main__":
    main()