import string
import matplotlib.pyplot as plt
from collections import Counter
import stop_w
from googletrans import Translator

def NLP(text):
    # text = open("read.txt", encoding="utf-8").read()
    
    #######starting input data #####

 

    detect=t.detect(text)
    
    if detect.lang  != 'en':
        
            text_eng=t.translate(text , dest='en').text
            text=text_eng
            # print(f"{text} 1")
            # print(f"{text_eng} 2")
    
    elif detect.lang  == 'en' :
        
        #   text_eng=t.origin
       
            text_eng = text
            text=text_eng



            lower_case = text_eng.lower()


            cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))


            tokenized_words = cleaned_text.split()
        
        

        
    # print(text_eng)
    # print(text)
    # trans=' '.join(tokenized_words)
    # translate(trans)

        
    final_words = []
    for word in tokenized_words:
        if word not in stop_w.stop_words:
            final_words.append(word)



    emotion_list = []
    with open('emotions.txt', 'r',encoding='utf-8') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in final_words:

                emotion_list.append(emotion)

                # emotion_list.append(word)
                ####can add to anther append list to count emoji 

    # print(emotion_list)
    # global w
    NLP.w = Counter(emotion_list)
    # w = Counter(emotion_list)
    print(NLP.w)
    # print(w)


  



t = Translator()
class Trans_Dialog:
    def translate(self ,text_ar):
        

        self.detect_lang =t.detect(text_ar)

        print(f"Languge Detect : {self.detect_lang.lang} " )

        self.trans_any= t.translate(text_ar, dest='ar').text # send to dialogflow
        
        # trans_en= t.translate(text_ar, dest='en').text # send to analyse NLP 
        
        print(f"Arbic Trans : {self.trans_any}")



# NLP("Im very happy to day ")

# NLP("Im very happy to day")

# print(NLP.w)