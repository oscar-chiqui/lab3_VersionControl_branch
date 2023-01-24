def camelcase(sentence):

    title_case = sentence.title()
    upper_camel_cased = title_case.replace(' ','')

    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def alternative():
    """Display program name """
    message = 'Awesome camelcase program!!'
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}')

def main():
    alternative()
    sentence =input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)

if __name__ =='__main__':
    main()