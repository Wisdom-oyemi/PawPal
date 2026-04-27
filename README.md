# PawPal+

This is **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Summary

If you're a busy pet owner that needs help staying consistent with caring for your pet, we have the solution for you! The PawPal+ assistant can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan
It also comes with increased internal reliability checks to ensure the quality of the system!


### Architecture Overview
The user inputs data into the system, such as pet info and constraints. This data is funneled into the scheduler engine, which is the backbone of the system's operation; the engine subsequently produces a plan output that mirrors the preferences of the user, with added reasoning based on the data points. The newly-added quality and reliability layer "stress-tests" the robustness of the plan to ensure the engine is behaving in the ideal manner, combining an automated test suite with a separate evaluator and regression gate that rejects bad plans. Ultimately, the plan is then suggested for user approval, which can then influence subsequent task edits.


## Sample Interactions
<a href="/course_images/ai110/demo_screenshot.png" target="_blank"><img src='/course_images/ai110/demo_screenshot.png' title='PawPal App' width='' alt='PawPal App' class='center-block' /></a>.
<a href="/course_images/ai110/2nd_screenshot.png" target="_blank"><img src='/course_images/ai110/2nd_screenshot.png' title='PawPal App' width='' alt='PawPal App' class='center-block' /></a>.
<a href="/course_images/ai110/3rd_screenshot.png" target="_blank"><img src='/course_images/ai110/3rd_screenshot.png' title='PawPal App' width='' alt='PawPal App' class='center-block' /></a>.

## Video Walkthrough


## Set-Up

### Instructions

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```


### Design Decisions
This system was designed to both generate and evaluate schedules based on data given by the user. I intentionally made the call to strengthen the evaluation suite (as opposed to introducing more generative AI-powered features) because the very spine of the system itself is generative. Therefore, ensuring the plans created are correct will increase the system's efficiency.


## Testing PawPal+

### Setup

```bash
python -m pytest
```

The tests in the PawPal+ test suite cover the following behaviors:
- Task count increase
- Marking a task complete
- Chronological order of display
- Task daily reoccurrence
- Time conflicts for tasks
- Reliability scoring for clean schedules
- Reliability warnings for conflicting schedules

### Testing Summary
PawPal+ now includes a separate reliability layer on top of the scheduler. The app and CLI both show a reliability score, rule checks, and warnings so the user can review the plan before acting on it.


## Reflection
While working on this project, I came to a definitive understanding of how AI in its many forms can boost/aid problem-solving. This particular project aimed to solve the rather uncomplicated yet non-trivial issue of scheduling things for a pet to do, and the implementation of an automated system that generates schedules based on tasks saves a user a lot of time and mental bandwidth. The development of the codebase was made in conjunction with GitHub Copilot, with which I made key system updates/changes to polish the system's strengths and lessen its flaws. 
