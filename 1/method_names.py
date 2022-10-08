
# good: present tense verbs
def perform(): pass
def open(): pass
def close(): pass
def validate(): pass

# bad: past tense verbs
# def performed(): pass def validated(): pass def closed(): pass
# bad: gerunds
# def performing(): pass def opening(): pass def closing(): pass
# def validating(): pass

# better: prefix past tense verbs with "has" and gerunds with "is"
def has_performed(): pass
def is_opening(): pass
def is_closing(): pass
def has_validated(): pass