import pandas as pd
import html

try:
    # Load data, skip headers
    df = pd.read_excel('Research Papers List.xlsx', skiprows=2)
    # Rename columns for easier access
    df.columns = ['Member_Index', 'USN', 'Title', 'Author', 'Year']
    
    # Filter rows that have a Title (some rows might be empty or footer)
    df = df[df['Title'].notna()]
    # Remove footer rows if any (like "TOTAL Number of papers found")
    df = df[~df['Title'].str.contains('TOTAL', case=False, na=False)]
    
    html_rows = ""
    for i, row in enumerate(df.itertuples(), 1):
        title = str(row.Title).strip()
        author = str(row.Author).strip()
        year = str(row.Year).split('.')[0] if pd.notna(row.Year) else "N/A"
        # Search link
        link = f"https://scholar.google.com/scholar?q={html.escape(title)}"
        
        html_rows += f"""
                <tr>
                    <td>{i}</td>
                    <td>{html.escape(author)}</td>
                    <td>{html.escape(title)}</td>
                    <td>{year}</td>
                    <td><a href="{link}" target="_blank" class="glass" style="padding: 5px 15px; font-size: 0.8rem; color: var(--primary);">View</a></td>
                </tr>"""
    
    with open('table_rows.txt', 'w', encoding='utf-8') as f:
        f.write(html_rows)
    print("Successfully generated table_rows.txt")

except Exception as e:
    print(f"Error: {e}")
