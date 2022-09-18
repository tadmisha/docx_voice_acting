from docx import Document
from gtts import gTTS
from gtts.lang import tts_langs
from pathlib import Path

def doc_path_is_ok(path: str) -> bool:
    path = Path(path)
    if path.exists():
        if path.suffix == '.docx': return True
        else: print('File is not .docx')
    else: print('File is not exists')
    return False


def result_path_is_ok(path: str) -> bool:
    path = Path(path)
    if path.parent.exists():
        if path.suffix in ['.mp3', '.wav', '.aac']: return True
        else: print('File is not speech')
    else: print('File path is not exists')
    return False


def lang_supported(lang):
    langs = tts_langs().keys()
    if lang in langs:
        return True
    else:
        print('Language is not supported')
        return False


def read_docx(path: str) -> str:
    doc = Document(path)
    text = '\n'.join(paragraph.text for paragraph in doc.paragraphs)  # read text from every paragraph
    return text


def voice_act(text: str, lang: str, result_path: str):
    speech = gTTS(text, lang=lang, slow=False)
    speech.save(result_path)


def main():
    doc_path = input('Input path to document: ')
    if not doc_path_is_ok(doc_path): return
    res_path = input('Result path: ')
    if not result_path_is_ok(res_path): return
    lang = input('Language code: ').lower()
    if not lang_supported(lang): return

    print('Reading text...')
    text = read_docx(doc_path)
    print('Finished')

    print('Voice acting...')
    voice_act(text, lang, res_path)
    print('Finished')


if __name__ == '__main__':
    main()