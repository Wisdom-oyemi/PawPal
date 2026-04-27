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

The system works best with a limited, straightforward dataset of 2-3 pets and a small variety of tasks. It is also good at verifying whether the created schedule follows the conventions that the internal program stipulates.

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
I collaborated with GitHub Copilot on this project, and it helped me in multiple ways: make sense of the codebase at hand, evaluate what path to take towards implementing the added reliability layer, and test the strength of the schedules provided. Copilot made the correct observation of the implemented reliability system being strong enough to fulfill requirements I outlined (based on the assignment's guidelines); however, it made a flawed multi-implementation of the Mermaid diagram I requested in a slide-architecture format, which I had to override and specifically request in Mermaid format. 
  
