import tkinter as tk
from tkinter import messagebox
import pandas as pd
import pickle
import random

# Function to load the pre-trained model from pickle
def load_model():
    global model
    with open('rf_regressor.pkl', 'rb') as f:
        model = pickle.load(f)

def predict_costs(*args):
    try:
        # Collect user inputs
        inputs = {
            'sku': int(sku_var.get()),
            'price': float(price_var.get()),
            'revenue_generated': float(revenue_generated_var.get()),
            'shipping_times': float(shipping_times_var.get()),
            'shipping_costs': float(shipping_costs_var.get()),
            'lead_time': float(lead_time_var.get()),
            'production_volumes': float(production_volumes_var.get()),
            'manufacturing_lead_time': float(manufacturing_lead_time_var.get()),
            'manufacturing_costs': float(manufacturing_costs_var.get()),
            'inspection_results': int(inspection_results_var.get()),
            'defect_rates': float(defect_rates_var.get()),
            'routes': int(routes_var.get()),
            'stock_levels': float(stock_levels_var.get())
        }

        # Prepare input data for prediction (convert inputs to a DataFrame)
        input_data = pd.DataFrame([inputs])

        # Predict costs using the trained model
        predicted_cost = model.predict(input_data)
        print(f"Original Predicted Cost: {predicted_cost[0]}")

        # Add a random factor for variability in the predicted cost
        random_variability = random.uniform(-100, 100)  # Variability between -100 and 100
        predicted_cost_with_variability = predicted_cost[0] + random_variability
        print(f"Predicted Cost with Variability: {predicted_cost_with_variability}")

        # Ensure the predicted cost stays within the desired range (200 to 1000)
        predicted_cost_with_variability = max(200, min(predicted_cost_with_variability, 1000))
        print(f"Final Predicted Cost (after capping): {predicted_cost_with_variability}")

        # Format the result message based on the prediction
        result_message = f"Predicted Costs: {predicted_cost_with_variability:.2f}"

        # Update the result label with the prediction
        result_label.config(text=result_message)

    except Exception as e:
        messagebox.showerror("Input Error", f"Error in input values: {e}")
        result_label.config(text="Predicted Costs: Error in inputs")

# Function to reset all input fields
def reset_fields():
    sku_var.set("")
    price_var.set("")
    revenue_generated_var.set("")
    shipping_times_var.set("")
    shipping_costs_var.set("")
    lead_time_var.set("")
    production_volumes_var.set("")
    manufacturing_lead_time_var.set("")
    manufacturing_costs_var.set("")
    inspection_results_var.set("")
    defect_rates_var.set("")
    routes_var.set("")
    stock_levels_var.set("")
    result_label.config(text="Predicted Costs: N/A")

# Load the trained model before starting the GUI
load_model()

# Create the main window
# Create the main window
root = tk.Tk()
root.title("E-commerce Supply Chain Cost Prediction")
root.geometry("350x550")
root.config(bg='#e0f7fa')

# Configure grid columns to expand proportionally
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Add a header label for the title on the GUI
title_label = tk.Label(root, text="E-commerce Supply Chain Cost Prediction", font=("Arial", 18, 'bold'), bg='#e0f7fa')
title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")  # sticky="nsew" ensures full span and centering

# Rest of the code remains unchanged


# Create StringVar() for each entry field to track changes dynamically
sku_var = tk.StringVar()
price_var = tk.StringVar()
revenue_generated_var = tk.StringVar()
shipping_times_var = tk.StringVar()
shipping_costs_var = tk.StringVar()
lead_time_var = tk.StringVar()
production_volumes_var = tk.StringVar()
manufacturing_lead_time_var = tk.StringVar()
manufacturing_costs_var = tk.StringVar()
inspection_results_var = tk.StringVar()
defect_rates_var = tk.StringVar()
routes_var = tk.StringVar()
stock_levels_var = tk.StringVar()

# Add a header label for the title on the GUI
title_label = tk.Label(root, text="E-commerce Supply Chain Cost Prediction", font=("Arial", 18, 'bold'), bg='#e0f7fa')
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Create labels and entry fields for each feature
sku_label = tk.Label(root, text="SKU", font=("Arial", 12), bg='#e0f7fa')
sku_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
sku_entry = tk.Entry(root, textvariable=sku_var, font=("Arial", 12))
sku_entry.grid(row=1, column=1, padx=10, pady=5)

price_label = tk.Label(root, text="Price", font=("Arial", 12), bg='#e0f7fa')
price_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
price_entry = tk.Entry(root, textvariable=price_var, font=("Arial", 12))
price_entry.grid(row=2, column=1, padx=10, pady=5)

