# PlugListing REST API

Base URL: `https://YOUR-RENDER-SERVICE.onrender.com/api/` (replace after deployment).

Authentication uses DRF Token Authentication: send `Authorization: Token YOUR_TOKEN` for protected writes. Obtain a token with `POST /api-token-auth/` using `username` and `password` fields; alternatively use the Django browsable API session while logged in.

| Method | Endpoint | Authentication | Purpose |
|---|---|---|---|
| GET | `/api/properties/` | No | Paginated property list |
| POST | `/api/properties/` | Yes | Create a property owned by the authenticated user |
| GET | `/api/properties/{id}/` | No | Retrieve one property |
| PUT/PATCH | `/api/properties/{id}/update/` | Yes; owner or staff | Update an owned property |
| DELETE | `/api/properties/{id}/delete/` | Yes; owner or staff | Delete an owned property |

Example list response:
```json
{"count":1,"next":null,"previous":null,"results":[{"id":1,"owner_username":"demo","title":"Sunny apartment","property_type":"apartment","status":"available","price":"2500000.00","city":"Lagos"}]}
```
Create request example:
```json
{"title":"Sunny apartment","description":"Bright two-bedroom apartment.","property_type":"apartment","status":"available","price":"2500000.00","address":"12 Example Road","city":"Lagos","bedrooms":2,"bathrooms":2,"area_sq_m":95}
```
Expected statuses: 200 for successful reads/updates, 201 for creation, 204 for deletion, 400 for invalid input, and 404 when a record does not exist or is outside the caller's ownership scope.
