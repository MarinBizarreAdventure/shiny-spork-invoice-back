

### Setting Up the Project

#### Installation

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file at the root of the project and set your environment variables (e.g., database credentials, OpenAI API key, Google API credentials).


---
### Project Structure

The project is divided into the following main components, following Clean Architecture:

1. **API (app/api):** 
   - This folder contains all the route handlers (endpoints) for different features such as user management, contract parsing, invoice generation, and Google integration.
   - Routes are versioned (e.g., `v1/`) for future extensibility.
   
2. **Core (app/core):**
   - Core configurations, security settings, and third-party API integrations (e.g., Google API services) live here.
   - The `security.py` file handles authentication logic such as JWT token generation and validation.

3. **Services (app/services):**
   - Business logic is encapsulated in service classes.
   - `user_service.py`: Contains the business logic for managing users.
   - `contract_service.py`: Handles contract parsing using OpenAI.
   - `invoice_service.py`: Deals with the logic for generating and managing invoices.
   - `google_docs_service.py`: Manages interactions with Google Docs.
   - `google_calendar_service.py`: Manages calendar scheduling for reminders.

4. **Database Models (app/db/models):**
   - ORM models represent the data schema in PostgreSQL.
   - `user_model.py`: Defines the user table structure.
   - `contract_model.py`: Defines how contracts are stored.
   - `invoice_model.py`: Represents invoice data.

5. **Repository (app/repository):**
   - Repository pattern abstracts the data access layer.
   - `user_repository.py`: Queries related to users.
   - `contract_repository.py`: Handles contract data.
   - `invoice_repository.py`: Deals with invoices.

6. **Schemas (app/schemas):**
   - Pydantic models define the request and response payload structure.
   - `user_schemas.py`: Defines how user data is validated.
   - `contract_schemas.py`: Validation schema for contract data.
   - `invoice_schemas.py`: Schema for invoices.
---

### Endpoints

Here are the key API endpoints in the project:

- **User Endpoints (Authentication & User Management):**
  - `POST /api/v1/auth/login`: User login and JWT token generation.
  - `POST /api/v1/users`: Create a new user.
  - `GET /api/v1/users/{user_id}`: Retrieve user details.
  - `PUT /api/v1/users/{user_id}`: Update user information.
  - `DELETE /api/v1/users/{user_id}`: Delete a user.

- **Contract Parsing:**
  - `POST /api/v1/contracts`: Upload and parse a contract for billing terms.

- **Invoice Generation:**
  - `POST /api/v1/invoices`: Generate invoices based on parsed contract data.
  - `GET /api/v1/invoices/{invoice_id}`: Retrieve invoice details.

- **Google Docs Integration:**
  - `POST /api/v1/google/docs/upload`: Upload a contract to Google Docs.
  - `GET /api/v1/google/docs/{doc_id}`: Retrieve Google Docs information.

- **Google Calendar Integration:**
  - `POST /api/v1/google/calendar/schedule`: Schedule reminders on Google Calendar.

---

