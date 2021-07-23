# order= input('キー入力してください')
# print(order)

# 国クラス
class CountryInstance :
    # 自作関数
    # self=インスタンス自身
    def info(self):
        print(self.name)


# インスタンスを生成
country0 = CountryInstance ()
country1 = CountryInstance ()
country2 = CountryInstance ()
country3 = CountryInstance ()
country4 = CountryInstance ()
country5 = CountryInstance ()
country6 = CountryInstance ()
country7 = CountryInstance ()
country8 = CountryInstance ()
country9 = CountryInstance ()

# インスタンス変数の代入
# 名前コード　リージョン　面積(万km2)　人口(万人) 首都 言語
country1.name = '中国'
country1.code = 'CHN'
country1.region = 'アジア'
country1.area = 960
country1.population = 139000
country1.capital = '北京'
country1.language = '漢語（中国語）'

country1.info()

# インスタンス変数の代入
# 名前コード　リージョン　面積(万km2)　人口(万人) 首都 言語
country2.name = 'アメリカ合衆国'
country2.code = 'USA'
country2.region = '北・中央アメリカ'
country2.area = 962.8
country2.population = 32775
country2.capital = 'ワシントンD.C.'
country2.language = '英語'


# インスタンス変数の代入
# 名前コード　リージョン　面積(万km2)　人口(万人) 首都 言語
country3.name = 'イタリア'
country3.code = 'ITA'
country3.region = 'ヨーロッパ'
country3.area = 30.1
country3.population = 6060
country3.capital = 'ローマ'
country3.language = 'イタリア語'

