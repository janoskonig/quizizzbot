from quizizz import QuizizzUploader 
import os

def process_filename(folder):
    results = []  # Lista az eredmények tárolására
    for file in os.listdir(folder):
        if file.endswith('.xlsx') and os.path.isfile(os.path.join(folder, file)) and not file.startswith('.'):
            file_path = os.path.join(folder, file)  # A fájl teljes elérési útja
            filename = os.path.basename(file_path)
            name_without_extension = filename[:-5]
            parts = name_without_extension.split()
            second_variable = ' '.join(parts[:4])
            # Hozzáadjuk a file_path-t is az eredményekhez
            results.append((file_path, name_without_extension, second_variable))
    return results


source_folder = "/Volumes/T7 Touch/02 Klinika/25 kurrikulumreform/TAF MOODLE ONLINE ANYAGOK working dir/Quizizz kvízek/feltolthetok/"
file_results = process_filename(source_folder)

username = 'gipsz@jakab.com'
password = 'NOTPUBLIC'

for result in file_results:
    file_path, quiz_name, second_variable = result
    button_xpath = f"//button[.//div[contains(text(), '{second_variable}')]]"
    uploader = QuizizzUploader(username, password, file_path)
    uploader.login()
    uploader.upload_quiz(quiz_name, button_xpath, file_path)