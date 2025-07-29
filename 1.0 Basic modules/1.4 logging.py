import logging

# logging.basicConfig(level=logging.DEBUG)
# # logging.info("App started")

# logging.debug("This is for debugging")
# logging.info("All systems operational")
# logging.warning("Disk space low")
# logging.error("File not found")
# logging.critical("Server is down!")

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("App started")
