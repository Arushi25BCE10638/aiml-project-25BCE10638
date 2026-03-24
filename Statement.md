AI Medical Diagnosis Assistant

Overview:
The AI Medical Diagnosis Assistant is a rule-based expert system developed to address the growing issue of cyberchondria —anxiety caused by conflicting or extreme medical information found through traditional search engines. 
This application provides a structured, deterministic path for preliminary health assessments using an interactive Graphical User Interface (GUI).

Problem Description:
Individuals seeking medical clarity online often face a barrage of unstructured data. 
There is a critical need for a localized tool that:
1. Replaces overwhelming search results with a logical decision-tree.
2. Provides immediate, actionable safety precautions.
3. Maintains a calm, user-friendly environment to reduce stress during health-related queries.

Technical Objectives:
The project aims to demonstrate the application of Artificial Intelligence and Data Structures in a healthcare context:
1. Graph Theory Application: Representing medical triage logic as a Directed Acyclic Graph (DAG)
2. Algorithm Implementation: Utilizing Depth-First Search (DFS) to navigate from general symptoms (root nodes) to specific diagnoses (leaf nodes).
3. Event-Driven Architecture: Creating a responsive GUI using the Tkinter library that updates dynamically based on user interaction.

Functional Requirements:
To solve the problem effectively, the system implements the following:
1. User Personalization: A registration phase to capture user details for a tailored experience.
2. Knowledge Base: A structured database of diseases, symptoms, and specific precautions.
3. State Management: The ability to navigate through various symptom branches and reset the analysis at any time.
4. Safety Protocols: Mandatory medical disclaimers and specific health advice for every identified condition.

System Design:
1. Architecture: Modular Monolithic (Separation of Knowledge Base, Logic Controller, and View).
2. Logic: Rule-Based Expert System.
3. UI Design: Stress-reducing color palette (#FFF5E1 Cream / #FF6B6B Coral) with high-readability fonts for accessibility.
