
# CareerTrack-CLI: Automated Job Application & Deadline Monitor

An engineered, lightweight Command Line Interface (CLI) application built in pure Python to manage, filter, and audit job application pipelines. This tool solves the operational chaos of job tracking by replacing heavy spreadsheets with a fast, zero-dependency terminal dashboard that evaluates upcoming deadlines and follow-up targets against the host machine's system time.

## 🧠 Architectural Decisions & Technical Highlights

When designing this application, the core philosophy was **maximum performance with zero external overhead**. 

*   **Zero-Dependency Architecture:** Built exclusively using the Python Standard Library (`csv`, `datetime`). This guarantees cross-platform compatibility, instant deployment, and zero vulnerability/patching requirements from third-party packages.
*   **Memory-Efficient I/O:** Leveraged `csv.DictReader` and `csv.DictWriter` to abstract low-level file manipulations into dynamic Python dictionaries. This allows structured row-by-row parsing without loading monolithic datasets into memory.
*   **Dynamic Time Serialization:** Utilized `datetime.strptime` objects to parse static ISO-8601 string inputs into mathematical date structures, enabling dynamic timezone-agnostic date logic (e.g., calculation of exact days remaining until interview deadlines).

## ✨ Core Functionalities

*   **Daily Action Reminders:** Automatically flags active applications that require follow-up if the target date is `<= today`.
*   **Urgent Deadline System:** Looks ahead 3 days to catch and surface impending submission closures or technical interview deadlines.
*   **Local Persistence Engine:** Implements safe, non-destructive file appending (`'a'` mode) to ensure data persistence across terminal sessions.
*   **Input Validation Guardrails:** Gracefully handles malformed or missing string dates to prevent terminal execution failure.

## 📊 Data Architecture & Schema

The application handles persistence through a structured flat-file database (`jobs.csv`). The data is mapped across the following schema:

| Column Name | Data Type | Constraint / Format | Description |
| :--- | :--- | :--- | :--- |
| **Job Title** | String | Non-Null | Name of the role applied for |
| **Company** | String | Non-Null | Target organization |
| **Application Date** | String | `YYYY-MM-DD` | Defaults to system date if blank |
| **Status** | String | Choice (`Applied`, `Interviewing`, etc.) | State machine tracker |
| **Deadline** | String | `YYYY-MM-DD` | Target closure date |
| **Follow-up Date** | String | `YYYY-MM-DD` | Automated reminder trigger point |
| **Notes** | String | Nullable | Contextual details (referrals, links) |

## 🚀 Installation & Local Deployment

1. **Clone the repository:**
```bash
git clone https://github.com/biikashsubedi/CareerTrack-CLI-Python.git
```


2. **Initialize the local data environment:**
The application auto-generates the database on its initial write. However, a `jobs_sample.csv` is provided to demonstrate functionality.
3. **Execute the script:**
```bash
python main.py
```



## 📈 Future Scalability Roadmap
*   [ ] **Analytics Dashboard:** Implement logic to calculate conversion rates (e.g., Application-to-Interview ratio).
*   [ ] **Cross-Platform Exports:** Add a module to export reports into JSON or Markdown formats.
*   [ ] **Automatic Backups:** Script a routine to automatically back up the local database to an archive folder.

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.
