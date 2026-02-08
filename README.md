<div align="center">

  <img src="https://cdn-icons-png.flaticon.com/512/2920/2920349.png" alt="logo" width="100" height="100" />
  <h1>RFM Customer Segmentation Analysis</h1>
  
  <p>
    <b>Transforming transactional data into actionable business strategies using SQL & Python.</b>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/SQL-SQLite-orange?logo=sqlite&logoColor=white" alt="SQL" />
    <img src="https://img.shields.io/badge/Library-Pandas-150458?logo=pandas&logoColor=white" alt="Pandas" />
    <img src="https://img.shields.io/badge/Library-NumPy-013243?logo=numpy&logoColor=white" alt="NumPy" />
    <img src="https://img.shields.io/badge/Status-Completed-success" alt="Status" />
  </p>

  <br />

  <img src="./segmentation_chart.png" alt="Customer Segmentation Chart" width="800" />

</div>

<hr />

<h2>📌 Project Overview</h2>
<p>
  This project analyzes customer behavior using the <b>RFM (Recency, Frequency, Monetary)</b> technique on the "Online Retail II" dataset. By simulating a real-world data pipeline, I bridged <b>SQL</b> for efficient data extraction and <b>Python</b> for advanced statistical scoring.
</p>

<h3>🔍 Key Features</h3>
<ul>
  <li><b>Hybrid Pipeline:</b> SQL for heavy aggregations + Python for analytics.</li>
  <li><b>Vectorized Scoring:</b> Utilizing <code>NumPy</code> and <code>Pandas</code> for high-performance calculations.</li>
  <li><b>Actionable Insights:</b> Classifying customers into 4 distinct segments for marketing targeting.</li>
</ul>

<hr />

<h2>📊 Analysis Results</h2>
<p>Below is a snapshot of the segmentation logic applied to the dataset:</p>

<table align="center">
  <thead>
    <tr>
      <th>Segment</th>
      <th>Description</th>
      <th>Actionable Strategy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>🌟 <b>Top Customer</b></td>
      <td>High spending, frequent visits, recent activity.</td>
      <td>Provide VIP offers & loyalty programs.</td>
    </tr>
    <tr>
      <td>💎 <b>Loyal Customer</b></td>
      <td>Good frequency and monetary value.</td>
      <td>Upsell new products & encourage reviews.</td>
    </tr>
    <tr>
      <td>⚠️ <b>Needs Attention</b></td>
      <td>Recent purchase but low frequency.</td>
      <td>Send discount codes to increase engagement.</td>
    </tr>
    <tr>
      <td>📉 <b>At Risk</b></td>
      <td>High value in past, but hasn't visited recently.</td>
      <td>Win-back campaigns immediately.</td>
    </tr>
  </tbody>
</table>

<hr />

<h2>🛠 How to Run</h2>
<p>Follow these steps to reproduce the analysis:</p>

<pre>
<code>
# 1. Clone the repository
git clone https://github.com/SeyyedSajjadFazeli/RFM-Customer-Segmentation.git

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn

# 3. Run the analysis script
python analysis.py

# 4. Generate visualizations
python visualize.py
</code>
</pre>

<hr />

<div align="center">
  <p><i>Developed by Seyyed Sajjad Fazeli - Data Analysis Engineer</i></p>
  <p>
    <a href="https://www.linkedin.com/in/seyyed-sajjad-fazeli-a58aa1360">
      <img src="https://img.shields.io/badge/Connect-LinkedIn-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn" />
    </a>
  </p>
</div>
