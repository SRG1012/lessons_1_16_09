def correct_sentence(text: str) -> str:
    sentences = text.split('.')
    corrected_sentences = [s.capitalize() if s else '' for s in sentences]
    result = '. '.join(corrected_sentences)
    if not result.endswith('.'):
        result += '.'
    return result
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')