import tkinter as tk
from tkinter import ttk
from itertools import product

class DomainCombiner:
    def __init__(self, root):
        self.root = root
        self.root.title("Domain Name Combiner")
        self.root.geometry("600x400")

        # Create first combobox
        self.label1 = ttk.Label(root, text="First Word List:")
        self.label1.pack(pady=5)
        self.combo1 = ttk.Combobox(root, width=40)
        self.combo1['values'] = ['web', 'net', 'tech', 'digital', 'online']
        self.combo1.pack(pady=5)

        # Create second combobox
        self.label2 = ttk.Label(root, text="Second Word List:")
        self.label2.pack(pady=5)
        self.combo2 = ttk.Combobox(root, width=40)
        self.combo2['values'] = ['site', 'hub', 'zone', 'space', 'spot']
        self.combo2.pack(pady=5)

        # Create button to generate combinations
        self.generate_button = ttk.Button(root, text="Generate Combinations", command=self.generate_combinations)
        self.generate_button.pack(pady=10)

        # Create text area for results
        self.result_text = tk.Text(root, height=15, width=50)
        self.result_text.pack(pady=10)

    def generate_combinations(self):
        # Clear previous results
        self.result_text.delete(1.0, tk.END)
        
        # Get values from comboboxes
        word1 = self.combo1.get()
        word2 = self.combo2.get()
        
        if not word1 or not word2:
            self.result_text.insert(tk.END, "Please select words from both lists")
            return

        # Generate combinations
        combinations = [
            f"{word1}{word2}.com",
            f"{word1}-{word2}.com",
            f"{word2}{word1}.com",
            f"{word2}-{word1}.com"
        ]

        # Display results
        for combo in combinations:
            self.result_text.insert(tk.END, combo + "\n")

def main():
    root = tk.Tk()
    app = DomainCombiner(root)
    root.mainloop()

if __name__ == "__main__":
    main()