from __future__ import annotations

import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class Settings(BaseModel):
    app_name: str = "Trading Agent Premium"
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", "8000"))
    cors_origins: list[str] = Field(default_factory=lambda: ["*"])

    mode: str = os.getenv("MODE", "paper")
    allow_live_trading: bool = os.getenv("ALLOW_LIVE_TRADING", "false").lower() == "true"
    symbols: list[str] = Field(
        default_factory=lambda: [
            s.strip() for s in os.getenv("SYMBOLS", "BTCUSDT,ETHUSDT").split(",") if s.strip()
        ]
    )

    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-5.4-thinking")
    ai_enabled: bool = os.getenv("AI_ENABLED", "true").lower() == "true"

    telegram_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    telegram_chat_id: str = os.getenv("TELEGRAM_CHAT_ID", "")

    initial_portfolio_lei: float = float(os.getenv("INITIAL_PORTFOLIO_LEI", "1000"))
    initial_active_allocation_pct: float = float(os.getenv("INITIAL_ACTIVE_ALLOCATION_PCT", "0.35"))

    app_username: str = os.getenv("APP_USERNAME", "owner")
    app_password: str = os.getenv("APP_PASSWORD", "change-me")
    app_otp_secret: str = os.getenv("APP_OTP_SECRET", "123456")
    app_jwt_secret: str = os.getenv("APP_JWT_SECRET", "dev-secret")


settings = Settings()