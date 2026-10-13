"""
Vaccination Tracker - PROG211 Object-Oriented Programming 1
Domain: Health

A small, open-source Digital Public Good (DPG) for tracking vaccinations.
Privacy by design: NO names, phone numbers or addresses are stored.
Each person is represented only by an anonymous ID, an age group and a district.
"""

from datetime import date

# ---------------------------------------------------------------------------
# Tuples (optional bonus): fixed values that should never change
# ---------------------------------------------------------------------------
VACCINES = ("BCG", "OPV", "Pentavalent", "Measles", "Yellow Fever", "COVID-19")
AGE_GROUPS = ("0-5", "6-17", "18-59", "60+")


# ---------------------------------------------------------------------------
# TASK 1 & 3: Classes, attributes, instance / class / static methods
# ---------------------------------------------------------------------------
class VaccineRecord:
    """One vaccination event (e.g. Measles, dose 1, on a given date)."""

    def __init__(self, vaccine, dose_number, date_given=None):
        if not VaccineRecord.is_valid_vaccine(vaccine):
            raise ValueError(f"Unknown vaccine: {vaccine}. Choose from {VACCINES}")
        self.vaccine = vaccine
        self.dose_number = dose_number
        self.date_given = date_given or date.today()

    @staticmethod
    def is_valid_vaccine(name):
        """Static method: needs no object or class data, just checks a value."""
        return name in VACCINES

    def display_info(self):
        """Instance method: show this record."""
        print(f"    - {self.vaccine} | dose {self.dose_number} | {self.date_given}")


class Patient:
    """An anonymous patient. Holds a list of VaccineRecord objects."""

    total_patients = 0  # class attribute shared by all patients

    def __init__(self, patient_id, age_group, district):
        if not Patient.is_valid_age_group(age_group):
            raise ValueError(f"Invalid age group: {age_group}. Choose from {AGE_GROUPS}")
        self.patient_id = patient_id
        self.age_group = age_group
        self.district = district
        self.records = []  # interaction: Patient HAS-MANY VaccineRecord objects
        Patient.total_patients += 1

    # ----- instance methods -----
    def add_vaccination(self, vaccine, dose_number, date_given=None):
        """Create a VaccineRecord object and attach it to this patient."""
        record = VaccineRecord(vaccine, dose_number, date_given)
        self.records.append(record)
        return record

    def update_record(self, vaccine, new_dose_number):
        """Update the dose number of an existing vaccination. Returns True if found."""
        for record in self.records:
            if record.vaccine == vaccine:
                record.dose_number = new_dose_number
                record.date_given = date.today()
                return True
        return False

    def display_info(self):
        print(f"Patient ID: {self.patient_id} | Age group: {self.age_group} "
              f"| District: {self.district}")
        if not self.records:
            print("    (no vaccinations recorded)")
        for record in self.records:
            record.display_info()

    # ----- class method -----
    @classmethod
    def get_total_patients(cls):
        """Class method: works with class data, not one specific patient."""
        return cls.total_patients

    # ----- static method -----
    @staticmethod
    def is_valid_age_group(age_group):
        return age_group in AGE_GROUPS


# ---------------------------------------------------------------------------
# TASK 2: ONE data structure - a dictionary (patient_id -> Patient object)
# ---------------------------------------------------------------------------
def add_patient(registry, patient):
    """Add a Patient to the registry dictionary, using the ID as the key."""
    if patient.patient_id in registry:
        print(f"ID {patient.patient_id} already exists. Record not added.")
        return False
    registry[patient.patient_id] = patient
    return True


def display_patients(registry):
    """Loop through the dictionary and display every patient."""
    if not registry:
        print("No patients in the registry.")
        return
    print(f"\n--- Registry ({Patient.get_total_patients()} patients) ---")
    for patient in registry.values():
        patient.display_info()


# ---------------------------------------------------------------------------
# Demo + simple menu
# ---------------------------------------------------------------------------
def run_demo(registry):
    """Shows object creation and interaction between objects."""
    p1 = Patient("P001", "0-5", "Western Area Urban")
    p1.add_vaccination("BCG", 1)
    p1.add_vaccination("Measles", 1)

    p2 = Patient("P002", "18-59", "Bo")
    p2.add_vaccination("Yellow Fever", 1)

    add_patient(registry, p1)
    add_patient(registry, p2)
    add_patient(registry, p1)  # duplicate ID -> rejected

    p1.update_record("Measles", 2)  # update an existing record
    display_patients(registry)


def run_menu(registry):
    """Text menu so a user can enter their own data."""
    while True:
        print("\n1. Add patient  2. Add vaccination  3. View all  4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            pid = input("Anonymous ID (e.g. P003): ").strip()
            age = input(f"Age group {AGE_GROUPS}: ").strip()
            district = input("District: ").strip()
            try:
                add_patient(registry, Patient(pid, age, district))
            except ValueError as error:
                print("Error:", error)
        elif choice == "2":
            pid = input("Patient ID: ").strip()
            if pid not in registry:
                print("Patient not found.")
                continue
            vaccine = input(f"Vaccine {VACCINES}: ").strip()
            try:
                dose = int(input("Dose number: "))
                registry[pid].add_vaccination(vaccine, dose)
                print("Vaccination recorded.")
            except ValueError as error:
                print("Error:", error)
        elif choice == "3":
            display_patients(registry)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    patient_registry = {}  # the dictionary data structure
    run_demo(patient_registry)
    run_menu(patient_registry)