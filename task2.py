import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

# Step 1: Read data
df = pd.read_csv("data.csv")

# Step 2: Analyze data (average marks per student)
summary = df.groupby("Name")["Marks"].mean()

# Step 3: Create a chart
plt.figure(figsize=(6,4))
summary.plot(kind="bar", color="skyblue")
plt.title("Average Marks of Students")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("chart.png")  # Save chart as image
plt.close()

# Step 4: Generate PDF Report
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Student Performance Report", ln=True, align="C")

pdf.ln(10)  # new line

# Add Summary in PDF
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Average Marks:", ln=True)

for name, avg in summary.items():
    pdf.cell(200, 10, txt=f"{name}: {avg:.2f}", ln=True)

# Add Chart
pdf.image("chart.png", x=40, y=80, w=120)

# Save PDF
pdf.output("report.pdf")

print("✅ PDF report generated successfully: report.pdf")

