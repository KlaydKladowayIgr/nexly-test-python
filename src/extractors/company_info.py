from datetime import date

from pypdf import PdfReader
from dateparser.search import search_dates

from models import CompanyInfo


class CompanyInfoExtractor:
    def __init__(self, pdf_path: str) -> None:
        self.pdf = PdfReader(pdf_path)

    def get_company_info(self) -> CompanyInfo:
        return CompanyInfo(
            name=self._get_company_name(),
            date=self._get_report_date()
        )
    
    def _get_raw_content(self) -> str:
        return self.pdf.get_page(0).extract_text()
    
    def _get_report_date(self) -> date:
        return search_dates(self._get_raw_content(), settings={"STRICT_PARSING": True})[0][-1].date()
    
    def _get_company_name(self) -> str:
        return self._get_raw_content().split("\n")[0].strip()
