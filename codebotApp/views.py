from django.shortcuts import render
from django.contrib import messages
import openai

def home(request):
    lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'docker', 'go','html', 'java', 'javascript', 'json', 'json5', 'jsx', 'markup', 'markup-templating', 'perl', 'php', 'plsql', 'powershell', 'python', 'regex', 'sql', 'tsx', 'typescript', 'yaml']
    
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']

        if lang == "Select Programming Language":
            messages.success(request, 'Hey! You forgot to pick a programming language...')
            return render(request, 'home.html', {'lang_list':lang_list, 'response':code, 'code':code, 'lang':lang})
        else:

            # OpenAI Key
            openai.api_key = "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"

            # Create OpenAI Instance
            openai.Model.list()

            # Make an OpenAI Request
            try:
                response = openai.Completion.create(
                    engine = 'text-davinci-003',
                    prompt = f"Respond only with code. Fix this {lang} code: {code}",
                    temperature = 0,
                    max_tokens = 1000,
                    top_p = 1.0,
                    frequency_penalty = 0.0,
                    presence_penalty = 0.0
                )

                # Parse the response
                response = (response['choices'][0]['text']).strip()

                return render(request, 'home.html', {'lang_list': lang_list, 'response': response, 'lang': lang})



            except Exception as e:

                return render(request, 'home.html', {'lang_list': lang_list, 'response': e, 'lang': lang})



    return render(request, 'home.html', {'lang_list': lang_list})


def suggest(request):
    lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'docker', 'go','html', 'java', 'javascript', 'json', 'json5', 'jsx', 'markup', 'markup-templating', 'perl', 'php', 'plsql', 'powershell', 'python', 'regex', 'sql', 'tsx', 'typescript', 'yaml']
    
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']

        if lang == "Select Programming Language":
            messages.success(request, 'Hey! You forgot to pick a programming language...')
            return render(request, 'suggest.html', {'lang_list':lang_list, 'response':code, 'code':code, 'lang':lang})
        else:

            # OpenAI Key
            openai.api_key = "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"

            # Create OpenAI Instance
            openai.Model.list()

            # Make an OpenAI Request
            try:
                response = openai.Completion.create(
                    engine = 'text-davinci-003',
                    prompt = f"Respond only with code. {code}",
                    temperature = 0,
                    max_tokens = 1000,
                    top_p = 1.0,
                    frequency_penalty = 0.0,
                    presence_penalty = 0.0
                )

                # Parse the response
                response = (response['choices'][0]['text']).strip()

                return render(request, 'suggest.html', {'lang_list': lang_list, 'response': response, 'lang': lang})



            except Exception as e:

                return render(request, 'suggest.html', {'lang_list': lang_list, 'response': e, 'lang': lang})



    return render(request, 'suggest.html', {'lang_list': lang_list})