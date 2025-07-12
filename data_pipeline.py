
import pandas as pd
import matplotlib.pyplot as plt
import logging
import sqlalchemy

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_csv_in_chunks(file_path, chunk_size=10000):
    """Reads and processes a large CSV file in chunks to conserve memory."""
    logging.info(f"Processing {file_path} in chunks of {chunk_size} rows...")
    try:
        # Initialize an empty Series to store aggregated revenue data
        total_revenue_by_product = pd.Series(dtype='float64')

        # Process the file in chunks
        with pd.read_csv(file_path, chunksize=chunk_size) as reader:
            for chunk in reader:
                # Clean data in the chunk
                chunk.dropna(inplace=True)
                
                # Aggregate revenue by product_id within the chunk
                chunk_revenue = chunk.groupby('product_id')['revenue'].sum()
                
                # Add chunk's revenue to the total
                total_revenue_by_product = total_revenue_by_product.add(chunk_revenue, fill_value=0)

        logging.info("Successfully processed all chunks.")
        return total_revenue_by_product

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None

def create_visualization(data, output_path):
    """Creates a visualization of the top 10 products by revenue."""
    logging.info("Creating visualization...")
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 8))
    
    data.sort_values(ascending=False).plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
    
    ax.set_title('Top 10 Products by Revenue', fontsize=16, fontweight='bold')
    ax.set_xlabel('Product ID', fontsize=12)
    ax.set_ylabel('Total Revenue', fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    for i, v in enumerate(data.sort_values(ascending=False)):
        ax.text(i, v + 50, f"${v:,.2f}", ha='center', va='bottom', fontsize=10)
        
    plt.tight_layout()
    plt.savefig(output_path)
    logging.info(f"Visualization saved to {output_path}")

def main():
    """Main function to run the data pipeline."""
    input_csv_path = 'sales_data.csv'
    output_plot_path = 'top_10_products.png'
    
    total_revenue = process_csv_in_chunks(input_csv_path)
    if total_revenue is not None:
        top_10_products = total_revenue.nlargest(10)
        create_visualization(top_10_products, output_plot_path)

if __name__ == '__main__':
    main()
