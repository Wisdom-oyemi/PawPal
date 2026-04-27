# Model Card: PawPal+

## 1. Model Name  

PawPal+ 

---

## 2. Intended Use  

This system is intended for users who want a clean and structured schedule for taking care of their pets.

---

## 3. How the Model Works  

The PawPal+ system takes in pet data and preferences from the user, builds a schedule with tasks to perform based on the input data, validates that the schedule is in accordance with a stipulated set of rules, and displays it for human review.

---

## 4. Data  

Describe the dataset the model uses.  

The PawPal+ system relies on user data such as the owner's profile, the pets under said profile, any created tasks, and specific constraints/preferences. 

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

The PawPal+ system may struggle with a non-trivial amount of tasks to be added or multiple schedules per one user (think a convoluted and meticulous pet owner being overprotective).
In addition, the system is biased towards the most popular pet types (cats and dogs), and would only handle the kinds of behaviors most associated with those pet types (e.g. walks or litter cleaning).

---

## 7. Evaluation  

Within the codebase there is a dedicated test suite to ensure the system works as intended, along with a newly-dedicated quality and reliability layer built specifically to ensure the consistency of the system's outputs with the given scheduler format.

---

## 8. Future Work  

Some potential upgrades to the PawPal+ system may include:

- Better ways to explain recommendations  
- Increased task handling/implementation for larger sizes 
- Cleaner/upgraded UI for more seamless performance on multiple devices 

---

## 9. Personal Reflection/AI Collaboration 
  
