# File Compare Platform Backend

A FastAPI-based backend service for the File Compare Platform that provides APIs for file comparison, user management, and authentication.

## Features

- File comparison and analysis
- User authentication and authorization
- Role-based access control
- Audit logging
- RESTful API endpoints
- Docker support
- CORS configuration for frontend integration

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Docker

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Docker (optional)

### Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/manjuofficalz/file-compare-backend.git
cd file-compare-backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at http://localhost:8000

### Docker Setup

1. Build the Docker image:
```bash
docker build -t file-compare-backend .
```

2. Run the container:
```bash
docker run -p 8000:8000 file-compare-backend
```

## API Documentation

Once the server is running, you can access:
- Interactive API documentation (Swagger UI): http://localhost:8000/docs
- Alternative API documentation (ReDoc): http://localhost:8000/redoc

## Project Structure

```
file-compare-platform-backend/
├── main.py            # FastAPI application and router definitions
├── requirements.txt   # Python dependencies
├── Dockerfile        # Docker configuration
└── .gitignore       # Git ignore rules
```

## Environment Variables

The following environment variables can be configured:

- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
