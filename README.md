
# Sales Data Pipeline & Visualization

This project processes sales data from a CSV file, analyzes it, and generates a bar chart of the **Top 10 Products** based on sales.  
The output chart is saved as `top_10_products.png`.

---

## 📂 Project Structure(recommended to have)
.
├── data_pipeline.py # Main Python script
├── sales_data.csv # Sample sales data
├── requirements.txt # Project dependencies
├── top_10_products.png # Output chart (generated after running the script)
└── README.md # Project documentation



---

## 🚀 Features

- Reads sales data from `sales_data.csv`
- Processes and analyzes the dataset
- Identifies the **top 10 products by sales**
- Generates a **bar chart** as an image file
- Fully automated with a single Python script

---

## 📦 Requirements

The project uses the following Python libraries:

| Library     | Purpose |
|-------------|---------|
| **pandas**  | Data loading, cleaning, and analysis |
| **matplotlib** | Chart creation and visualization |
| **sqlalchemy** | Enables database connections (optional if storing/retrieving data from a database) |

All dependencies are listed in `requirements.txt`.

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
If you want to run this project locally, first **clone it** from GitHub:
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
(If you don’t have a repository yet, create a new one on GitHub and upload these files before cloning.)

2️⃣ Create & Activate a Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Script
python data_pipeline.py
This will generate top_10_products.png in the project directory.

📊 How It Works
mermaid
flowchart 
    A[Start] --> B[Read sales_data.csv]
    B --> C[Process & clean data using Pandas]
    C --> D[Sort products by sales]
    D --> E[Select top 10 products]
    E --> F[Generate bar chart with Matplotlib]
    F --> G[Save chart as top_10_products.png]
    G --> H[End]
