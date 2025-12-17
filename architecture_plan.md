# Architecture and Implementation Plan

This project proposes a cloud-based architecture for collecting and summarizing patient-reported symptom data related to uterine fibroids. The purpose of the design is to demonstrate how cloud services can be integrated to support healthcare data ingestion, storage, and basic analytics. The system focuses on symptom monitoring and trend analysis rather than diagnosis or treatment.

## Service Mapping

The table below outlines the main cloud services used in this solution and their roles.

| Layer | Cloud Service | Role in Solution | Related Course Work |
|------|--------------|------------------|---------------------|
| Storage | Cloud Storage / Azure Blob Storage | Store raw symptom tracking data files |Modules 5–6 or Assignment 4 |
| Compute | Virtual Machine or Container Service | Process symptom data and calculate summaries | Modules 1–2 (Cloud Foundations & Virtual Machines) & Modules 3–4 (Containers) |
| Database | Cloud SQL / Azure SQL | Store aggregated fibroid symptom metrics |  Modules 5–6 (Databases & SQL) & Assignment 3 |
| Analytics | SQL queries or notebook environment | Generate symptom trends and summaries | Modules 7–9 (Analytics and Data Processing) |

## Data Flow Description

The workflow starts when patients enter symptom tracking information related to uterine fibroids through a basic web interface or API. The submitted data consists of synthetic or de-identified symptom severity scores, such as pain, bleeding, and fatigue, along with the date and time of each entry.

Once received, the data is stored in cloud object storage, which provides a centralized and durable location for raw symptom files. A compute service then accesses these files and performs basic checks to confirm that the data is complete and within expected value ranges.

After validation, the compute service processes the data to generate daily or weekly summary metrics. These summaries may include average symptom severity, how often symptoms are reported, and changes in symptoms over time. The resulting aggregated data is saved in a managed SQL database optimized for querying and analysis.

Clinicians or care coordinators can view these summarized trends through an API or simple reporting tool, making it easier to identify patterns without reviewing individual symptom entries.

## Security and Governance Considerations

Security is addressed by managing credentials through environment variables or cloud-managed identity services rather than embedding secrets in application code. Role-based access control limits access to storage and database resources to authorized users only.

To minimize privacy risk, the system is designed to operate entirely on synthetic or de-identified data. No protected health information is included, and the architecture is intended for educational demonstration purposes rather than production clinical use.

## Cost and Operational Considerations

This architecture is designed to remain low-cost and suitable for a student environment. Storage costs are minimal due to the small size of symptom tracking files. Compute resources can be scheduled or run on demand to reduce unnecessary usage. Managed SQL services represent the primary ongoing cost but can be maintained within free-tier or low-cost limits.

