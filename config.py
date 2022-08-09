from dotenv import load_dotenv
import os


class SimpleConfig:
    def __init__(self):
        load_dotenv()
        if os.environ.get("USE_DB_IN") == "dev":
            self.DB_DATABASE = os.environ.get("DEV_DATABASE")
            self.DB_USER = os.environ.get("DEV_USER")
            self.DB_PASSWORD = os.environ.get("DEV_PASSWORD")
            self.DB_HOST = os.environ.get("DEV_HOST")
            self.DB_PORT = os.environ.get("DEV_PORT")
            self.EXPOSE_API_DOCUMENTATION: bool = os.environ.get(
                "DEV_EXPOSE_API_DOCUMENTATION"
            )
        elif os.environ.get("USE_DB_IN") == "docker":
            self.DB_HOST = os.environ.get("DOCKER_HOST")
            self.DB_DATABASE = os.environ.get("DEV_DATABASE")
            self.DB_USER = os.environ.get("DEV_USER")
            self.DB_PASSWORD = os.environ.get("DEV_PASSWORD")

            self.DB_PORT = os.environ.get("DEV_PORT")
            self.EXPOSE_API_DOCUMENTATION: bool = os.environ.get(
                "DEV_EXPOSE_API_DOCUMENTATION"
            )
        elif os.environ.get("USE_DB_IN") == "production":
            self.DB_DATABASE = os.environ.get("PROD_DATABASE")
            self.DB_USER = os.environ.get("PROD_USER")
            self.DB_PASSWORD = os.environ.get("PROD_PASSWORD")
            self.DB_HOST = os.environ.get("PROD_HOST")
            self.DB_PORT = os.environ.get("PROD_PORT")
            self.EXPOSE_API_DOCUMENTATION: bool = os.environ.get(
                "PROD_EXPOSE_API_DOCUMENTATION"
            )
        else:
            raise Exception("Invalid USE_DB_IN flag")


cfg = SimpleConfig()
