# Architecture and Implementation Plan

This project proposes a cloud-based architecture for collecting and summarizing patient-reported symptom data related to uterine fibroids. The purpose of the design is to demonstrate how cloud services can be integrated to support healthcare data ingestion, storage, and basic analytics. The system focuses on symptom monitoring and trend analysis rather than diagnosis or treatment.

## Service Mapping

The table below outlines the main cloud services used in this solution and their roles.

| Layer | Cloud Service | Role in Solution | Related Course Work |
|------|--------------|------------------|---------------------|
| Storage | Cloud Storage / Azure Blob Storage | Store raw symptom tracking data files | Cloud storage module |
| Compute | Virtual Machine or Container Service | Process symptom data and calculate summaries | Compute assignments |
| Database | Cloud SQL / Azure SQL | Store aggregated fibroid symptom metrics | SQL and database modules |
| Analytics | SQL queries or notebook environment | Generate symptom trends and summaries | Analytics module |

## Data Flow Description

The workflow begins when patients submit symptom tracking data related to uterine fibroids through a simple web interface or API. These submissions include synthetic or de-identified symptom severity scores, such as pain level, bleeding severity, and fatigue, along with timestamps.

Submitted data is first stored in cloud object storage to provide durable and centralized file management. A compute service then retrieves the stored files and performs basic validation to ensure values fall within expected ranges.

After validation, the compute service aggregates the data to produce daily or weekly summary metrics. Examples include average symptom severity scores, frequency of reported symptoms, and changes over time. These aggregated metrics are written to a managed SQL database designed to support efficient querying.

Clinicians or care coordinators can access summarized symptom trends through an API or simple reporting interface, allowing them to review patterns without needing to examine raw individual entries.

## Security and Governance Considerations

Security is addressed by managing credentials through environment variables or cloud-managed identity services rather than embedding secrets in application code. Role-based access control limits access to storage and database resources to authorized users only.

To minimize privacy risk, the system is designed to operate entirely on synthetic or de-identified data. No protected health information is included, and the architecture is intended for educational demonstration purposes rather than production clinical use.

## Cost and Operational Considerations

This architecture is designed to remain low-cost and suitable for a student environment. Storage costs are minimal due to the small size of symptom tracking files. Compute resources can be scheduled or run on demand to reduce unnecessary usage. Managed SQL services represent the primary ongoing cost but can be maintained within free-tier or low-cost limits.

Overall, the design balances simplicity, healthcare relevance, and cloud integration while supporting future enhancements such as dashboards, alerts, or integration with other health information systems.
