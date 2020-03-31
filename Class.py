

class Cat:

    def __init__(self, name='나비', color='black'):
        self.name = name
        self.color = color

    def info(self):
        print('고양이 이름은', self.name, '색은', self.color)


cat1 = Cat('네로', '검정')
cat2 = Cat('미미', '갈색')

cat1.info()
cat2.info()
