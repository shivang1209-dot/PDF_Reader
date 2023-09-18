import pyttsx3,PyPDF2

#Input For The Name Of PDF File
pdf_name = input("Enter The Name Of The PDF You Want To Convert To mp3: ") + ".pdf"

#Initialise PDF Reader And Error Handling
try:
    pdfReader = PyPDF2.PdfReader(open(pdf_name, 'rb'))

except FileNotFoundError:
    print("Incorrect File Name/File Does Not Exist")

#Initialise Speaker
speaker = pyttsx3.init()

#Read Page By Page Line By Line
for curr_page in range(len(pdfReader.pages)):
    text = pdfReader.pages[curr_page].extract_text()
    final_text = text.strip().replace('\n', ' ')

#Input For The Output Audio File
audio_name = input("Enter The Name Of The Audio File: ") + ".mp3" 

#Save File
speaker.save_to_file(final_text, audio_name)

#Stop The Speaker
speaker.runAndWait()
speaker.stop()

#EOF