import pattern
from pattern.web import Wikipedia, plaintext
import re
from collections import defaultdict


class WikiParser:
    def __init__(self):
        pass

    def get_articles(self, start):

        article = Wikipedia().article(title=start)
        links = article.links
        list_of_strings = []
        for l in links:
            l_art = Wikipedia().article(title=l)
            l_text =  re.sub(' +', ' ', plaintext(l_art.source), flags = re.DOTALL)
            l_text = re.sub('[.;:!?\'\"-\(\)1234567890@,]+', '', l_text, flags = re.DOTALL).lower()
            list_of_strings.append(l_text.split())

        return list_of_strings




class TextStatistics:
     def __init___(self, articles):
            pass
    
     def get_top_3grams(self, n):
            
            list_of_3grams_in_descending_order_by_freq = []
            list_of_their_corresponding_freq = []
            for art in self.articles:
                for i in range(len(self.articles[art]) - 2):
                    three_gram = ' '.join(self.articles[art][i],  self.articles[art][i+1], self.articles[art][i+2])
                    if three_gram in list_of_3grams_and_freq:
                        list_of_3grams_and_freq.setdefault(three_gram, 0)
                        list_of_3grams_and_freq[three_gram] += 1          
            for key, value in sorted(list_of_3grams_and_freq.items(), key=operator.itemgetter(1)): 
                while len(list_of_3grams_in_descending_order_by_freq) != n:
                    list_of_3grams_in_descending_order_by_freq.append(key)
                    list_of_their_corresponding_freq.append(value)  
                                          
            return (list_of_3grams_in_descending_order_by_freq, list_of_their_corresponding_freq)
    
    
    
     def get_top_words(self, n):
            list_of_words_in_descending_order_by_freq = []
            list_of_their_corresponding_freq = []
            
            for art in self.articles:
                for w in self.articles[art]:
                    list_of_words_and_freq.setdefault(w, 0)
                    list_of_words_and_freq[w] += 1 
                    
            for key, value in sorted(list_of_words_and_freq.items(), key=operator.itemgetter(1)): 
                while len(list_of_words_in_descending_order_by_freq) != n:
                    list_of_words_in_descending_order_by_freq.append(key)
                    list_of_their_corresponding_freq.append(value)  

            return (list_of_words_in_descending_order_by_freq, list_of_their_corresponding_freq)


        
        

class Experiment:
    def __init___(self):
        pass
      
    def show_results(self):
        parser = WikiParser()
        articles = parser.get_articles('Natural language processing')
        art_statistics = TextStatistics(articles)
        print('топ-20 3-грамм по корпусу статей\r\n' + art_statistics.get_top_3grams(20))
        print('топ-20 слов по корпусу статей\r\n' + art_statistics.get_top_words(20))
        
        article = Wikipedia().article('Natural language processing')
        a_statistics = TextStatistics(article)
        print('топ-5 3-грамм по самой статье \r\n' + a_statistics.get_top_3grams(5))
        print('топ-5 слов по самой статье \r\n' + a_statistics.get_top_words(5))

        
a = Experiment()
        
    





