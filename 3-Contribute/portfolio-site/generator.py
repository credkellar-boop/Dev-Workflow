import os

# Simple engine to transform your README files into a single HTML portfolio page
def generate_portfolio():
    readme_path = "README.md"
    output_html = "index.html"
    
    with open(readme_path, "r") as f:
        content = f.read()

    # Minimalist CSS for a professional look
    html_template = f"""
    <html>
        <head>
            <title>Systems Engineering Laboratory</title>
            <style>
                body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: auto; padding: 20px; }}
                h1 {{ color: #2563eb; }}
                code {{ background: #f1f5f9; padding: 2px 4px; }}
            </style>
        </head>
        <body>
            <h1>Systems Engineering Laboratory</h1>
            <pre>{content}</pre>
        </body>
    </html>
    """
    
    with open(output_html, "w") as f:
        f.write(html_template)
    print("✅ Portfolio site generated: index.html")

if __name__ == "__main__":
    generate_portfolio()
