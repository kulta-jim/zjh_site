from django import forms


class UserProfileForm(forms.Form):
    area = (('北京市', 0),
            ('天津市', 1),
            ('上海市', 2),
            ('重庆市', 3),
            ('河北省', 4),
            ('山西省', 5),
            ('辽宁省', 6),
            ('吉林省', 7),
            ('黑龙江省', 8),
            ('江苏省', 9),
            ('浙江省', 10),
            ('安徽省', 11),
            ('福建省', 12),
            ('江西省', 13),
            ('山东省', 14),
            ('河南省', 15),
            ('湖北省', 16),
            ('湖南省', 17),
            ('广东省', 18),
            ('海南省', 19),
            ('四川省', 20),
            ('贵州省', 21),
            ('云南省', 22),
            ('陕西省', 23),
            ('甘肃省', 24),
            ('青海省', 25),
            ('西藏自治区', 26),
            ('广西壮族自治区', 27),
            ('内蒙古自治区', 28),
            ('宁夏回族自治区', 1),
            ('新疆维吾尔自治区', 29),
            ('香港特别行政区', 30),
            ('澳门特别行政区', 31),
            ('台湾省', 32))
    telephone = forms.IntegerField(label='telephone', max_length=11, required=False)
    address = forms.ChoiceField(label='address', choices=area, required=True)
    industry = forms.CharField(label='industry', max_length=20, required=False)
    position = forms.CharField(label='position', max_length=20, required=False)
    Introduction = forms.CharField(label='Introduction', max_length=50, required=False)
