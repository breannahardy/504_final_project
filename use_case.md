# Symptom Monitoring for Patients with Uterine Fibroids

## Overview
Uterine fibroids are a common condition that can cause symptoms such as pain, heavy bleeding, and fatigue. Patients often track these symptoms over time, but the information may be recorded inconsistently or reviewed manually. This project designs a cloud-based system that collects symptom tracking data and produces simple summaries to support clinical monitoring and follow-up.

The goal of this system is to demonstrate how cloud services can be used to organize and analyze healthcare-related data, rather than to diagnose or treat medical conditions.

## Problem Statement
Patients with uterine fibroids may experience changes in symptoms over time, but raw daily entries can be difficult for clinicians to review. Without summarized trends, it can be challenging to identify whether symptoms are improving, worsening, or remaining stable. This project addresses this issue by designing a system that aggregates symptom data into easy-to-review summaries.

## Users and Stakeholders
The primary users are clinicians and care coordinators who monitor patient-reported symptoms. Patients are indirect stakeholders, as improved tracking and review may support better communication during clinical visits.

## Data Sources
The system uses synthetic or de-identified symptom tracking data collected through periodic patient self-reports. Data may include symptom severity scores, frequency of symptoms, and timestamps. No protected health information is included.

## System Workflow
1. Patients submit symptom tracking data through a simple web interface.
2. Data is stored in cloud object storage.
3. A compute service processes the data and validates entries.
4. Daily or weekly summary metrics are calculated.
5. Aggregated data is stored in a managed SQL database.
6. Summary trends are made available for clinician review.

## Value of the Cloud-Based Approach
Cloud services allow symptom data to be stored securely and processed automatically. This approach supports scalability, reduces manual review, and allows for future enhancements such as dashboards or
