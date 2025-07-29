# main.py

import tkinter as tk
from tkinter import ttk, messagebox
import database as db  # Local database module


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Innovative Student Management Solutions")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)

        self.entries = {}

        # ---------------- Frame Setup ----------------
        self.setup_entry_frame()
        self.setup_tree_frame()
        self.refresh_treeview()

    def setup_entry_frame(self):
        entry_frame = tk.Frame(self.root, padx=20, pady=20)
        entry_frame.pack(side=tk.TOP, fill=tk.X)

        labels = ["Name:", "Age:", "Email:", "College:", "Address:", "Mobile:"]
        for i, label in enumerate(labels):
            tk.Label(entry_frame, text=label).grid(row=i, column=0, sticky='w', pady=5)
            entry = tk.Entry(entry_frame, width=40)
            entry.grid(row=i, column=1, pady=5)
            self.entries[label[:-1].lower()] = entry

        # Buttons below the form
        button_frame = tk.Frame(entry_frame, pady=10)
        button_frame.grid(row=len(labels), column=0, columnspan=2)

        tk.Button(button_frame, text="Add Student", command=self.add_student).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Update Selected", command=self.update_student).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Delete Selected", command=self.delete_student).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Clear Fields", command=self.clear_fields).pack(side=tk.LEFT, padx=10)

    def setup_tree_frame(self):
        tree_frame = tk.Frame(self.root, padx=20, pady=10)
        tree_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        columns = ("ID", "Name", "Age", "Email", "College", "Address", "Mobile")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show='headings', selectmode='browse')

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_item_select)

    def refresh_treeview(self):
        """Refresh the treeview display from DB."""
        self.tree.delete(*self.tree.get_children())
        for student in db.get_all_students():
            self.tree.insert("", tk.END, values=list(student.values()))

    def get_entry_data(self):
        """Get current entry field values as a dictionary."""
        return {key: entry.get().strip() for key, entry in self.entries.items()}

    def validate_fields(self, data):
        """Ensure all fields are filled in."""
        return all(data.values())

    def add_student(self):
        data = self.get_entry_data()
        if not self.validate_fields(data):
            messagebox.showerror("Validation Error", "All fields are required.")
            return

        if db.add_student(**data):
            messagebox.showinfo("Success", "Student added successfully!")
            self.refresh_treeview()
            self.clear_fields()
        else:
            messagebox.showerror("Database Error", "Failed to add student. Check console for details.")

    def update_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Student", "Please select a student to update.")
            return

        student_id = self.tree.item(selected[0])["values"][0]
        data = self.get_entry_data()

        if not self.validate_fields(data):
            messagebox.showerror("Validation Error", "All fields are required.")
            return

        if db.update_student(student_id, **data):
            messagebox.showinfo("Success", "Student updated successfully!")
            self.refresh_treeview()
            self.clear_fields()
        else:
            messagebox.showerror("Database Error", "Failed to update student.")

    def delete_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Student", "Please select a student to delete.")
            return

        student_id = self.tree.item(selected[0])["values"][0]
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this student?")
        if confirm and db.delete_student(student_id):
            messagebox.showinfo("Success", "Student deleted successfully!")
            self.refresh_treeview()
            self.clear_fields()
        else:
            messagebox.showerror("Database Error", "Failed to delete student.")

    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        if self.tree.selection():
            self.tree.selection_remove(self.tree.selection()[0])

    def on_item_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return

        values = self.tree.item(selected[0], "values")
        field_keys = ['name', 'age', 'email', 'college', 'address', 'mobile']

        for i, key in enumerate(field_keys):
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, values[i + 1])  # Skip ID


# ---------------- Run the App ----------------

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = StudentApp(root)
        root.mainloop()
    except Exception as e:
        print("\n[CRITICAL ERROR] The application could not start.")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")
