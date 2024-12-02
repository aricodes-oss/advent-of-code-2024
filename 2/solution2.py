#!/usr/bin/env python

Report = list[int]

reports: list[Report] = []
with open("input", "r") as f:
    for line in f:
        reports.append([int(val) for val in line.rstrip().split()])


def all_ascending_or_descending(report: Report) -> bool:
    return report == sorted(report) or report == list(reversed(sorted(report)))


def step_size_valid(report: Report) -> bool:
    prev = report[0]
    for level in report[1:]:
        jump = abs(level - prev)
        if not (1 <= jump <= 3):
            return False
        prev = level
    return True


def is_safe(report: Report) -> bool:
    return all_ascending_or_descending(report) and step_size_valid(report)


def is_safe_without_el(report: Report, el: int) -> bool:
    return is_safe(report[:el] + report[el + 1 :])


safe_reports: list[Report] = []
for report in reports:
    safe = is_safe(report)
    if not safe:
        for idx in range(len(report)):
            safe = safe or is_safe_without_el(report, idx)

    if safe:
        safe_reports.append(report)

print(len(safe_reports))
