# Health Facility Management System

A comprehensive Django REST API system for managing health facility operations including patient management, appointments, billing, pharmacy, and staff management.

## 🏥 Features

- **Patient Management**: Complete patient records with medical history
- **Staff Management**: Doctor profiles and specializations
- **Appointment Scheduling**: Book and manage patient appointments
- **Billing System**: Track payments and billing records
- **Pharmacy Management**: Medicine inventory and stock management
- **User Authentication**: JWT-based secure authentication
- **Admin Interface**: Django admin for easy data management

## 🛠️ Technology Stack

- **Backend**: Django 4.2+ with Django REST Framework
- **Authentication**: JWT (JSON Web Tokens) using djangorestframework-simplejwt
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **API Documentation**: Django REST Framework browsable API
- **CORS**: Enabled for frontend integration

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/alieutech2m-corp/Health-Facility.git
cd Health-Facility/healthFacility
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root (optional):

```bash
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## 📚 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | User registration |
| POST | `/api/auth/token/` | Login (obtain JWT tokens) |
| POST | `/api/auth/token/refresh/` | Refresh JWT token |

### Core API Endpoints

| Resource | Endpoint | Methods | Description |
|----------|----------|---------|-------------|
| Patients | `/api/patients/` | GET, POST, PUT, DELETE | Manage patient records |
| Doctors | `/api/doctors/` | GET, POST, PUT, DELETE | Manage doctor profiles |
| Appointments | `/api/appointments/` | GET, POST, PUT, DELETE | Manage appointments |
| Medicines | `/api/medicines/` | GET, POST, PUT, DELETE | Manage pharmacy inventory |
| Bills | `/api/bills/` | GET, POST, PUT, DELETE | Manage billing records |

### Authentication

Include JWT token in request headers:

```bash
Authorization: Bearer <your-access-token>
```

## 🏗️ Project Structure

```
healthFacility/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── healthFacility/          # Main project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/                # User authentication
├── patients/                # Patient management
├── staff/                   # Doctor/staff management
├── appointments/            # Appointment scheduling
├── billing/                 # Billing system
└── pharmacy/               # Medicine inventory
```

## 🔧 API Usage Examples

### 1. User Registration

```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepassword123",
    "password2": "securepassword123",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

### 2. Login

```bash
curl -X POST http://localhost:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepassword123"
  }'
```

### 3. Create Patient

```bash
curl -X POST http://localhost:8000/api/patients/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your-access-token>" \
  -d '{
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane@example.com",
    "phone": "123-456-7890",
    "date_of_birth": "1990-01-15",
    "address": "123 Main St, City, State"
  }'
```

### 4. Schedule Appointment

```bash
curl -X POST http://localhost:8000/api/appointments/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your-access-token>" \
  -d '{
    "patient": 1,
    "staff": 1,
    "appointment_date": "2025-11-15T10:00:00Z",
    "reason": "Regular checkup",
    "status": "scheduled"
  }'
```

## 📊 Database Models

### Patient Model
- Personal information (name, email, phone, address)
- Date of birth
- Medical records relationship

### Doctor Model
- Professional information (name, specialty, email)
- Hire date and active status

### Appointment Model
- Patient and doctor relationships
- Date/time scheduling
- Status tracking (scheduled, completed, canceled)

### Medicine Model
- Inventory management
- Stock tracking
- Pricing and expiration dates

### Billing Record Model
- Patient billing information
- Payment tracking
- Amount and description

## 🔒 Security Features

- JWT-based authentication
- Password validation
- CORS protection
- Secure headers middleware
- User permission controls

## 🛡️ Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DJANGO_SECRET_KEY` | Django secret key | Auto-generated |
| `DJANGO_DEBUG` | Debug mode | True |
| `DJANGO_ALLOWED_HOSTS` | Allowed hosts | localhost,127.0.0.1 |

## 🚀 Deployment

### Production Settings

1. Set `DEBUG = False`
2. Configure proper `SECRET_KEY`
3. Set up production database (PostgreSQL)
4. Configure static files serving
5. Set up proper `ALLOWED_HOSTS`

### Docker Deployment (Optional)

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 🧪 Testing

Run tests:

```bash
python manage.py test
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Team

- **Developer**: [Your Name]
- **Organization**: alieutech2m-corp

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Contact: [your-email@example.com]

## 🔄 Changelog

### v1.0.0
- Initial release
- Basic CRUD operations for all modules
- JWT authentication
- Admin interface
- API documentation

---

**Note**: This is a development version. Please ensure proper security configurations before deploying to production.
