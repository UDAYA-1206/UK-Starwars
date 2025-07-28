# 🌌 Star Wars QA Automation Project

This project automates testing of a React + Redux-based Star Wars application using **Robot Framework** and **Python**. 
It includes both **API** and **UI-based test validations** leveraging the [SWAPI](https://swapi.dev) (Star Wars API). Tests are organized using Robot Framework and custom Python libraries.

---
## 🚀 Getting Started

### 📥 Clone the Repository

## 📁 Folder Structure

```text
UK-Starwars/
├── lib/                      # Python libraries
│   ├── APIKeywords.py        # API-related keyword implementations
│   ├── UIKeywords.py         # UI-related keyword implementations
│   ├── LoggerUtil.py         # Custom logger utilities
│   └── swapi_client.py       # Handles SWAPI HTTP interactions
│
├── tests/                    # Robot tests and test data
│   ├── tests.robot           # All test cases (UI & API)
│   └── test_data.yaml        # Input variables and data
│
├── .github/
│   └── workflows/
│       └── run-tests.yml     # GitHub Actions CI configuration
│
├── requirements.txt          # Python package dependencies
└── README.md                 # Project documentation


## 🔧 Requirements

Before running the tests, install the required tools:

1. **Python 3.10+**
2. **pip** package manager

### Install Dependencies

pip install -r requirements.txt

**▶️ How to Run Tests**

Change directory to the project root and run:

✅ Run All Test Cases

robot tests/starwars_tests.robot

✅ Run UI Tests Only

robot --include "UI" tests/starwars_tests.robot

✅ Run a Specific Test Case (e.g. Testcase 3)

robot --include "Testcase 3" tests/starwars_tests.robot


✅ Output Reports
After running, reports will be available:

log.html

report.html

output.xml
