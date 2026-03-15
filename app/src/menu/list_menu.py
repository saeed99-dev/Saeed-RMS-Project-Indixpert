class Manage_menu:
    def __init__(self):
        self.menu = {
            "starters": [
                {"index":1,"name": "manchurian", "half": 80.0, "full": 140.0},
                {"index":2,"name": "chilli", "half": 80.0, "full": 150.0},
                {"index":3,"name": "leefu", "half": 90.0, "full": 180.0},
                {"index":4,"name": "kung pao", "half": 90.0, "full": 180.0},
                {"index":5,"name": "drumps of heaven", "half": 130.0, "full": 250.0},
            ],
            "main course: veg": [
                {"index":1,"name": "mix veg curry", "half": 100.0, "full": 180.0},
                {"index":2,"name": "Aloo Gobi Masala", "half": 90.0, "full": 160.0},
                {"index":3,"name": "Dum Aloo", "half": 100.0, "full": 180.0},
                {"index":4,"name": "Dal Makhani", "half": 120.0, "full": 200.0},
                {"index":5,"name": "Sahi Paneer", "half": 160.0, "full": 280.0},
                {"index":6,"name": "Kadhai Paneer", "half": 150.0, "full": 250.0},
                {"index":7,"name": "Matar Mashroom", "half": 180.0, "full": 250.0},
                {"index":8,"name": "Paneer Bhurji", "half": None, "full": 300.0}   
            ],
            "main course: non-veg": [
                {"index":1,"name": "Chiken Dum Biryani", "half": 180.0, "full": 320.0},
                {"index":2,"name": "Chicken Handi", "half": 160.0, "full": 300.0},
                {"index":3,"name": "Chicken sweet & sour", "half": 140.0, "full": 230.0},
                {"index":4,"name": "Butter Chicken", "half": 220.0, "full": 450.0},
                {"index":5,"name": "Chicken Fried", "half": 180.0, "full": 350.0} 
            ],
            "main course: non-veg": [
                {"index":1,"name": "Chiken Dum Biryani", "half": 180.0, "full": 320.0},
                {"index":2,"name": "Chicken Handi", "half": 160.0, "full": 300.0},
                {"index":3,"name": "Chicken sweet & sour", "half": 140.0, "full": 230.0},
                {"index":4,"name": "Butter Chicken", "half": 220.0, "full": 450.0},
                {"index":5,"name": "Chicken Fried", "half": 180.0, "full": 350.0} 
            ],
        }
        self.cart=[]

    def dislay_menu(self):
        print("="*55)
        print(f"{'RESTAURANT MENU':>32}")
        print("="*55)

        for category,items in self.menu.items():
            print(f"\n{category.upper()}")
            print("-"*55)
            print(f"{"Index":<10}{"Name":<25}{"Half":<10}{"Full":<10}")
            print("-"*55)

            for item in items:
                half=f"₹{item["half"]}" if {item["half"]} else '-'
                full=f"₹{item["full"]}" if {item["full"]} else '-'
                print(f"{item["index"]:<5}{item["name"].capitalize():<30}{half:<10}{full:<10}")
            print("="*55)





menu=Manage_menu()
menu.dislay_menu()
