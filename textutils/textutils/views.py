from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    text = request.POST.get('text', 'default text')

    remove_punc = request.POST.get('removepunc', 'off')
    full_caps = request.POST.get('fullcaps', 'off')
    newline_remover = request.POST.get('newlineremover', 'off')
    extraspace_remover = request.POST.get('extraspaceremover',  'off')

    # print(request.POST.get('csrfmiddlewaretoken'))
    # print(repr(raw_text))
    actions = []

    if remove_punc == "on":
        actions.append("Punctuations removed")
        analyzed_text = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in text:
            if char not in punctuations:
                analyzed_text += char

        text = analyzed_text

    if full_caps == "on":
        actions.append("Capatilized letters")
        analyzed_text = ""

        for char in text:
            analyzed_text += char.upper()

        text = analyzed_text

    if newline_remover == "on":
        actions.append("Newlines removed")
        analyzed_text = ""

        for char in text:
            if char != "\n" and char != "\r":
                analyzed_text += char

        text = analyzed_text

    if extraspace_remover == "on":
        actions.append("Extraspaces removed")
        analyzed_text = ""

        for index, char in enumerate(text):
            if index != (len(text) - 1):
                if not(text[index] == " " and text[index + 1] == " "):
                    analyzed_text += char

        if text[len(text) - 1] != " ":
            analyzed_text += char

        text = analyzed_text

    if len(actions) == 0:
        actions.append("None")

    params = {
        'actions': actions,
        'analyzed_text': text
    }

    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')
