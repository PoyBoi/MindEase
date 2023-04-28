import app, connectAPI
import webbrowser
import os
import subprocess

def run_bat_file(bat_file):
    if not os.path.exists(bat_file):
        print(f"{bat_file} does not exist")
        return
    try:
        output = subprocess.check_output(
            f'tasklist /fi "imagename eq cmd.exe" /v /fo csv', shell=True
        ).decode()
        if bat_file in output:
            print(f"{bat_file} is already running")
            return
    except subprocess.CalledProcessError as e:
        print(e.output)
    subprocess.Popen(bat_file, shell=True)

# run_bat_file(r"C:\TheGoodShit\PythonProject\forMindEaseDocumentation\KoboldAI\KoboldAI\play.bat")

webbrowser.open_new_tab(r"C:\Users\parvs\VSC Codes\Python - root\mindEase\chatbot.html")
app.app.run(host = "localhost", port=8000, debug = True)