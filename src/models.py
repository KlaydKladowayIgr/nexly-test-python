from dataclasses import dataclass, field
import datetime


@dataclass(slots=True)
class CompanyInfo:
    name: str
    date: datetime.date