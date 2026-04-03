from datetime import datetime

class Inventory:
    def __init__(self, file_manager, path_model):
        self.file_manager = file_manager
        self.path_model = path_model
        # Structure: {"item_name": {"stock": 100, "unit": "kg", "threshold": 10}}
        self.inventory_data = self.file_manager.load_data(self.path_model.inventory_data)

    def check_availability(self, item_name, qty_needed):
        """Check if enough ingredients exist for a menu item."""
        # Simple mapping: in a real app, 1 Burger might need 1 Bun, 100g Patty, etc.
        # For this logic, we assume 1 menu item = 1 unit of its primary ingredient.
        item_stock = self.inventory_data.get(item_name.lower())
        if not item_stock:
            return True  # If not tracked in inventory, assume available
        
        return item_stock['stock'] >= qty_needed

    def deduct_stock(self, item_name, qty):
        """Deduct stock after a successful order."""
        name_lower = item_name.lower()
        if name_lower in self.inventory_data:
            self.inventory_data[name_lower]['stock'] -= qty
            self.file_manager.save_data(self.inventory_data, self.path_model.inventory_data)

    def generate_inventory_report(self):
        """Prints a detailed inventory status report."""
        print("\n" + "=" * 60)
        print(f"{'INVENTORY STATUS REPORT':^60}")
        print("=" * 60)
        print(f"{'Ingredient':<25}{'Current Stock':<15}{'Status':<15}")
        print("-" * 60)

        for name, data in self.inventory_data.items():
            status = "GOOD"
            if data['stock'] <= data['threshold']:
                status = "!!! LOW !!!"
            if data['stock'] <= 0:
                status = "OUT OF STOCK"
            
            print(f"{name.capitalize():<25}{f'{data['stock']} {data['unit']}':<15}{status:<15}")
        print("=" * 60)

class BusinessAnalytics:
    def __init__(self, order_history):
        self.history = order_history

    def generate_management_report(self):
        if not self.history:
            print("\nNo data available for analytics.")
            return

        total_revenue = sum(order['bill_amount'] for order in self.history)
        total_orders = len(self.history)
        
        # Item popularity tracking using standard dictionaries
        item_counts = {}
        payment_methods = {}

        for order in self.history:
            # Count payment methods
            pm = order['payment']
            payment_methods[pm] = payment_methods.get(pm, 0) + 1
            
            for item in order['items']:
                name = item['name']
                item_counts[name] = item_counts.get(name, 0) + item['qty']

        # Determine top selling item manually
        top_item_name = "N/A"
        top_item_qty = 0
        for name, qty in item_counts.items():
            if qty > top_item_qty:
                top_item_qty = qty
                top_item_name = name

        print("\n" + "╔" + "═" * 58 + "╗")
        print(f"║{'CANVAS BUSINESS ANALYTICS':^58}║")
        print("╠" + "═" * 58 + "╣")
        print(f"║ Total Revenue:           ₹{total_revenue:<33.2f}║")
        print(f"║ Total Orders Placed:     {total_orders:<35}║")
        print(f"║ Average Order Value:     ₹{total_revenue/total_orders if total_orders else 0:<33.2f}║")
        print(f"║ Most Popular Item:       {top_item_name.capitalize():<20} ({top_item_qty} sold) ║")
        print("╠" + "═" * 58 + "╣")
        
        print(f"║ {'PAYMENT METHOD DISTRIBUTION':^56} ║")
        for method, count in payment_methods.items():
            perc = (count/total_orders) * 100
            print(f"║ - {method:<20}: {count:>3} orders ({perc:>5.1f}%)         ║")
        
        print("╚" + "═" * 58 + "╝")

# --- Integration Logic (How to use in your existing Menu class) ---
# 1. Inside search_and_order:
#    if not inventory.check_availability(selected["name"], qty):
#        print("SORRY: This item is currently Out of Stock!")
#        return

# 2. Inside view_bill (after saving to order_history):
#    for item in self.cart:
#        inventory.deduct_stock(item["name"], item["qty"])