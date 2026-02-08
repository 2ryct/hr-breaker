from hr_breaker.config import Settings


def test_settings_has_retry_fields():
    s = Settings()
    assert s.retry_max_attempts == 5
    assert s.retry_max_wait == 60.0
