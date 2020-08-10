#!/usr/bin/env python3
"""
Parse a Public Suffix List (https://publicsuffix.org) file and outputs a regular expression.

The Public Suffix List offers a list of top-level domains and hosting sites that
offer subdomains that are in effect like top-level domainsp.

We take only the ICANN TLDs from the Public Suffix List and turn them into a
regular expression that this Terraform module can use.

Usage:
    python3 make_regex.py public_suffix_list.dat > regex.txt

"""
import fileinput

BEGIN_LINE = "BEGIN ICANN DOMAINS"

END_LINE = "END ICANN DOMAINS"

def get_domains(input_iterator):
    start_parsing = False
    for line in input_iterator:
        if BEGIN_LINE in line:
            start_parsing = True
            continue
        if END_LINE in line:
            break
        if start_parsing:
            if "//" in line:
                continue
            splitted = line.split()
            if splitted:
                first_part = splitted[0]
                if first_part:
                    if first_part[:2] == "*.":
                        continue
                        yield first_part[:2]
                    else:
                        yield first_part

REGEX_STR = "".join([
    r"(?P<domain>[^.:/@]+)\.",
    r"(?P<suffix>",
    r"|".join(
        domain.replace(".", r"\.")
        for domain in get_domains(fileinput.input())
    ),
    r")$",
])

print(REGEX_STR, end="")