revenue_generated_label = tk.Label(root, text="Revenue Generated", font=("Arial", 12), bg='#e0f7fa')
revenue_generated_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
revenue_generated_entry = tk.Entry(root, textvariable=revenue_generated_var, font=("Arial", 12))
revenue_generated_entry.grid(row=3, column=1, padx=10, pady=5)

shipping_times_label = tk.Label(root, text="Shipping Times", font=("Arial", 12), bg='#e0f7fa')
shipping_times_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
shipping_times_entry = tk.Entry(root, textvariable=shipping_times_var, font=("Arial", 12))
shipping_times_entry.grid(row=4, column=1, padx=10, pady=5)

shipping_costs_label = tk.Label(root, text="Shipping Costs", font=("Arial", 12), bg='#e0f7fa')
shipping_costs_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
shipping_costs_entry = tk.Entry(root, textvariable=shipping_costs_var, font=("Arial", 12))
shipping_costs_entry.grid(row=5, column=1, padx=10, pady=5)

lead_time_label = tk.Label(root, text="Lead Time", font=("Arial", 12), bg='#e0f7fa')
lead_time_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
lead_time_entry = tk.Entry(root, textvariable=lead_time_var, font=("Arial", 12))
lead_time_entry.grid(row=6, column=1, padx=10, pady=5)

production_volumes_label = tk.Label(root, text="Production Volumes", font=("Arial", 12), bg='#e0f7fa')
production_volumes_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
production_volumes_entry = tk.Entry(root, textvariable=production_volumes_var, font=("Arial", 12))
production_volumes_entry.grid(row=7, column=1, padx=10, pady=5)

manufacturing_lead_time_label = tk.Label(root, text="Manufacturing Lead Time", font=("Arial", 12), bg='#e0f7fa')
manufacturing_lead_time_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
manufacturing_lead_time_entry = tk.Entry(root, textvariable=manufacturing_lead_time_var, font=("Arial", 12))
manufacturing_lead_time_entry.grid(row=8, column=1, padx=10, pady=5)

manufacturing_costs_label = tk.Label(root, text="Manufacturing Costs", font=("Arial", 12), bg='#e0f7fa')
manufacturing_costs_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")
manufacturing_costs_entry = tk.Entry(root, textvariable=manufacturing_costs_var, font=("Arial", 12))
manufacturing_costs_entry.grid(row=9, column=1, padx=10, pady=5)

inspection_results_label = tk.Label(root, text="Inspection Results", font=("Arial", 12), bg='#e0f7fa')
inspection_results_label.grid(row=10, column=0, padx=10, pady=5, sticky="w")
inspection_results_entry = tk.Entry(root, textvariable=inspection_results_var, font=("Arial", 12))
inspection_results_entry.grid(row=10, column=1, padx=10, pady=5)

defect_rates_label = tk.Label(root, text="Defect Rates", font=("Arial", 12), bg='#e0f7fa')
defect_rates_label.grid(row=11, column=0, padx=10, pady=5, sticky="w")
defect_rates_entry = tk.Entry(root, textvariable=defect_rates_var, font=("Arial", 12))
defect_rates_entry.grid(row=11, column=1, padx=10, pady=5)

routes_label = tk.Label(root, text="Routes", font=("Arial", 12), bg='#e0f7fa')
routes_label.grid(row=12, column=0, padx=10, pady=5, sticky="w")
routes_entry = tk.Entry(root, textvariable=routes_var, font=("Arial", 12))
routes_entry.grid(row=12, column=1, padx=10, pady=5)

stock_levels_label = tk.Label(root, text="Stock Levels", font=("Arial", 12), bg='#e0f7fa')
stock_levels_label.grid(row=13, column=0, padx=10, pady=5, sticky="w")
stock_levels_entry = tk.Entry(root, textvariable=stock_levels_var, font=("Arial", 12))
stock_levels_entry.grid(row=13, column=1, padx=10, pady=5)

# Create a button to trigger the prediction
predict_button = tk.Button(root, text="Predict Costs", font=("Arial", 14), bg='#4CAF50', fg='white', command=predict_costs)
predict_button.grid(row=14, column=0, columnspan=2, pady=10)

# Create a reset button
reset_button = tk.Button(root, text="Reset Fields", font=("Arial", 14), bg='#f44336', fg='white', command=reset_fields)
reset_button.grid(row=15, column=0, columnspan=2, pady=10)

# Create a label to display the result message
result_label = tk.Label(root, text="Predicted Costs: N/A", font=("Arial", 10), bg='#e0f7fa', fg='#333333')
result_label.grid(row=16, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
