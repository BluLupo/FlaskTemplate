# Flask Application

A simple Flask web application that serves content on `localhost/app`.

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## 🚀 Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/BluLupo/FlaskTemplate.git
cd FlaskTemplate
```

### 2. Create a virtual environment (recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the application
Make sure the `config.py` file is present in the project root with the necessary configurations.

### 5. Start the application
```bash
python app.py
```

## 🌐 Accessing the Application

Once the application is running, it will be accessible at:
```
http://localhost:5000/app
```

## 📁 Project Structure

```
├── app.py              # Main application file
├── config.py           # Application configuration
├── requirements.txt    # Python dependencies
├── routes/
│   └── home.py        # Home page routes
└── README.md          # This file
```

## ⚙️ Configuration

The application uses a `config.py` file to manage configurations. Make sure it contains at least:

```python
class Config:
    APP_DEBUG = True           # Debug mode
    APP_HOST = 'localhost'     # Application host
    APP_PORT = 5000           # Application port
    URL_PREFIX = '/app'       # URL prefix
```

## 🛠️ Development

To run the application in debug mode:
1. Make sure `APP_DEBUG = True` in `config.py`
2. Start with `python app.py`
3. Code changes will be automatically reloaded

## 📝 Notes

- The application is configured to work on `localhost:5000/app`
- Debug mode is enabled by default (configurable in `config.py`)
- Uses Blueprint to organize routes