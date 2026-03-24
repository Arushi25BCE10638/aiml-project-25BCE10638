import tkinter as tk
from tkinter import messagebox

#symptom-disease graph
medical_graph = {
    "Start": ["Fever", "Cough", "Skin Rash"],
    "Fever": ["High Grade", "Low Grade"],
    "High Grade": ["Malaria"],
    "Low Grade": ["Common Cold"],
    "Cough": ["Persistent", "Short-term"],
    "Persistent": ["Tuberculosis"],
    "Short-term": ["Bronchitis"],
    "Skin Rash": ["Itchy", "Non-itchy"],
    "Itchy": ["Chickenpox"],
    "Non-itchy": ["Measles"]}

#disease database
disease_info = {"Malaria": {
        "symptoms": "High fever, chills, sweating, headache, and nausea.",
        "precautions": "Use mosquito nets, wear long sleeves, and use insect repellent."},
    "Common Cold": {
        "symptoms": "Runny nose, sneezing, sore throat, and mild cough.",
        "precautions": "Rest, stay hydrated, and wash hands frequently."},
    "Tuberculosis": {
        "symptoms": "Chronic cough (often with blood), chest pain, weight loss, and fatigue.",
        "precautions": "Wear a mask, ensure good ventilation, and complete the full antibiotic course."},
    "Bronchitis": {
        "symptoms": "Cough with mucus, shortness of breath, and chest discomfort.",
        "precautions": "Avoid smoke and air pollutants, use a humidifier, and get plenty of rest."},
    "Chickenpox": {
        "symptoms": "Itchy red blisters, fever, and tiredness.",
        "precautions": "Avoid scratching, stay isolated to prevent spread, and use calamine lotion."},
    "Measles": {
        "symptoms": "High fever, dry cough, runny nose, and a characteristic skin rash.",
        "precautions": "Isolate from others, stay hydrated, and ensure vitamin A intake."}}

#background colors and font styles
class MedicalAIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Medical Assistant")
        self.root.geometry("500x620")
        self.bg_warm = "#FFF5E1"
        self.btn_warm = "#FF6B6B"
        self.text_color = "#4A4A4A"
        self.accent_color = "#E67E22" 
        self.root.configure(bg=self.bg_warm)
        self.user_name = ""
        self.current_node = "Start"
        self.main_container = tk.Frame(self.root, bg=self.bg_warm)
        self.main_container.pack(expand=True, fill="both", padx=30, pady=20)
        self.setup_name_screen()

    def clear_container(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def setup_name_screen(self):
        self.clear_container()
        tk.Label(self.main_container, text="Medical AI Assistant", font=("Arial", 18, "bold"), bg=self.bg_warm, fg=self.btn_warm).pack(pady=30)
        tk.Label(self.main_container, text="Please enter your name to begin:", font=("Arial", 11), bg=self.bg_warm, fg=self.text_color).pack(pady=10)
        self.name_entry = tk.Entry(self.main_container, font=("Arial", 12), width=25, justify='center')
        self.name_entry.pack(pady=10)
        start_btn = tk.Button(self.main_container, text="Start Diagnosis", font=("Arial", 10, "bold"), bg=self.btn_warm, fg="white", relief="flat", cursor="hand2", command=self.start_app)
        start_btn.pack(pady=20, ipady=8, ipadx=15)

    def start_app(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Required", "Please enter your name.")
            return
        self.user_name = name
        self.show_symptom_screen()

    def show_symptom_screen(self):
        self.clear_container()
        tk.Label(self.main_container, text=f"Patient: {self.user_name}", font=("Arial", 12, "bold"), bg=self.bg_warm, fg=self.text_color).pack(pady=5)
        tk.Label(self.main_container, text="Select your current symptom:", font=("Arial", 11), wraplength=400, bg=self.bg_warm, fg=self.text_color).pack(pady=15)
        self.button_frame = tk.Frame(self.main_container, bg=self.bg_warm)
        self.button_frame.pack(pady=10)
        self.update_options()

    def update_options(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        options = medical_graph.get(self.current_node, [])
        for opt in options:
            btn = tk.Button(self.button_frame, text=opt, width=25, font=("Arial", 10, "bold"), bg=self.btn_warm, fg="white", activebackground="#FF8787", relief="flat", cursor="hand2", command=lambda o=opt: self.dfs_search(o))
            btn.pack(pady=8, ipady=5)

    def dfs_search(self, choice):
        next_options = medical_graph.get(choice, [])
        if choice not in medical_graph:
            self.display_final_result(choice)
            return
        if len(next_options) == 1 and next_options[0] not in medical_graph:
            self.display_final_result(next_options[0])
        else:
            self.current_node = choice
            self.update_options()
    def display_final_result(self, disease):
        #displays full assessment in the same window
        self.clear_container()
        info = disease_info.get(disease, {})
        tk.Label(self.main_container, text="Assessment Complete", font=("Arial", 16, "bold"), bg=self.bg_warm, fg=self.accent_color).pack(pady=10)
        tk.Label(self.main_container, text=f"Hello {self.user_name},", font=("Arial", 12, "bold"), bg=self.bg_warm, fg=self.text_color).pack(anchor="w")
        tk.Label(self.main_container, text=f"Based on your symptoms, it is possible you have:", font=("Arial", 11), bg=self.bg_warm, fg=self.text_color).pack(anchor="w", pady=(0, 5))
        tk.Label(self.main_container, text=disease.upper(), font=("Arial", 20, "bold"), bg=self.bg_warm, fg=self.btn_warm).pack(pady=15)
        detail_card = tk.Frame(self.main_container, bg="#FFF9F0", padx=15, pady=15, highlightbackground="#FFD8A8", highlightthickness=1)
        detail_card.pack(fill="x", pady=10)
        tk.Label(detail_card, text="TYPICAL SYMPTOMS:", font=("Arial", 10, "bold"), bg="#FFF9F0", fg=self.text_color).pack(anchor="w")
        tk.Label(detail_card, text=info.get('symptoms'), font=("Arial", 10), bg="#FFF9F0", fg=self.text_color, wraplength=380, justify="left").pack(anchor="w", pady=(0, 10))
        tk.Label(detail_card, text="PRECAUTIONS:", font=("Arial", 10, "bold"), bg="#FFF9F0", fg=self.text_color).pack(anchor="w")
        tk.Label(detail_card, text=info.get('precautions'), font=("Arial", 10), bg="#FFF9F0", fg=self.text_color, wraplength=380, justify="left").pack(anchor="w")
        disclaimer_text = "MEDICAL ADVICE: Please consult a doctor if your health deteriorates further. This is for information only."
        tk.Label(self.main_container, text=disclaimer_text, font=("Arial", 9, "bold italic"), bg=self.bg_warm, fg="#C0392B", wraplength=400, pady=20).pack()
        restart_btn = tk.Button(self.main_container, text="Restart Analysis", font=("Arial", 10, "bold"), bg=self.btn_warm, fg="white", relief="flat", cursor="hand2", command=self.reset_app)
        restart_btn.pack(pady=10, ipady=8, ipadx=15)

    def reset_app(self):
        self.current_node = "Start"
        self.show_symptom_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalAIApp(root)
    root.mainloop()
