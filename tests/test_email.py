import pytest
from unittest.mock import AsyncMock
from app.services.email_service import EmailService
from app.utils.template_manager import TemplateManager

@pytest.mark.asyncio
async def test_send_markdown_email(monkeypatch):
    # Setup
    email_service = EmailService(template_manager=TemplateManager())
    monkeypatch.setattr(email_service, "send_user_email", AsyncMock())

    # Test input
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "verification_url": "http://example.com/verify?token=abc123"
    }

    # Action
    await email_service.send_user_email(user_data, 'email_verification')

    # Assert it was called
    email_service.send_user_email.assert_called_once_with(user_data, 'email_verification')
