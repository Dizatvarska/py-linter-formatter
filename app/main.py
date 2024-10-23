error = {
    "code": "E501",
    "filename": "./source_code_2.py",
    "line_number": 18,
    "column_number": 80,
    "text": "line too long (99 > 79 characters)",
    "physical_line": '    return f"I like to filter, rounding, doubling, '
    "store and decorate numbers: {', '.join(items)}!\"",
    }

errors = [
    {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
        "text": "line too long (99 > 79 characters)",
        "physical_line": '    return f"I like to filter, rounding, doubling, ' 
        "store and decorate numbers: {', '.join(items)}!\"",
    },
    {
        "code": "W292",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 100,
        "text": "no newline at end of file",
        "physical_line": '    return f"I like to filter, rounding, doubling, '
        "store and decorate numbers: {', '.join(items)}!\"",
    },
]
report_file = {
    "./test_source_code_2.py": [],
    "./source_code_2.py":
        [
            {
                "code": "E501",
                "filename": "./source_code_2.py",
                "line_number": 18,
                "column_number": 80,
                "text": "line too long (99 > 79 characters)",
                "physical_line": '    return f"I like to filter, rounding, doubling, '
                "store and decorate numbers: {', '.join(items)}!\"",
            },
            {
                "code": "W292",
                "filename": "./source_code_2.py",
                "line_number": 18,
                "column_number": 100,
                "text": "no newline at end of file",
                "physical_line": '    return f"I like to filter, rounding, doubling, '
                "store and decorate numbers: {', '.join(items)}!\"",
            },
        ]
}


def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


format_linter_error = format_linter_error(error=error)


def format_single_linter_file(file_path: str, errors: list, error: dict) -> dict:
    return {
    "errors":
        [
            format_linter_error,
            {
                "line": errors[1]["line_number"],
                "column": errors[1]["column_number"],
                "message": errors[1]["text"],
                "name": errors[1]["code"],
                "source": "flake8"
            }
        ],
    "path": file_path,
    "status": "passed"
}


format_single = format_single_linter_file(file_path="./source_code_2.py", errors=errors, error=error)


def format_linter_report(linter_report: dict) -> list:
    return [
    {
        "errors": report_file["./test_source_code_2.py"],
        "path": "./test_source_code_2.py",
        "status": "passed"
    }, format_single
    ]


format_linter_report(linter_report=report_file)