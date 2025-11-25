Project 4: TCGA RNA-seq Data Analysis (Data Science Version)

Goal: Analyze gene expression differences between tumor and normal tissue samples from TCGA data using a pure Python "Data Science" approach. This method leverages Pandas for data manipulation and Seaborn for visualization, avoiding the complexity of multi-language pipelines (Bash/R).

🚀 Key Features

Pure Python: The entire workflow—data extraction, transformation, and visualization—is contained in a single Python script.

Robust Metadata Handling: Loads the GDC sample sheet into a Pandas DataFrame for powerful filtering and selection.

Visual Analysis: Uses seaborn to generate professional-quality boxplots with overlaid strip plots to show individual data points.

Error Resilience: Includes error handling for missing files or malformed data lines.

📂 File Structure

File

Language

Description

project4_datascience.py

Python

The main script that extracts data and generates the plot.

🛠 Prerequisites

Python 3.x

Libraries: pandas, seaborn, matplotlib, numpy

To install dependencies:

pip install pandas seaborn matplotlib numpy


⚙️ Usage

1. Prepare Data

Ensure you have the following files in your working directory:

gdc_sample_sheet.tsv (Metadata)

Unzipped data folders (containing the *.augmented_star_gene_counts.tsv files)

2. Run the Script

python3 project4_datascience.py


Output:

nkx2_1_seaborn_plot.png: A visualization comparing NKX2-1 expression levels in Primary Tumor vs. Solid Tissue Normal samples.
