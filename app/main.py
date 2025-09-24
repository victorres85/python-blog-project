import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from starlette.middleware.cors import CORSMiddleware


logging.basicConfig(
    level=getattr(logging, settings.log_level),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log") if not settings.is_production else logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle application lifespan events."""
    logger.info(f"🚀 {settings.app_name} v{settings.version} starting up...")
    logger.info(f"📊 Environment: {settings.environment}")
    logger.info(f"🔧 Debug mode: {settings.debug}")
    logger.info(f"🌐 CORS origins: {settings.allowed_origins}")
    logger.info(f"📝 Docs available at: /docs" if settings.debug else "📝 Documentation disabled in production")
    
    yield
    
    logger.info("Application shutting down...")


def create_application() -> FastAPI:
    """Create and configure the FastAPI application."""
    # Create FastAPI app
    app = FastAPI(
        title=settings.app_name,
        description="A modern, AI-enhanced personal blog API built with FastAPI",
        version=settings.version,
        docs_url="/docs" if settings.debug else None,
        redoc_url="/redoc" if settings.debug else None,
        openapi_url="/openapi.json" if settings.debug else None,
        openapi_tags=[
            {
                "name": "health",
                "description": "Health check and system status endpoints"
            },
        ]
    )
    
    # Register exception handlers
    register_exception_handlers(app)

    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=settings.allow_credentials,
        allow_methods=settings.allowed_methods,
        allow_headers=settings.allowed_headers,
    )
    
    return app

app = create_application()


# Health check endpoint
@app.get("/health", tags=["health"])
async def health_check() -> tuple[str, int]:
    """Basic health check endpoint."""
    return "OK", 200

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        workers=settings.workers if not settings.reload else 1,
        log_level=settings.log_level.lower(),
        access_log=True,
        server_header=False,
        date_header=False
    )
