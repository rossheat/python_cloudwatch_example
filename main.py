from cloud_logger import logger


def main():
    print("Starting main")
    log = logger(__name__)
    log.info("Hello from main")
    print("Ending main")


if __name__ == "__main__":
    main()
