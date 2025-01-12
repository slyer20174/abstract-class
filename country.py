class uk:
    def capital(self):
        print("london is the capital of uk")
    def language(self):
        print("english is the language of uk")
class nigeria:
    def capital(self):
        print("abuja is the capital of nigeira ")
    def language(self):
        print("english is one of the languages in nigeria")
object_uk=uk()
object_nigeria=nigeria()
for i in(object_uk,object_nigeria):
    i.capital()
    i.language()