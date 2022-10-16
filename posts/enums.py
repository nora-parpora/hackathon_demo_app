from enum import Enum


class EmploymentType(Enum):
    FULL_TIME = "Full time"
    PART_TIME = "Part time"
    INTERN = "Intern"


class RentalType(Enum):
    RENT = 'Rent'
    FUNDED = 'Funded'



    # @classmethod
    # def from_string(cls, value) -> str:
    #     if value not in [cls.FULL_TIME, cls.PART_TIME, cls.INTERN]:
    #         return HttpResponse(status=400, content=(
    #             f'None of the possible Employment types match the value {value}.'))
    #
    #     return value


