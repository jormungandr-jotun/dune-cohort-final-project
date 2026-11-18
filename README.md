# PlugListing — Property Listing Platform

**Live demo:** [https://YOUR-RENDER-SERVICE.onrender.com](https://YOUR-RENDER-SERVICE.onrender.com)  
**Deployment note:** Replace this placeholder with the actual public HTTPS URL after deploying the project to Render. This source package has not been deployed, so no live URL is being claimed.

PlugListing is a property discovery and listing application built with Django. Property owners can publish and manage listings; visitors can browse and search available homes, inspect property details, and registered users can send inquiries and save properties.

## Features

- Public home page with latest available properties.
- Property search by title, city, or address.
- Property detail pages with image, location, price, features, and owner details.
- User registration, login, and logout.
- Authenticated owner dashboard.
- Full property CRUD with ownership checks and staff override.
- Image upload for property cover photos and a related gallery-image model.
- Authenticated inquiries and saved-property functionality.
- Staff-only inquiry overview.
- Django admin with searchable/filterable property and inquiry records.
- Django REST Framework API for listing, retrieving, creating, updating, and deleting properties.
- Token and session authentication support for API requests.
- WhiteNoise static-file serving for production.
- PostgreSQL support through `DATABASE_URL`; local SQLite is used only when no database URL is configured.

## Tech stack

- Python 3.11+
- Django 5.1+
- Django REST Framework
- PostgreSQL (production) / SQLite (local development fallback)
- DRF Token Authentication and Session Authentication
- WhiteNoise
- Gunicorn
- Pillow
- Render

## Project structure

```text
dune-cohort-final-project/
└── pluglisting/
    ├── manage.py
    ├── Procfile
    ├── requirements.txt
    ├── .env.example
    ├── project_config/
    ├── accounts/
    ├── listings/
    ├── templates/
    ├── static/css/main.css
    ├── api_docs.md
    ├── postman_collection.json
    └── screenshots/
```

## Local setup

1. Clone the repository and enter the project directory:

   ```bash
   git clone https://github.com/YOUR-GITHUB-USERNAME/dune-cohort-final-project.git
   cd dune-cohort-final-project/pluglisting
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # macOS/Linux
   source .venv/bin/activate
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create your local environment file:

   ```bash
   cp .env.example .env
   ```

   Set a unique `SECRET_KEY`. For local development, `DEBUG=True` is acceptable. Leave `DATABASE_URL` blank to use the local SQLite database, or provide a PostgreSQL URL.

5. Apply migrations and create an administrator:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/`.

## Environment variables

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Django cryptographic signing key; use a strong secret in production. |
| `DEBUG` | Enables/disables debug mode. Must be `False` on Render. |
| `DATABASE_URL` | PostgreSQL connection URL on Render. |
| `ALLOWED_HOSTS` | Comma-separated allowed hostnames. |
| `CSRF_TRUSTED_ORIGINS` | Comma-separated trusted HTTPS origins, including scheme. |

`.env.example` contains variable names with blank values. Never commit your real `.env` file.

## API documentation

See [api_docs.md](api_docs.md). The included [Postman collection](postman_collection.json) covers list, detail, create, update, and delete requests. Import it into Postman and set its `base_url`, `property_id`, and `token` variables for your deployment.

| Method | URL | Auth required | Success |
|---|---|---:|---|
| GET | `/api/properties/` | No | 200 |
| POST | `/api/properties/` | Yes | 201 |
| GET | `/api/properties/{id}/` | No | 200 |
| PUT/PATCH | `/api/properties/{id}/update/` | Yes | 200 |
| DELETE | `/api/properties/{id}/delete/` | Yes | 204 |

Invalid input returns 400; missing or inaccessible records return 404.

## Render deployment

1. Push this repository to a public GitHub repository named `dune-cohort-final-project`.
2. In Render, create a managed PostgreSQL database and copy its **internal** connection URL.
3. Create a new **Web Service** connected to the GitHub repository. Set the root directory to `pluglisting`.
4. Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
5. Start command: `gunicorn project_config.wsgi:application`
6. Add environment variables:
   - `SECRET_KEY`: generated production secret
   - `DEBUG`: `False`
   - `DATABASE_URL`: Render PostgreSQL internal URL
   - `ALLOWED_HOSTS`: your Render hostname, e.g. `your-service.onrender.com`
   - `CSRF_TRUSTED_ORIGINS`: `https://your-service.onrender.com`
7. Deploy, then create a superuser from the Render shell using `python manage.py createsuperuser`.
8. Open the HTTPS service URL, test registration and listing workflows, and update the Live demo URL at the top of this README.

The application settings use PostgreSQL whenever `DATABASE_URL` is set and enable secure cookies and HTTPS proxy handling when `DEBUG=False`.

## Screenshots

Place real browser and Postman screenshots in `screenshots/` and embed them here before submission:

- `screenshots/homepage.png` — home page
- `screenshots/property-detail.png` — property detail page
- `screenshots/dashboard.png` — owner dashboard
- `screenshots/postman-list.png` — successful API list response
- `screenshots/postman-create.png` — authenticated API create response

Example Markdown once screenshots have been added:

```md
![PlugListing homepage](screenshots/homepage.png)
```

No screenshots are fabricated or included in this starter package.

## Future improvements

- Add map-based search, geocoding, and neighbourhood filters.
- Add property moderation and verification workflows.
- Add pagination and richer filters for price, bedrooms, and property type.
- Add automated tests and CI checks for views, permissions, and API responses.
- Add cloud object storage for uploaded property images.
- Add email notifications for property inquiries and saved-search alerts.
- Add a dedicated API token issuance endpoint and refresh/revocation workflow.

## Quality and submission checklist

- [ ] Replace the Render URL placeholder with the deployed HTTPS URL.
- [ ] Add screenshots captured from the running application and Postman.
- [ ] Import and execute every request in the Postman collection against the deployed API.
- [ ] Confirm `DEBUG=False` and PostgreSQL is connected in the Render environment.
- [ ] Push to the public `dune-cohort-final-project` repository.
- [ ] Make at least eight meaningful commits with descriptive messages as development progresses.
- [ ] Run `python manage.py check` and `python manage.py makemigrations --check --dry-run` before submission.
