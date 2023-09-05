# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых
# частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

from collections import Counter

text = """
        It was a bright cold day in April, and the clocks were striking 
        thirteen. Winston Smith, his chin nuzzled into his
        breast in an effort to escape the vile wind, slipped quickly
        through the glass doors of Victory Mansions, though not
        quickly enough to prevent a swirl of gritty dust from enter-
        ing along with him. The hallway smelt of boiled cabbage and old rag mats. At
        one end of it a coloured poster, too large for indoor display,
        had been tacked to the wall. It depicted simply an enormous face, 
        more than a metre wide: the face of a man of
        about forty- five, with a heavy black moustache and rugged-
        ly handsome features. Winston made for the stairs. It was
        no use trying the lift. Even at the best of times it was 
        seldom working, and at present the electric current was cut
        off during daylight hours. It was part of the economy drive
        in preparation for Hate Week. The flat was seven flights up,
        and Winston, who was thirty-nine and had a varicose ulcer
        above his right ankle, went slowly, resting several times on
        the way. On each landing, opposite the lift-shaft, the poster
        with the enormous face gazed from the wall. It was one of
        those pictures which are so contrived that the eyes follow
        you about when you move. BIG BROTHER IS WATCHING
        YOU, the caption beneath it ran.
""".lower().replace(',', '').replace('.', '').replace(':', '')

words = Counter(item for item in text.split())
top_10_words = words.most_common(10)
print(top_10_words)
