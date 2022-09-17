from docx import Document
from pathlib import Path

# print(pardir(r'C:\Users\Misha\Downloads\Labirint.docx'))
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
    
def read_docx(path: str) -> str:
    doc = Document(r'C:/Users/Misha/Downloads/Labirint.docx')
    text = '\n'.join(paragraph.text for paragraph in doc.paragraphs)  # read text from every paragraph
    return text

def voice_act(text: str, result_path: str): pass

def main():
    doc_path = input('Input path to document: ')
    if not doc_path_is_ok(doc_path): return
    res_path = input('Result path: ')
    if not result_path_is_ok(res_path): return

if __name__ == '__main__':
    main()