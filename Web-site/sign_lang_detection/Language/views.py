from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Language, Alphabet

def index(request):
    languages = Language.objects.all()
    return render(request, 'index.html', {'languages': languages})

def convert_to_sign_index(request):
    languages = Language.objects.all()
    return render(request, 'convert_to_sign.html', {'languages': languages})

def alphabet(request):
    language_id = request.GET.get('language_id', '1')
    languages = Language.objects.all()
    if language_id:
        language = Language.objects.get(id=language_id)
        alphabets = Alphabet.objects.filter(language=language)
        return render(request, 'alphabet.html', {'languages': languages, 'language':language, 'alphabets':alphabets})
    return render(request, 'alphabet.html', {'languages': languages})

def get_letter_images(request):
    word = request.GET.get('word', '').lower()
    language_title = request.GET.get('language', '')
    images = []

    try:
        language = Language.objects.get(title=language_title)
        for letter in word:
            if letter.isspace():
                images.append('-')
            else:
                alphabet = Alphabet.objects.filter(language=language, letter=letter).first()
                if alphabet:
                    images.append(request.build_absolute_uri(alphabet.photo.url))
                else:
                    images.append('')
    except Language.DoesNotExist:
        pass

    return JsonResponse({'images': images})


def convert_to_sign(request):
    text = request.GET.get('text', '').lower()
    language_title = request.GET.get('language', 'English')

    language = get_object_or_404(Language, title=language_title)

    images = []
    for letter in text:
        if letter.isspace():
            images.append("space-placeholder")
        elif letter.isalpha() or letter.isdigit():
            try:
                alphabet = Alphabet.objects.get(letter=letter, language=language)
                images.append(request.build_absolute_uri(alphabet.photo.url))
            except Alphabet.DoesNotExist:
                images.append("missing-letter-placeholder")
        else:
            images.append("unknown-character-placeholder")

    return JsonResponse({'images': images})