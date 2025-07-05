<<<<<<< HEAD

# GenAI-Integrated-Portal

This project is an integrated platform to orchestrate the software development life cycle using GenAI tools:
- Windsurf (Requirement generation from Figma)
- Builder.io (UI component generation)
- Cursor IDE + GitHub Copilot (Backend code scaffolding and test generation)
- Azure DevOps (CI/CD pipelines)

## Setup Instructions

1. Setup backend:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

2. Setup frontend:
```bash
cd frontend
npm install
npm start
```

3. Configure scripts in /scripts with your API keys and project details.
4. Configure Azure DevOps pipeline using provided YAML file in /pipelines.
=======
# GenAIDevPortal
GenAIDevPortal
>>>>>>> c8963849a41d9a4ec13f54df6257cae82e81978d
