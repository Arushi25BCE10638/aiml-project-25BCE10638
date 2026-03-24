AI Medical Diagnosis Assistant

Overview:
The AI Medical Diagnosis Assistant is a Python-based desktop application designed to provide a preliminary health assessment.
This tool bridges the gap between complex medical data and user-friendly interfaces using a Rule-Based Expert System to categorize symptoms.
The application utilizes a Depth-First Search (DFS) algorithm to navigate a specialized Directed Acyclic Graph (DAG).
By treating each symptom as a node, the AI traverses deeper into specific branches based on user input until it reaches a "leaf node"—the final diagnosis.

Features:
1. Personalization: Captures the user's name during a registration phase for a tailored experience.
2. Dynamic Navigation: A button-driven interface that updates options in real-time based on previous selections.
3. Modular Architecture: Follows a Modular Monolithic design, separating the Knowledge Base (medical graph and disease info) from the Controller and View
4. Stress-Reducing UI: Employs a warm color palette (#FFF5E1 Cream and #FF6B6B Coral) to provide a calm environment and reduce user anxiety.
5. Safety First: Includes a clear medical disclaimer and safety precautions for every diagnosis.
6. State Management: Users can reset the diagnosis path at any point without losing their session data.

Technical Stack:

Language: Python

GUI Framework: Tkinter

Data Structures: Dictionaries used for the Knowledge Base and Symptom-Disease Graph

Diagnosis Logic:
1. The system mimics professional diagnostic reasoning through a structured workflow:
2. Input Validation: Ensures user details are provided.
<img width="433" height="457" alt="image" src="https://github.com/user-attachments/assets/29159cdc-4880-4e4f-82f6-614259437d42" />

3. Symptom Root: Initial selection (e.g., Fever, Cough, Skin Rash).
<img width="452" height="375" alt="image" src="https://github.com/user-attachments/assets/ed440b22-9587-4287-8bf2-b4db50b15df1" />

4. Severity/Sub-symptom Check: Deeper traversal into the graph.
<img width="505" height="417" alt="image" src="https://github.com/user-attachments/assets/4c0f50ed-d4f8-4395-a710-ec18cdb865e0" />

5. Final Leaf Node: Reaching a diagnosis like Malaria, Tuberculosis, or Chickenpox.
<img width="497" height="566" alt="image" src="https://github.com/user-attachments/assets/27b7d578-b321-4948-87ea-d8c6d80fee7a" />


How to Run:
1. Prerequisites: Ensure you have Python installed on your system.
2. Launch: Run the script using the following command:python "aiml project.py"
3. Usage: Enter your name and click Start Diagnosis.
<img width="498" height="426" alt="image" src="https://github.com/user-attachments/assets/7b6da167-239b-480d-91f1-51aeb5006908" />

4. Follow the button prompts to select your current symptoms.
<img width="452" height="375" alt="image" src="https://github.com/user-attachments/assets/8e9ed698-66e8-4290-9b09-00429db02d7b" />

5. Review the final assessment, symptoms, and recommended precautions.
<img width="479" height="516" alt="image" src="https://github.com/user-attachments/assets/18c3e378-470a-4346-9c15-3ca62dce0d27" />

6. Click Restart Analysis if you wish to begin a new assessment.
<img width="772" height="131" alt="image" src="https://github.com/user-attachments/assets/671c20a2-8654-49ff-add1-12ce57ddbdf6" />

Disclaimer: 
This tool is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. 
Always consult a doctor if your health deteriorates.
<img width="772" height="119" alt="image" src="https://github.com/user-attachments/assets/230818b6-b5e3-4a38-bb1c-e050f2596ec5" />
