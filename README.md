# OOP-ASSIGNMENT-BSEM-1101-SEM3 Abdulai Deam 905005560
# Vaccination Tracker - PROG211 OOP Project
**Domain:** Health | **Type:** Digital Public Good (DPG)

> Privacy by design: NO names, phone numbers or addresses stored.

## How To Run (Straight To The Work)

1. Run:
   python vaccination_tracker.py

2. DEMO will auto-run first:
   - Creates P001, P002
   - Adds BCG, Measles, Yellow Fever
   - Shows duplicate ID blocked
   - Shows update of dose

3. MENU appears:
   1. Add patient 2. Add vaccination 3. View all 4. Exit

## Code Meets All Tasks

**TASK 1 & 3: Classes**
- VaccineRecord: vaccine, dose_number, date_given | Methods: display_info() [instance], is_valid_vaccine() [static]
- Patient: patient_id, age_group, district, records | Methods: add_vaccination(), update_record(), display_info() [instance], get_total_patients() [class], is_valid_age_group() [static]
- Tuples: VACCINES, AGE_GROUPS (never change)
- Interaction: Patient HAS-MANY VaccineRecord

**TASK 2: Data Structure**
- patient_registry = {} Dictionary (patient_id -> Patient object)
- Functions add_patient(), display_patients()

**TASK 4: CRUD**
Create, Read, Update, Duplicate-check

## Requirements
Python 3.6+, no extra libraries
