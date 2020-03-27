'''
3.
Card 클래스를 생성해 카드에 충전기능, 소비기능, 잔액을 알려주는 기능을 넣으시오.
-충전기능 (charge)
-소비기능 (consume)
-영화관에서 카드를 사용하면 20% 할인율 적용
print 기능(print) # 잔액이 ( ) 원 입니다.

테스트코드
<입력>
card = Card()
card.charge(20000)
card.consume(3000,'마트')
card.consume(10000,'영화관')
card.consume(13000,'마트')
card.print()

<출력>
잔액이 20000원 입니다.
마트에서 3000원 사용했습니다.
영화관에서 8000원 사용했습니다.
잔액이 부족합니다
잔액이 9000원 입니다.
'''

class Card():
    def __init__(self):
        self.money = 0

    def charge(self, charge1):
        self.money += charge1
        print("잔액이 {}원 입니다.".format(self.money))

    def consume(self, consume1, site):
        if site == "영화관":
            if self.money > consume1 * 0.8:
                self.money = self.money - consume1 * 0.8
                print("영화관에서 {}원 사용했습니다.".format(int(consume1 * 0.8)))
            else:
                print("잔액이 부족하니다.")
        else:
            if self.money > consume1:
                self.money = self.money - consume1
                print("마트에서 {}원 사용했습니다.".format(consume1))
            else:
                print("잔액이 부족합니다.")

    def print(self):
        print("잔액이 {}원 입니다.".format(int(self.money)))

card = Card()
card.charge(20000)
card.consume(3000,'마트')
card.consume(10000,'영화관')
card.consume(13000,'마트')
card.print()




