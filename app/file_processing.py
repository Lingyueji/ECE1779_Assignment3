import PyPDF2
import re
from collections import Counter


def synonyms(word):
    SYN = (
        ['cpp', 'c++'],
        ['js', 'javascript'],
        ['ml', 'machine learning'],
        ['dl', 'deep learning']
    )

    for syn_list in SYN:

        if word in syn_list:
            return syn_list

    return [word]


def get_text(filepath):
    with open(filepath, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        num_of_pages = reader.getNumPages()

        text = ''
        for i in range(num_of_pages):
            text += reader.getPage(i).extractText().replace('\n', '')

        return text


def find_email(filepath):
    text = get_text(filepath)

    match = re.findall(r'[\w\.-]+@[\w\.-]+', text)

    return match[0] if match else 'Email not found'


def find_phone(filepath):
    text = get_text(filepath)

    pattern = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
    match = re.findall(pattern, text)

    return match[0] if match else 'Phone number not found'


def judge_skills(filepath, skill_set_string):
    cnt = Counter()

    text = get_text(filepath)
    text = re.sub('[^\w\+\#]', ' ', text.lower())

    skill_set_list = [s.strip(' ') for s in skill_set_string.split(',')]

    for skill in skill_set_list:
        cnt[skill] = str(text.count(' ' + skill.lower() + ' '))

    return cnt


def judge_skills_with_synonyms(filepath, skill_set_string):
    cnt = Counter()

    text = get_text(filepath)
    text = re.sub('[^\w\+\#]', ' ', text.lower())

    skill_set_list = [s.strip(' ') for s in skill_set_string.split(',')]

    for skill in skill_set_list:
        # cnt[skill] = str(text.count(' ' + skill.lower() + ' '))
        cnt[skill] = str(sum([text.count(' ' + s.lower() + ' ') for s in synonyms(skill)]))

    return cnt


