import json
import yaml
import csv
import logging
from logging.handlers import RotatingFileHandler
import os


# 1. JSON configuration va DEBUG log

with open("config.json", "r") as file:
    config = json.load(file)

logging.basicConfig(level=logging.INFO)

if config.get("debug") is True:
    logging.debug("DEBUG rejimi yoqilgan")
    print("DEBUG rejimi yoqilgan")


# 2. YAML -> JSON va JSON -> YAML

with open("config.yaml", "r") as file:
    yaml_data = yaml.safe_load(file)

with open("converted.json", "w") as file:
    json.dump(yaml_data, file, indent=4)

with open("converted.json", "r") as file:
    json_data = json.load(file)

with open("converted.yaml", "w") as file:
    yaml.dump(json_data, file)

print("YAML va JSON konvertatsiya qilindi")


# 3. CSV faylni qatorma-qator o'qish

with open("servers.csv", "r") as input_file, \
        open("errors.csv", "w", newline="") as output_file:

    reader = csv.DictReader(input_file)
    writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)

    writer.writeheader()

    for row in reader:
        if row["status"] == "error":
            writer.writerow(row)

print("ERROR qatorlar errors.csv fayliga yozildi")


# 4. RotatingFileHandler

logger = logging.getLogger("rotating_logger")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    "application.log",
    maxBytes=1024 * 1024,
    backupCount=3
)

logger.addHandler(handler)

logger.info("Application started")
print("Rotating log sozlandi")


# 5. Barcha .log fayllarni tekshirish

with open("error_report.txt", "w") as report:

    for filename in os.listdir("."):
        if filename.endswith(".log"):

            with open(filename, "r", errors="ignore") as log_file:
                for line in log_file:
                    if "ERROR" in line:
                        report.write(
                            f"{filename}: {line}"
                        )

print("ERROR loglar error_report.txt fayliga yozildi")
