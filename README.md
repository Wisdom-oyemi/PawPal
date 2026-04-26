# PawPal+

This is **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Summary

If you're a busy pet owner that needs help staying consistent with caring for your pet, we have the solution for you! The PawPal+ assistant can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan
It also comes with increased internal reliability checks to ensure the quality of the program!


### Architecture Overview
The user inputs data into the system, such as pet info and constraints. This data is funneled into the scheduler engine, which is the backbone of the system's operation; the engine subsequently produces a plan output that mirrors the preferences of the user, with added reasoning based on the data points. The newly-added quality and reliability layer "stress-tests" the robustness of the plan to ensure the engine is behaving in the ideal manner, combining an automated test suite with a separate evaluator and regression gate that rejects bad plans. Ultimately, the plan is then suggested for user approval, which can then influence subsequent task edits.


## Sample Interactions
<a href="/course_images/ai110/demo_screenshot.png" target="_blank"><img src='/course_images/ai110/demo_screenshot.png' title='PawPal App' width='' alt='PawPal App' class='center-block' /></a>.


## Set-Up

### Instructions

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```


### Design Decisions:


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

### Testing Summary


## Reflection
