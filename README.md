# OGA Database Archive

This repository contains the archived source code for the **Only Good Antibodies (OGA)** website and e‑learning module. It is intended as a reference implementation to reproduce our analyses and training materials. Sensitive keys and media have been stripped; follow the instructions below to configure and run locally.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Configuration](#configuration)  
   - [Database Setup](#database-setup)  
4. [Running the Application](#running-the-application)  
5. [Project Structure](#project-structure)  
6. [Contributing](#contributing)  
7. [License](#license)  
8. [Contact](#contact)  

---

## Project Overview

The OGA website provides:

- A browsable, searchable database of genes and associated antibodies  
- Detailed experiment records (WB, IP, ICC‑IF, FC)  
- User‑driven contact and resource pages  
- An integrated e‑learning “Academy” module with lessons, quizzes, and certificate generation  

This archive excludes production credentials, media uploads, and static build artifacts. It serves as a reproducible snapshot for research and development.

---

## Features

- **Django‑based backend** (Django 5.1)  
- **Core app**: gene/antibody database, search, filters, PDF citation  
- **Academy app**: lessons, sections, progress tracking, quizzes, certificates  
- **Authentication**: Django allauth + social (Google)  
- **Rich‑text**: CKEditor for lesson content  
- **Frontend**: Bootstrap 5 + custom CSS  

---

## Getting Started

### Prerequisites

- Python 3.10+  
- Git  
- [Node.js & npm](https://nodejs.org/) (for frontend asset builds, if customizing)  
- A Unix‑like shell (Linux, macOS, WSL)

### Installation

```bash
# 1. Clone this archive
git clone git@github.com:onlygoodantibodies/OGA_database_archive.git
cd OGA_database_archive

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install Python dependencies
pip install -r requirements.txt
