def checkNumber(number):
    pattern = r'\d+'  # match one or more digits
    match = re.match(pattern, number)
    return True if match else False