# E-Tech: High-Performance E-commerce API

## Overview
E-Tech is a production-ready, high-performance E-commerce backend built with **FastAPI** and **PostgreSQL**. It leverages a **Three-Tier Modular Monolith** architecture to ensure scalability, maintainability, and rigorous type safety.

## Technical Stack
- **Framework:** FastAPI (Python 3.12+)
- **Database:** PostgreSQL 16
- **ORM:** SQLAlchemy 2.0 (Async)
- **Validation:** Pydantic v2
- **Migrations:** Alembic
- **Containerization:** Docker & Docker Compose
- **Security:** OAuth2 with JWT, Argon2 Password Hashing

## Architectural Patterns
- **Three-Tier Architecture:** Clear separation between API Routers, Service Logic, and Repository Data Access.
- **Dependency Injection:** Extensive use of FastAPI's `Depends` for resource management (DB sessions, Auth).
- **Asynchronous I/O:** Fully async database operations to maximize throughput.
- **Idempotency:** Implement idempotency keys for sensitive transactions (Checkout, Payments).

## Project Structure
```text
E-Tech/
├── app/
│   ├── api/          # Route handlers & API versioning
│   ├── core/         # Global configuration, security & constants
│   ├── models/       # SQLAlchemy 2.0 declarative models
│   ├── schemas/      # Pydantic v2 validation schemas
│   ├── services/     # Business logic & orchestration
│   ├── repositories/ # Abstracted data access layer
│   ├── db/           # Session management & engine setup
│   └── main.py       # Application entry point
├── tests/            # Pytest suite (Unit & Integration)
├── alembic/          # Database migrations
└── scripts/          # Utility scripts (seeding, maintenance)
```

## Getting Started
(Standard instructions for senior devs...)
