# Upskill-club

A Django-based project designed to serve course-related APIs using Django Rest Framework (DRF). It supports a set of APIs that expose course categories, courses, sessions, and concepts, with all course data populated by the Django admin panel.


## Features

- **Course Management:** Define course categories, courses, and sessions.
- **API Powered by DRF:** Expose data through REST APIs with rate limiting.
- **File Upload Support:** Upload and serve media files such as thumbnails for courses and sessions.
- **Admin Panel:** Content creation and management is handled through the Django admin interface.

## Environment Variables

Make sure to set the following environment variables in your `.env` file:

- `SECRET_KEY`: Django secret key for your application.
- `ADMIN_URL`: Custom URL for accessing the Django admin panel.
- `DB_ENGINE`: Set to `mysql` so Django connects to the managed MySQL instance.
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`: Credentials for your MySQL database.
- `DB_HOST` *(optional)*: Defaults to `127.0.0.1`. Use the host provided by your MySQL provider.
- `DB_PORT` *(optional)*: Defaults to `3306`.
  
## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   ```
2. **Create Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **Run Migrations**
```bash
python manage.py migrate
```
5. **Create Superuser**
```bash
python manage.py createsuperuser
```
6. **Run the Development Serve**
```bash
python manage.py runserver
```
### Access Admin Panel

Navigate to the admin URL (set via `ADMIN_URL` in your `.env` file or use the default `/admin/`).

## API Endpoints

- **Categories:** `/api/categories/`
- **Courses:** `/api/courses/`
- **Sessions:** `/api/sessions/`
- **Concepts:** `/api/concepts/`

## Configuration

### CORS Setup

Allow CORS requests from your frontend (e.g., GitHub Pages) by setting the allowed origins in `CORS_ALLOWED_ORIGINS` in `settings.py`.

```python
CORS_ALLOWED_ORIGINS = [
    "https://youralloweddomain.com",
]
```

### Rate Limiting

Anonymous users are limited to 1000 requests per minute, while authenticated users are limited to 100 requests per day.

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1000/min',
        'user': '100/day'
    }
}
```

### Media Files

Uploaded media files are stored in the `media/` directory. Make sure the `MEDIA_ROOT` and `MEDIA_URL` are configured correctly in `settings.py`.

```python
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
