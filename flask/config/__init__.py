# coding: UTF-8
import os


def load_config(mode=os.environ.get('MODE')):
    """Load config."""
    try:
        if mode == 'pro':
            from .production import ProductionConfig
            return ProductionConfig
        elif mode == 'test':
            from .testing import TestingConfig
            return TestingConfig
        else:
            from .development import DevelopmentConfig
            return DevelopmentConfig
    except ImportError:
        from .default import Config
        return Config
