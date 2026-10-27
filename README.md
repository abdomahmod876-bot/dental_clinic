# Dental Clinic Management

Dental Clinic Management is a custom Odoo module designed to manage patients, visits, treatment notes, and dental imaging records inside a dental clinic.

This project is built as an Odoo application and provides a complete workflow for tracking patient information and treatment history.

## Overview

The system allows the clinic to:
- Register and manage patient records
- Track patient personal information (name, birthdate, sex, phone, email, address)
- Categorize patients by city, race, and class
- Assign treating and referring doctors
- Monitor patient treatment stage
- Record patient visits and treatment lines
- Manage clinical images and X-ray categories
- View relevant patient data through a customized Odoo interface

## Main Features

### 1. Patient Management
- Add new patient records
- Auto-generate patient IDs
- Validate patient number is greater than zero
- Store personal details such as:
  - First name
  - Middle name / initials
  - Last name
  - Birthdate and age
  - Sex
  - Phone and email
  - City and address
  - Race
  - Class
  - Treating doctor
  - Referring doctor

### 2. Patient Stages
Each patient can be tracked by a current stage, such as:
- Installation
- Follow-up
- Removal

### 3. Visits and Treatment Tracking
The system supports:
- Multiple visits per patient
- Visit date tracking
- Treating doctor assignment
- Notes for each visit
- Treatment lines with:
  - Stage / diagnosis
  - Procedure
  - Notes

### 4. Dental Imaging Management
Patients can have many images organized by categories, including:
- Start
- Progress
- Retention
- Models
- PAN
- CEPH
- Occl
- Various
- Hygiene
- Library

This makes it easy to review patient progress visually over time.

### 5. Dashboard and Search
The Odoo views include:
- List view for all patients
- Search filters by name, phone, email, sex, class, city, and doctor
- Grouping by class, city, and treating doctor
- Form view with patient details and image gallery sections

## Project Structure

```text
dental_clinic/
├── __init__.py
├── __manifest__.py
├── data/
│   └── patient_sequence.xml
├── models/
│   ├── __init__.py
│   ├── patient.py
│   ├── patient_city.py
│   ├── patient_image.py
│   ├── patient_race.py
│   ├── patient_xray_date.py
│   ├── doctor_patient.py
│   └── visit.py
├── security/
│   ├── ir.model.access.csv
│   └── security.xml
├── static/
│   └── src/
│       └── scss/
│           └── dental.scss
└── views/
    └── patient_views.xml
```

## Key Files

### __manifest__.py
Defines the module metadata, dependencies, data files, and frontend assets.

### models/patient.py
Contains the main patient model with fields, validation rules, age calculations, name generation, and sequence logic.

### models/visit.py
Defines patient visits and treatment line records.

### views/patient_views.xml
Contains the custom Odoo views for:
- patient list
- patient search
- patient form
- image management
- menu and action definitions

## Dependencies

This module depends on:
- Odoo base
- mail
- web

## Installation

1. Place the project in your Odoo addons path.
2. Update the apps list.
3. Install the module named Dental Clinic Management.
4. Configure the patient sequence if needed.

## Use Case

This module is useful for:
- Dental clinics
- Orthodontic centers
- Private dental practices
- Clinic management systems requiring patient history and treatment tracking

## Summary

The project is a custom Odoo clinic management solution focused on dental patient records, treatment monitoring, doctor assignments, and visual case tracking through patient images and X-rays.

It is designed to give clinics a centralized system for maintaining patient histories and treatment progress in a simple and organized interface.
