from .models import TafsiliAccount,AccountGroup,BasicAccount,MoeinAccount
from utility.constants import SUCCEED,FAILED


def init_all_accounts():
    account_groups=[
            
        {"name":"دارایی جاری",'code':"1","basic_accounts":[
            {"name":"	موجودی نقد و بانک",'code':"11","moein_accounts":[
                {"name":"صندوق",'code':"111/10","accounts":[
                    {"name":"ریالی",'code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                ]},

                
                # {"name":"aaaaaaaaaaaa",'code':"111","accounts":[
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                # ]},
            ]},
            {"name":"سرمایه گذاری کوتاه مدت",'code':"12","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                ]}
            ]},
            {"name":"حساب ها و اسناد دریافتنی تجاری",'code':"13","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                ]}
            ]},
            {"name":"سایر حساب های دریافتنی تجاری",'code':"14","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                ]}
            ]},
            {"name":"جاری شرکا",'code':"15","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                ]}
            ]},
            {"name":"موجودی مواد و کالا",'code':"16","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                ]}
            ]},
            {"name":"سفارشات و پیش پرداختها",'code':"17","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                ]}
            ]},
            {"name":"سپرده هایمان نزد دیگران",'code':"18"},
            {"name":"دارایی های نگهداری شده برای فروش",'code':"19"},
            ]},
        {"name":"دارایی های غیر جاری",'code':"2","basic_accounts":[
            {"name":"دارایی های ثابت مشهود",'code':"21","moein_accounts":[
                {"name":"زمین",'code':"111/10","accounts":[
                    {"name":"ریالی",'code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                ]},


                {"name":"ساختمان",'code':"111/10","accounts":[
                    {"name":"ریالی",'code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                ]},

                

                {"name":"ماشین آلات و تجهیزات",'code':"111/10","accounts":[
                    {"name":"ریالی",'code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                ]},
                 

                 
                {"name":"تاسیسات",'code':"111/10","accounts":[
                    {"name":"ریالی",'code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                ]},
                 

                 
                {"name":"وسایط نقلیه",'code':"111/10","accounts":[
                    {"name":"ریالی",'code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                ]},
                 

                 
                {"name":"اثاثه و منصوبات",'code':"111/10","accounts":[
                    {"name":"ریالی",'code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                ]},
                
                 
                {"name":"ابزار آلات",'code':"111/10","accounts":[
                    {"name":"ریالی",'code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                ]},
                
                 
                {"name":"قالب ها",'code':"111/10","accounts":[
                    {"name":"ریالی",'code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                ]},
                
            ]},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"بدهی های جاری	",'code':"3","basic_accounts":[
            {"name":"aaaaaa",'code':"102","moein_accounts":[
                {"name":"صندوق",'code':"111/10","accounts":[
                    {"name":"ریالی",'code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                ]},
            ]},

            {"name":"bbbbb",'code':"102","moein_accounts":[
                {"name":"صندوق",'code':"111/10","accounts":[
                    {"name":"ریالی",'code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                ]},
            ]},

            {"name":"ccccc",'code':"102","moein_accounts":[
                {"name":"صندوق",'code':"111/10","accounts":[
                    {"name":"ریالی",'code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                    # {"name":"aaaaaaaaa",'code':"102"},
                ]},
            ]},

 


            ]},
        {"name":"بدهی های بلند مدت (غیرجاری)",'code':"4","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"حقوق صاحبان سهام",'code':"5","basic_accounts":[
            {"name":"سرمایه",'code':"51","moein_accounts":[
                {"name":"سرمایه",'code':"5101"},
            ]},
            {"name":"افزایش سرمایه‌ی در جریان",'code':"52",'moein_accounts':[
                {"name":"افزایش سرمایه از محل مطالبات سهام‌داران",'code':"5201",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},

                {"name":"افزایش سرمایه از محل آورده‌ی نقدی سهام‌داران",'code':"5202",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                
            ]},
            {"name":"اندوخته‌ی صرف سهام",'code':"53",'moein_accounts':[
                {"name":"اندوخته‌ی صرف سهام افزایش سرمایه‌ی ...",'code':"5301",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},

                {"name":"اندوخته‌ی صرف سهام افزایش سرمایه‌ی ...	",'code':"5302",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                
            ]},
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"درآمد ها",'code':"6","basic_accounts":[
            {"name":"درآمد خدمات",'code':"61",'moein_accounts':[
                {"name":"درآمد ارائه‌ی خدمات",'code':"6101",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},

                {"name":"درآمد خدمات از ...",'code':"6102",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                
            ]},

            {"name":"سایر درآمدهای عملیاتی",'code':"62",'moein_accounts':[
                {"name":"سایر درآمد خدمات",'code':"6201",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},

                 {"name":"سایر درآمدهای عملیاتی",'code':"6202",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                
            ]},

            
        ]},
        {"name":"بهای تمام شده کالای فروش رفته و خدمات ارائه شده",'code':"7","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"هزینه ها",'code':"7","basic_accounts":[
            {"name":"هزینه‌ی حقوق و دستمزد	",'code':"71",'moein_accounts':[
                {"name":"حقوق پایه",'code':"7101",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},

                {"name":"اضافه‌کاری",'code':"7102",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},

                {"name":"خواربار و مسکن	",'code':"7103",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},

                {"name":"حق اولاد",'code':"7104",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},

                {"name":"کمک‌هزینه‌ی اقلام مصرفی خانوار	",'code':"7105",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},

                {"name":"نوبت کاری و شب‌کاری	",'code':"7106",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"%23 حق بیمه‌ی سهم کارفرما	",'code':"7107",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"عیدی و پاداش",'code':"7108",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"حق‌الجذب",'code':"7109",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"بازخرید مرخصی استفاده‌نشده",'code':"7110",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"مزایای پایان‌خدمت کارکنان",'code':"7111",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"کمک‌های غیرنقدی",'code':"7112",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
            ],},

            {"name":"هزینه‌های عملیاتی",'code':"72",'moein_accounts':[
                {"name":"تعمیر و نگهداری ساختمان و تاسیسات",'code':"7202",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},

                {"name":"تعمیر و نگهداری ماشین‌آلات و تجهیزات",'code':"7203",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},

                {"name":"تعمیر و نگهداری وسائط نقلیه",'code':"7204",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},

                {"name":"تعمیر و نگهداری اثاثیه و منصوبات",'code':"7205",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},


                {"name":"سوخت و انرژی",'code':"7206",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"آب ، برق ، گاز و تلفن",'code':"7207",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"ملزومات ، نوشت‌افزار و آگهی",'code':"7208",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"آبدارخانه",'code':"7209",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"حمل‌ و نقل",'code':"7210",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"اجاره‌ی مکان",'code':"7211",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"بیمه‌ی دارایی‌ها",'code':"7212",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"استهلاک دارایی‌ها",'code':"7213",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"ملزومات مصرفی",'code':"7214",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"ایاب‌ و‌ ذهاب",'code':"7215",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"هزینه‌ی غذای کارکنان",'code':"7216",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"هزینه‌ی پیک و پست",'code':"7217",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"پوشاک کارکنان	",'code':"7218",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"بهداشت و درمان	",'code':"7219",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"هزینه‌ی سفر و ماموریت",'code':"7220",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"کارمزدهای بانکی",'code':"7221",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"هزینه‌های بسته‌بندی",'code':"7222",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"حق‌المشاوره",'code':"7223",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"هزینه‌های رایانه‌ای",'code':"7224",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"هزینه‌ی ثبتی، حق تمبر و وکالت",'code':"7225",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
            ],},

            {"name":"هزینه‌های توزیع و فروش",'code':"73",'moein_accounts':[
                {"name":"هزینه‌های تبلیغات، بازاریابی، کاتالوگ و بروشور	",'code':"7301",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"هزینه‌ی انبار داری",'code':"7302",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
 

                {"name":"کمیسیون‌های پرداختی",'code':"7303",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
                {"name":"هزینه‌ی حمل‌ونقل کالای فروش‌ رفته",'code':"7304",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
 
                {"name":"هزینه‌ی مطالبات مشکوک‌الوصول و سوخت‌شده",'code':"7305",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
 
 
                {"name":"پاداش هیئت‌ مدیره",'code':"7306",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'code':"7101/01",},
                ],},
            ],},
            {"name":"سایر اقلام عملیاتی",'code':"74"},
            {"name":"هزینه‌های مالی",'code':"75"},
            {"name":"سایر درآمدها و هزینه‌های غیرعملیاتی",'code':"76"},
            ]},
        {"name":"سایر حسابها",'code':"9","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        
    ]
    TafsiliAccount.objects.all().delete()
    MoeinAccount.objects.all().delete()
    BasicAccount.objects.all().delete()
    AccountGroup.objects.all().delete() 
    for account_group in account_groups:
        new_account_group=AccountGroup(name=account_group["name"],code=account_group['code'])
        new_account_group.save()
        if 'basic_accounts' in account_group:
            for basic_account in account_group["basic_accounts"]:
                new_basic_account=BasicAccount(name=basic_account["name"],code=basic_account['code'],account_group=new_account_group)
                new_basic_account.save()
                if 'moein_accounts' in basic_account:
                    for moein_account in basic_account["moein_accounts"]:
                        new_moein_account=MoeinAccount(name=moein_account["name"],code=moein_account['code'],basic_account=new_basic_account)
                        new_moein_account.save()
                        if 'tafsili_accounts' in moein_account:
                            for tafsili_account in moein_account["tafsili_accounts"]:
                                new_tafsili_account=TafsiliAccount(title=tafsili_account["name"],code=account['code'],moein_account=new_moein_account)
                                new_tafsili_account.save()
    result=SUCCEED
    message="افزوده شد."
    return (result,message)

