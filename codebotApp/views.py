from django.shortcuts import render

def home(request):
    lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'docker', 'go','html', 'java', 'javascript', 'json', 'json5', 'jsx', 'markup', 'markup-templating', 'perl', 'php', 'plsql', 'powershell', 'python', 'regex', 'sql', 'tsx', 'typescript', 'yaml']
    
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']
        return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang': lang})

    return render(request, 'home.html', {'lang_list': lang_list})
