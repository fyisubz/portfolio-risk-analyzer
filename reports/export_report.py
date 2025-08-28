import pandas as pd
from fpdf import FPDF
import os

def export_to_excel(metrics_dict, cumulative_returns, drawdown, filename="reports/portfolio_report.xlsx"):
    metrics_df = pd.DataFrame.from_dict(metrics_dict, orient='index', columns=['Value'])
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        metrics_df.to_excel(writer, sheet_name='Metrics', index=False)
        cumulative_returns.to_frame(name='Cumulative Returns').to_excel(writer, sheet_name='Cumulative Returns')
    return filename

def export_to_pdf(metrics_dict, filename="reports/portfolio_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    
    pdf.cell(200, 10, txt="Portfolio Risk Report", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    for key, value in metrics_dict.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
    os.makedirs("reports", exist_ok=True)
    pdf.output(filename)
    return filename