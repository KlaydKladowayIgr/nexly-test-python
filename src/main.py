import argparse
from datetime import datetime

from extractors.company_info import CompanyInfoExtractor
from validators import CompanyNameValidator, ReportDateValidator


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="NexlyTest"
    )
    parser.add_argument("--company_name")
    parser.add_argument("--date")

    input_args = parser.parse_args()

    try:
        datetime.strptime(input_args.date, "%Y-%m-%d")
    except ValueError:
        print("Incorrect date format")
        exit(-1)

    company_info = CompanyInfoExtractor("./report.pdf").get_company_info()
    CompanyNameValidator(company_info.name).validate(input_args.company_name)
    ReportDateValidator(company_info.date.strftime("%Y-%m-%d")).validate(input_args.date)