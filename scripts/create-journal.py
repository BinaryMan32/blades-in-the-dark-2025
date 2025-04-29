#!/usr/bin/env python3
import datetime
import os
import pathlib
import string


def read_template(name):
    template_path = pathlib.Path(__file__).with_name(name)
    with open(template_path) as f:
        return string.Template(f.read())


def write_journal(template: string.Template, journal_date: datetime.date):
    date_string = journal_date.isoformat()
    journal_dir = os.path.join('docs', 'journal', 'posts', date_string)
    os.makedirs(journal_dir, exist_ok=True)
    journal_path = os.path.join(journal_dir, f'{date_string}.md')
    if os.path.exists(journal_path):
        print(f'File "{journal_path}" exists, aborting')
        exit(1)
    print(f'Creating "{journal_path}"')
    with open(journal_path, 'w') as f:
        f.write(template.substitute(DATE=date_string))


def main():
    template = read_template('journal-template.md')
    today = datetime.date.today()
    write_journal(template, today)


if __name__ == '__main__':
    exit(main())
