def is_this_answer_to_ultimate_question_of_life(n):
    if n < 0 or n > 100:
        return "Definetely no!"
    if (n > 0 and n < 10) or (n > 90):
        return "Rather no"
    elif (n >= 10 and n < 20) or (n > 80):
        return "Well no..."
    elif (n >= 20 and n < 30) or (n > 60):
        return "No but close"
    elif (n >= 30 and n < 40) or (n > 50):
        return "No but really close"
    elif (n >= 40 and n < 42) or (n > 42 and n < 50):
        return "Almost right"
    elif n == 42:
        return "Exactly!"
    return "That should not happen at all!"