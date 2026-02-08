import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load results
df = pd.read_csv('rfm_analysis_result.csv')

# 2. Count segments
segment_counts = df['Customer_Type'].value_counts().reset_index()
segment_counts.columns = ['Customer_Type', 'Count']

# 3. Create a professional Bar Plot
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
palette = {'Top Customer': '#2ecc71', 'Loyal Customer': '#3498db', 
           'Needs Attention': '#f1c40f', 'At Risk': '#e74c3c'}

ax = sns.barplot(x='Customer_Type', y='Count', data=segment_counts, palette=palette)

# Add titles and labels
plt.title('Customer Segmentation Distribution (RFM Analysis)', fontsize=15, fontweight='bold')
plt.xlabel('Customer Segment', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)

# Show numbers on bars
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# 4. Save Image
plt.savefig('segmentation_chart.png', dpi=300)
print("Chart saved as 'segmentation_chart.png'")
plt.show()