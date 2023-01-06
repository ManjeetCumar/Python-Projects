import pywhatkit as pw

txt = '''PyWhatKit is a Simple and Powerful WhatsApp
        Automation Library with many useful Features.
        It's easy-to-use and does not require you to 
        do any additional setup. Currently, it is one
         of the most popular library for WhatsApp and
          YouTube automation. New updates are released
           frequently with new features and bug fixes.'''

pw.text_to_handwriting(txt, "./ouputs/hand_writing.png",(0,0,138))
print("Done...")