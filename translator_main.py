import time
import tkinter as tk
from tkinter import END
from tkinter import ttk
from translator_func import *
from tkinter.filedialog import askopenfile


def open_file(ent):
    file = askopenfile(mode='r', filetypes=[('All Word files','.docx .doc' )])#
    if file is not None:
        print(file.name)
        ent.delete(0,END)
        ent.insert(0,file.name)

def conf_trans():
    leng = run_ammount(input_path_var.get())
    progbar = tk.ttk.Progressbar(root, orient=tk.HORIZONTAL,
                                 length=leng, mode='determinate')
    progbar.grid(column=0, row=4)
    text_trans(input_path_var.get(),output_path_var.get(),input_lang_var.get(),output_lang_var.get(),root,progbar)
    print(input_path_var.get())
    print(output_path_var.get())
    print(input_lang_var.get())
    print(output_lang_var.get())


lang_to_codes="""Afrikaans af

Albanian sq

Amharic am

Arabic ar

Armenian hy

Azerbaijani az

Basque eu

Belarusian be

Bengali bn

Bosnian bs

Bulgarian bg

Catalan ca

Cebuano ceb

Chichewa ny

Chinese(Simplified) zh-CN

Chinese(Traditional) zh-TW

Corsican co

Croatian hr

Czech cs

Danish da

Dutch nl

English en

Esperanto eo

Estonian et

Filipino tl

Finnish fi

French fr

Frisian fy

Galician gl

Georgian ka

German de

Greek el

Gujarati gu

Haitian_Creole ht

Hausa ha

Hawaiian haw

Hebrew iw

Hindi hi

Hmong hmn

Hungarian hu

Icelandic is

Igbo ig

Indonesian id

Irish ga

Italian it

Japanese ja

Javanese jw

Kannada kn

Kazakh kk

Khmer km

Kinyarwanda rw

Korean ko

Kurdish(Kurmanji) ku

Kyrgyz ky

Lao lo

Latin la

Latvian lv

Lithuanian lt

Luxembourgish lb

Macedonian mk

Malagasy mg

Malay ms

Malayalam ml

Maltese mt

Maori mi

Marathi mr

Mongolian mn

Myanmar(Burmese) my

Nepali ne

Norwegian no

Odia(Oriya) or

Pashto ps

Persian fa

Polish pl

Portuguese pt

Punjabi pa

Romanian ro

Russian ru

Samoan sm

Scots_Gaelic gd

Serbian sr

Sesotho st

Shona sn

Sindhi sd

Sinhala si

Slovak sk

Slovenian sl

Somali so

Spanish es

Sundanese su

Swahili sw

Swedish sv

Tajik tg

Tamil ta

Tatar tt

Telugu te

Thai th

Turkish tr

Turkmen tk

Ukrainian uk

Urdu ur

Uyghur ug

Uzbek uz

Vietnamese vi

Welsh cy

Xhosa xh

Yiddish yi

Yoruba yo

Zulu zu

Hebrew he

Chinese(Simplified) zh"""

s=['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg',
   'ca', 'ceb', 'ny', 'zh-CN', 'zh-TW', 'co', 'hr', 'cs', 'da', 'nl', 'en',
   'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl','ka', 'de', 'el', 'gu', 'ht', 'ha',
   'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn',
   'kk', 'km', 'rw', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms',
   'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro',
   'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es','su', 'sw', 'sv', 'tg',
   'ta', 'tt', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu', 'he', 'z']

root = tk.Tk()
frm = tk.ttk.Frame(root, padding=10)
frm.grid()
root.geometry('400x150')
input_path_var=tk.StringVar()
output_path_var=tk.StringVar()
input_lang_var=tk.StringVar()
output_lang_var=tk.StringVar()
label1=tk.ttk.Label(frm, text="Input file")
label1.grid(column=0, row=0)
label2=tk.ttk.Label(frm, text="Output file")
label2.grid(column=0, row=1)
label3=tk.ttk.Label(frm, text="Input language")
label3.grid(column=0, row=2)
label4=tk.ttk.Label(frm, text="Output language")
label4.grid(column=0, row=3)
ent1=tk.ttk.Entry(frm, width=30,textvariable = input_path_var)
ent1.grid(column=1, row=0)
ent2=tk.ttk.Entry(frm, width=30, textvariable = output_path_var)
ent2.grid(column=1, row=1)
cmb1=tk.ttk.Combobox(frm, textvariable = input_lang_var)
cmb1['values']=s
cmb1.current(21)
cmb1.grid(column=1, row=2)
cmb2=tk.ttk.Combobox(frm, textvariable = output_lang_var)
cmb2['values']=s
cmb2.current(99)
cmb2.grid(column=1, row=3)
but1=tk.ttk.Button(frm, text="Quit", command=root.destroy)
but1.grid(column=2, row=3)
but2=tk.ttk.Button(frm, text="Confirm",command=lambda:conf_trans())
but2.grid(column=2, row=2)
but3=tk.ttk.Button(frm, text="...",command=lambda:open_file(ent1))
but3.grid(column=2, row=0)
but4=tk.ttk.Button(frm, text="...",command=lambda:open_file(ent2))
but4.grid(column=2, row=1)
print("Language and language codes:\n")
print(lang_to_codes)
root.mainloop()