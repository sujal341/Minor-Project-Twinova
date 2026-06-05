import pandas as pd
try:
    df = pd.read_excel('Research Papers List.xlsx')
    df.to_csv('research_papers.csv', index=False)
    print("Successfully converted to research_papers.csv")
except Exception as e:
    print(f"Error: {e}")
