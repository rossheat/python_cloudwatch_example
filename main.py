from cloud_logger import logger

log = logger(__name__)


def main():
    log.info("Hello from main")


if __name__ == "__main__":
    main()
