import csv
import os
import math
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
SAMPLE_SHEET = "gdc_sample_sheet.tsv"
TARGET_GENE = "NKX2-1"
OUTPUT_IMAGE = "nkx2-1_boxplot.png"

def get_gene_values(file_list, target_gene):
    """
    Reads a list of files, finds the target gene, 
    and returns list of Log2(TPM+1) values.
    """
    values = []
    files_processed = 0
    
    for filepath in file_list:
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, "r") as f:
            for line in f:
                # TCGA data usually has header lines starting with N_ or gene_id
                if line.startswith("N_") or line.startswith("gene_id"):
                    continue
                
                # Check if this line is for our target gene
                # We check "in line" to be safe, assuming gene name is distinct
                if target_gene in line:
                    parts = line.split('\t')
                    
                    # 7th column is TPM (index 6)
                    try:
                        tpm = float(parts[6])
                        
                        # Project requirement: Log2(TPM + 1)
                        log_tpm = math.log2(tpm + 1)
                        
                        values.append(log_tpm)
                        files_processed += 1
                    except (IndexError, ValueError):
                        pass
                    
                    # Found the gene, move to next file
                    break
    
    return values

def main():
    print("--- Project 4: TCGA Analysis ---")
    
    # 1. Parse Metadata
    print("Step 1: Parsing metadata...")
    tumor_files = []
    normal_files = []
    
    try:
        with open(SAMPLE_SHEET, "r") as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                # Construct path: File ID / File Name
                path = os.path.join(row['File ID'], row['File Name'])
                
                if row['Sample Type'] == 'Primary Tumor':
                    tumor_files.append(path)
                elif row['Sample Type'] == 'Solid Tissue Normal':
                    normal_files.append(path)
    except FileNotFoundError:
        print(f"Error: {SAMPLE_SHEET} not found.")
        return

    print(f"Found {len(tumor_files)} Tumor samples.")
    print(f"Found {len(normal_files)} Normal samples.")

    # 2. Extract Data
    print(f"Step 2: Extracting {TARGET_GENE} expression...")
    tumor_vals = get_gene_values(tumor_files, TARGET_GENE)
    normal_vals = get_gene_values(normal_files, TARGET_GENE)

    # 3. Visualization
    print("Step 3: Creating Boxplot...")
    plt.figure(figsize=(8, 6))
    
    # Create Boxplot
    # We pass the list [Normal, Tumor] to match the X-axis order in the prompt
    plt.boxplot([normal_vals, tumor_vals], labels=['Solid Tissue Normal', 'Primary Tumor'])
    
    plt.ylabel("Log2 (TPM + 1)")
    plt.title(f"{TARGET_GENE} Expression in LUAD")
    
    # Add n= counts to the plot (optional, but looks professional)
    plt.text(1, max(normal_vals), f"n={len(normal_vals)}", ha='center', va='bottom')
    plt.text(2, max(tumor_vals), f"n={len(tumor_vals)}", ha='center', va='bottom')

    plt.savefig(OUTPUT_IMAGE, dpi=300)
    print(f"Success! Plot saved to {OUTPUT_IMAGE}")

if __name__ == "__main__":
    main()