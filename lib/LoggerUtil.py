import logging

logger = logging.getLogger("TestLogger")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class LoggerUtil:
    def log_pass(self, message):
        logger.info(f"✅ PASS: {message}")

    def log_fail(self, message):
        logger.error(f"❌ FAIL: {message}")
        raise AssertionError(f"FAIL: {message}")

    def log_info(self, message):
        logger.info(f"ℹ️ INFO: {message}")