#!/bin/bash

# Install your Python environment
apt-get update -y
apt-get install -y python3.14-venv
python3.14 -m venv venv
source venv/bin/activate

# Clone the latest app directly onto the server
git clone https://github.com/your-github/your-repo.git
cd your-repo
pip install -r requirements.txt

# Connection string
export DATABASE_URL="postgresql://${db_user}:${db_pwd}@${db_host}:${db_port}"

# Run Uvicorn on port 80 bound to all interfaces
uvicorn main:app --host 0.0.0.0 --port ${app_port} > uvicorn.log 2>&1 &
