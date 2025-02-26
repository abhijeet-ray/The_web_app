# The_web_app

Installetion - 

Below is a summary of the installation process and how to download the required dependencies based on the provided README instructions:

Backend Setup:

• Prerequisites:
 – Python 3.7 or later is required.

• Create a Virtual Environment:
 Run the following commands in your project directory:   - On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate
  - On Windows:
   python -m venv venv
   venv\Scripts\activate

• Install Dependencies:
 The backend uses FastAPI, Uvicorn, and Pydantic. Install them using pip:   pip install fastapi uvicorn

• Run the Backend Server:
 Start the FastAPI server with:   uvicorn main:app --reload
 This will launch the server (by default on http://127.0.0.1:8000).

Frontend Setup:

• No Additional Dependencies:
 The frontend consists solely of HTML, CSS, and JavaScript. No extra installation is required.

• Launching the Frontend:
 Simply open index.html in your browser. Alternatively, serve the files via a static file server if needed.
 python -m http.server 8001

With these steps, your integrated system (frontend connecting to the backend API) will be fully operational.
