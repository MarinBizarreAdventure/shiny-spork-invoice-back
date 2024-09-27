from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import contract, invoice, customer, payment, error
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
# app.include_router(contract.router, prefix="/api/v1/contracts", tags=["contracts"])
# app.include_router(invoice.router, prefix="/api/v1/invoices", tags=["invoices"])
# app.include_router(customer.router, prefix="/api/v1/customers", tags=["customers"])
# app.include_router(payment.router, prefix="/api/v1/payments", tags=["payments"])
# app.include_router(error.router, prefix="/api/v1/errors", tags=["errors"])



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)