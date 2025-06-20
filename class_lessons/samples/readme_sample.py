# クラスとインスタンスの例 - Humanクラス

class Human:
    """
    Humanクラス - インスタンスの雛形となるクラス
    プロパティ（静的な属性）とメソッド（動的な動作）を定義
    """
    
    def __init__(self, height, weight, name):
        """
        コンストラクタ - インスタンス生成時に呼ばれる
        プロパティ（インスタンス変数）を初期化
        """
        # プロパティ（インスタンス変数） - 静的な基本情報
        self.height = height
        self.weight = weight
        self.name = name
    
    def introduce(self):
        """自己紹介するメソッド"""
        print(f"私は{self.name}です。")
        print(f"身長: {self.height}cm、体重: {self.weight}kg\n")

    def buy_juice(self, juice_type="オレンジジュース"):
        """ジュースを買うメソッド"""
        print(f"{self.name}は{juice_type}を買いました")

    def eat_coffee_jelly(self):
        """コーヒーゼリーを食べるメソッド"""
        print(f"{self.name}はコーヒーゼリーを食べています")

    def wash_dishes(self, count=1):
        """お皿を洗うメソッド"""
        print(f"{self.name}は{count}枚のお皿を洗いました")

    def write_code(self, language="Python"):
        """コードを書くメソッド"""
        print(f"{self.name}は{language}のコードを書いています")

    def shout(self, message="うわあああ！"):
        """叫ぶメソッド"""
        print(f"{self.name}は'{message}'と叫びました")


print("=== 太郎、次郎、花子を作る ===")
taro = Human(height=175, weight=70, name="Taro") # インスタンス1を生成
hanako = Human(height=160, weight=55, name="Hanako") # インスタンス2を生成
jiro = Human(height=180, weight=80, name="Jiro") # インスタンス3を生成

print("\n=== 各インスタンスの自己紹介 ===")
taro.introduce()
hanako.introduce()
jiro.introduce()

print("\n=== インスタンスメソッドの実行 ===")
# それぞれのインスタンスが異なる動作を実行
taro.buy_juice("パイナップルジュース")
hanako.eat_coffee_jelly()
jiro.write_code("JavaScript")

taro.wash_dishes(3)
hanako.shout("Yay!")
jiro.buy_juice()

print("\n=== プロパティへの直接アクセス ===")
print(f"Taro's height: {taro.height}cm")
print(f"Hanako's weight: {hanako.weight}kg")
print(f"Jiro's name: {jiro.name}")

print("\n=== プロパティの変更も可能 ===")
taro.height = 176  # 身長が1cm伸びた
print(f"Taro's new height: {taro.height}cm")