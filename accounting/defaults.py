from .models import TafsiliAccount,AccountGroup,BasicAccount,MoeinAccount
from utility.constants import SUCCEED,FAILED


def init_all_accounts_list_1():
    account_groups=[
            
        {"name":"دارایی جاری",'color':'success','code':"1","basic_accounts":[
            {"name":"	موجودی نقد و بانک",'color':'success','code':"11","moein_accounts":[
                {"name":"صندوق",'color':'success','code':"11-1","moein_accounts":[
                    {"name":"ریالی",'color':'success','code':"11-1-1"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                ]},
   
                {"name":"بانک",'color':'info','code':"11-2","moein_accounts":[
 
                    {"name":"بانک ملی",'color':'info','code':"11-2-1","tafsili_accounts":[
                        {"name":"حساب بانک ملی 0101581354009 به نام موسسه تست",'color':'info','code':"11-2-1-1"},
                    ]},

                    {"name":"بانک رفاه کارگران",'color':'warning','code':"11-2-2","tafsili_accounts":[
    
                    ]},

                    {"name":"بانک صادرات",'color':'dark','code':"11-2-3","tafsili_accounts":[
    
                    ]},
                    {"name":"بانک ملت",'color':'dark','code':"11-2-4","tafsili_accounts":[
    
                    ]},
                    {"name":"بانک تجارت",'color':'success','code':"11-2-5","tafsili_accounts":[
        
                    ]},
                ]},
                
               
                 {"name":"تنخواه",'color':'success','code':"11-3","accounts":[
     
                ]},
            ]},
            {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"12","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102","tafsili_accounts":[
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                ]}
            ]},
            {"name":"حساب ها و اسناد دریافتنی تجاری",'color':'success','code':"13","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"131","tafsili_accounts":[
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"1311"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"1312"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"1313"},
                ]}
            ]},
            {"name":"سایر حساب های دریافتنی تجاری",'color':'success','code':"14","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102","tafsili_accounts":[
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                ]}
            ]},
            {"name":"جاری شرکا",'color':'success','code':"15","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102","tafsili_accounts":[
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                ]}
            ]},
            {"name":"موجودی مواد و کالا",'color':'success','code':"16","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102","tafsili_accounts":[
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                ]}
            ]},
            {"name":"سفارشات و پیش پرداختها",'color':'success','code':"17","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102","tafsili_accounts":[
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
                ]}
            ]},
            {"name":"سپرده هایمان نزد دیگران",'color':'success','code':"18"},
            {"name":"دارایی های نگهداری شده برای فروش",'color':'success','code':"19"},
            ]},
        {"name":"دارایی های غیر جاری",'color':'success','code':"2","basic_accounts":[
            {"name":"دارایی های ثابت مشهود",'color':'success','code':"21","moein_accounts":[
                {"name":"زمین",'color':'success','code':"111/10","moein_accounts":[
                    {"name":"ریالی",'color':'success','code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                ]},


                {"name":"ساختمان",'color':'success','code':"111/10","accounts":[
                    {"name":"ریالی",'color':'success','code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                ]},

                

                {"name":"ماشین آلات و تجهیزات",'color':'success','code':"111/10","accounts":[
                    {"name":"ریالی",'color':'success','code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                ]},
                 

                 
                {"name":"تاسیسات",'color':'success','code':"111/10","accounts":[
                    {"name":"ریالی",'color':'success','code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                ]},
                 

                 
                {"name":"وسایط نقلیه",'color':'success','code':"111/10","accounts":[
                    {"name":"ریالی",'color':'success','code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                ]},
                 

                 
                {"name":"اثاثه و منصوبات",'color':'success','code':"111/10","accounts":[
                    {"name":"ریالی",'color':'success','code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                ]},
                
                 
                {"name":"ابزار آلات",'color':'success','code':"111/10","accounts":[
                    {"name":"ریالی",'color':'success','code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                ]},
                
                 
                {"name":"قالب ها",'color':'success','code':"111/10","accounts":[
                    {"name":"ریالی",'color':'success','code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                ]},
                
            ]},
            {"name":"موجودی نقد و بانک",'color':'success','code':"101"},
            ]},
        {"name":"بدهی های جاری	",'color':'danger','code':"3","basic_accounts":[
            {"name":"aaaaaa",'color':'success','code':"102","moein_accounts":[
                {"name":"صندوق",'color':'success','code':"111/10","accounts":[
                    {"name":"ریالی",'color':'success','code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                ]},
            ]},

            {"name":"bbbbb",'color':'success','code':"102","moein_accounts":[
                {"name":"صندوق",'color':'success','code':"111/10","accounts":[
                    {"name":"ریالی",'color':'success','code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                ]},
            ]},

            {"name":"ccccc",'color':'success','code':"102","moein_accounts":[
                {"name":"صندوق",'color':'success','code':"111/10","accounts":[
                    {"name":"ریالی",'color':'success','code':"1111/10/01"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                ]},
            ]},

 


            ]},
        {"name":"بدهی های بلند مدت (غیرجاری)",'color':'success','code':"4","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
            {"name":"موجودی نقد و بانک",'color':'success','code':"101"},
            ]},
        {"name":"حقوق صاحبان سهام",'color':'success','code':"5","basic_accounts":[
            {"name":"سرمایه",'color':'success','code':"51","moein_accounts":[
                {"name":"سرمایه",'color':'success','code':"5101","tafsili_accounts":[

                    {"name":"حسین مقیمی",'color':'success','code':"51011"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                    # {"name":"aaaaaaaaa",'color':'success','code':"102"},
                ],},
            ]},
            {"name":"افزایش سرمایه‌ی در جریان",'color':'success','code':"52",'moein_accounts':[
                {"name":"افزایش سرمایه از محل مطالبات سهام‌داران",'color':'success','code':"5201",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"افزایش سرمایه از محل آورده‌ی نقدی سهام‌داران",'color':'success','code':"5202",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                
            ]},
            {"name":"اندوخته‌ی صرف سهام",'color':'success','code':"53",'moein_accounts':[
                {"name":"اندوخته‌ی صرف سهام افزایش سرمایه‌ی ...",'color':'success','code':"5301",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"اندوخته‌ی صرف سهام افزایش سرمایه‌ی ...	",'color':'success','code':"5302",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                
            ]},
            {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
            {"name":"موجودی نقد و بانک",'color':'success','code':"101"},
            ]},
        {"name":"درآمد ها",'color':'info','code':"6","basic_accounts":[
            {"name":"درآمد فروش",'color':'success','code':"61",'moein_accounts':[
                {"name":"درآمد ارائه‌ی خدمات",'color':'success','code':"6101",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"درآمد خدمات از ...",'color':'success','code':"6102",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                
            ]},

            {"name":"ارائه خدمات",'color':'success','code':"61",'moein_accounts':[
                {"name":"درآمد ارائه‌ی خدمات",'color':'success','code':"6101",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"درآمد خدمات از ...",'color':'success','code':"6102",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                
            ]},

            {"name":"برگشت از فروش",'color':'success','code':"61",'moein_accounts':[
                {"name":"درآمد ارائه‌ی خدمات",'color':'success','code':"6101",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"درآمد خدمات از ...",'color':'success','code':"6102",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                
            ]},

            {"name":"تخفیفات فروش",'color':'success','code':"61",'moein_accounts':[
                {"name":"درآمد ارائه‌ی خدمات",'color':'success','code':"6101",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"درآمد خدمات از ...",'color':'success','code':"6102",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                
            ]},

            {"name":"سایر درآمدهای عملیاتی",'color':'success','code':"62",'moein_accounts':[
                {"name":"سایر درآمد خدمات",'color':'success','code':"6201",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                 {"name":"سایر درآمدهای عملیاتی",'color':'success','code':"6202",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                
            ]},

            
        ]},
        {"name":"بهای تمام شده کالای فروش رفته و خدمات ارائه شده",'color':'primary','code':"7","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
            {"name":"موجودی نقد و بانک",'color':'success','code':"101"},
            ]},
        {"name":"هزینه ها",'color':'danger','code':"7","basic_accounts":[
            {"name":"هزینه ی حقوق و دستمزد",'color':'success','code':"71",'moein_accounts':[
                {"name":"حقوق پایه",'color':'success','code':"7101",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"اضافه‌کاری",'color':'success','code':"7102",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"خواربار و مسکن	",'color':'success','code':"7103",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"حق اولاد",'color':'success','code':"7104",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"کمک‌هزینه‌ی اقلام مصرفی خانوار	",'color':'success','code':"7105",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"نوبت کاری و شب‌کاری	",'color':'success','code':"7106",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"%23 حق بیمه‌ی سهم کارفرما	",'color':'success','code':"7107",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"عیدی و پاداش",'color':'success','code':"7108",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"حق‌الجذب",'color':'success','code':"7109",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"بازخرید مرخصی استفاده‌نشده",'color':'success','code':"7110",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"مزایای پایان‌خدمت کارکنان",'color':'success','code':"7111",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"کمک‌های غیرنقدی",'color':'success','code':"7112",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
            ],},

            {"name":"هزینه های عملیاتی",'color':'danger','code':"72",'moein_accounts':[
                {"name":"تعمیر و نگهداری ساختمان و تاسیسات",'color':'success','code':"7202",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"تعمیر و نگهداری ماشین‌آلات و تجهیزات",'color':'success','code':"7203",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"تعمیر و نگهداری وسائط نقلیه",'color':'success','code':"7204",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},

                {"name":"تعمیر و نگهداری اثاثیه و منصوبات",'color':'success','code':"7205",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},


                {"name":"سوخت و انرژی",'color':'success','code':"7206",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"آب ، برق ، گاز و تلفن",'color':'success','code':"7207",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"ملزومات ، نوشت‌افزار و آگهی",'color':'success','code':"7208",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"آبدارخانه",'color':'success','code':"7209",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"حمل‌ و نقل",'color':'success','code':"7210",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"اجاره‌ی مکان",'color':'success','code':"7211",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"بیمه‌ی دارایی‌ها",'color':'success','code':"7212",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"استهلاک دارایی‌ها",'color':'success','code':"7213",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"ملزومات مصرفی",'color':'success','code':"7214",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"ایاب‌ و‌ ذهاب",'color':'success','code':"7215",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"هزینه‌ی غذای کارکنان",'color':'success','code':"7216",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"هزینه‌ی پیک و پست",'color':'success','code':"7217",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"پوشاک کارکنان	",'color':'success','code':"7218",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"بهداشت و درمان	",'color':'success','code':"7219",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"هزینه‌ی سفر و ماموریت",'color':'success','code':"7220",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"کارمزدهای بانکی",'color':'success','code':"7221",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"هزینه‌های بسته‌بندی",'color':'success','code':"7222",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"حق‌المشاوره",'color':'success','code':"7223",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"هزینه‌های رایانه‌ای",'color':'success','code':"7224",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"هزینه‌ی ثبتی، حق تمبر و وکالت",'color':'success','code':"7225",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
            ],},

            {"name":"هزینه‌ های توزیع و فروش",'color':'info','code':"73",'moein_accounts':[
                {"name":"هزینه‌های تبلیغات، بازاریابی، کاتالوگ و بروشور	",'color':'success','code':"7301",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"هزینه‌ی انبار داری",'color':'success','code':"7302",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
 

                {"name":"کمیسیون‌های پرداختی",'color':'success','code':"7303",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
                {"name":"هزینه‌ی حمل‌ونقل کالای فروش‌ رفته",'color':'success','code':"7304",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
 
                {"name":"هزینه‌ی مطالبات مشکوک‌الوصول و سوخت‌شده",'color':'success','code':"7305",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
 
 
                {"name":"پاداش هیئت‌ مدیره",'color':'success','code':"7306",'tafsili_accounts':[
                    # {"name":"aaaaaaaaaaaaaaaaaaaaa	",'color':'success','code':"7101/01",},
                ],},
            ],},
            {"name":"سایر اقلام عملیاتی",'color':'muted','code':"74"},
            {"name":"هزینه های مالی",'color':'success','code':"75"},
            {"name":"سایر درآمدها و هزینه های غیرعملیاتی",'color':'success','code':"76"},
            ]},
        {"name":"سایر حسابها",'color':'success','code':"9","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'color':'success','code':"102"},
            {"name":"موجودی نقد و بانک",'color':'success','code':"101"},
            ]},
        
    ]       
    return account_groups


def init_all_accounts_list():

    account_groups=[
        
        {'code':"10","name":"دارایی جاری",'color':'success',},
        {'code':"2" ,"name":"دارایی های غیر جاری",'color':'primary'},
        {'code':"3","name":"بدهی های جاری	",'color':'danger', },
        {'code':"4" ,"name":"بدهی های بلند مدت (غیرجاری)",'color':'success', },
        {'code':"5","name":"حقوق صاحبان سهام",'color':'success', },  
        {'code':"6","name":"درآمد ها",'color':'info', },
        {'code':"7","name":"بهای تمام شده کالای فروش رفته و خدمات ارائه شده",'color':'primary', },
        {'code':"8","name":"هزینه ها",'color':'danger', },
        {'code':"9","name":"سایر حسابها",'color':'success', },
        
    ]   

    basic_accounts=[
            #111111111111111111111111111
            {'code':"101","name":"موجودی نقد و بانک",'priority':"100",'account_group_code':"10",'color':'success' },
            {'code':"102","name":"سرمایه گذاری کوتاه مدت",'priority':"100",'account_group_code':"10",'color':'warning'},
            {'code':"103","name":"حساب ها و اسناد دریافتنی تجاری",'priority':"100",'account_group_code':"10",'color':'success'},
            {'code':"104","name":"سایر حساب های دریافتنی تجاری",'priority':"100",'account_group_code':"10",'color':'primary'},
            {'code':"105","name":"موجودی مواد و کالا",'priority':"100",'account_group_code':"10",'color':'success'},
            {'code':"106","name":"جاری شرکا",'priority':"100",'account_group_code':"10",'color':'success'},
            {'code':"107","name":"سفارشات و پیش پرداختها",'priority':"100",'account_group_code':"10",'color':'success'},
            {'code':"108","name":"سپرده هایمان نزد دیگران",'priority':"100",'account_group_code':"10",'color':'success'},
            {'code':"109","name":"دارایی های نگهداری شده برای فروش",'priority':"100",'account_group_code':"10",'color':'success'},
            #222222222222222222222222
            {'code':"201","name":"دارایی های ثابت مشهود",'color':'primary','priority':"100",'account_group_code':"2"}, 
            {'code':"202","name":"استهلاک انباشته دارایی های ثابت مشهود",'color':'primary','priority':"100",'account_group_code':"2" }, 
            {'code':"203","name":"دارایی های در جریان تکمیل",'color':'primary','priority':"100",'account_group_code':"2"}, 
            {'code':"204","name":"دارایی های نامشهود",'color':'primary','priority':"100",'account_group_code':"2"}, 
            {'code':"205","name":"سرمایه گذاری های بلند مدت",'color':'primary','priority':"100",'account_group_code':"2" },  
            #3333333333333333333333333
            {'code':"301","name":"ﺣﺴﺎب ﻫﺎ و اﺳﻨﺎد ﭘﺮداﺧﺘﻨﯽ ﺗﺠﺎری",'color':'danger','priority':"100",'account_group_code':"3"},  
            {'code':"302","name":"ﺳﺎﯾﺮ ﺣﺴﺎب ﻫﺎ و اﺳﻨﺎد ﭘﺮداﺧﺘﻨﯽ",'color':'danger','priority':"100",'account_group_code':"3"},  
            {'code':"303","name":"ﺳﻔﺎرﺷﺎت و ﭘﯿﺶ درﯾﺎﻓﺖ ﻫﺎ",'color':'danger','priority':"100",'account_group_code':"3"},  
            {'code':"304","name":"ذﺧﯿﺮه ﻣﺎﻟﯿﺎت",'color':'danger','priority':"100",'account_group_code':"3"},  
            {'code':"305","name":"ﺳﻮد ﺳﻬﺎم ﭘﺮداﺧﺘﻨﯽ",'color':'danger','priority':"100",'account_group_code':"3"},  
            {'code':"306","name":"ﺳﭙﺮده ﻫﺎی ﭘﺮداﺧﺘﻨﯽ",'color':'danger','priority':"100",'account_group_code':"3"},  
            {'code':"307","name":"ﺗﺴﻬﯿﻼت و اﻋﺘﺒﺎرات ﻣﺎﻟﯽ درﯾﺎﻓﺘﯽ ﮐﻮﺗﺎه ﻣﺪت",'color':'danger','priority':"100",'account_group_code':"3" },  
            {'code':"308","name":"ذﺧﺎﯾﺮ",'color':'danger','priority':"100",'account_group_code':"3" },  
            #4444444444444444444444444
            {'code':"401","name":"ﺣﺴﺎب ﻫﺎ و اﺳﻨﺎد ﭘﺮداﺧﺘﻨﯽ ﺑﻠﻨﺪ ﻣﺪت ﺗﺠﺎری",'color':'secondary','priority':"100",'account_group_code':"4" },  
            {'code':"402","name":"ﺳﺎﯾﺮ ﺣﺴﺎب ﻫﺎ و اﺳﻨﺎد ﭘﺮداﺧﺘﻨﯽ ﺑﻠﻨﺪﻣﺪت",'color':'secondary','priority':"100",'account_group_code':"4" },  
            {'code':"403","name":"ﺗﺴﻬﯿﻼت و اﻋﺘﺒﺎرات ﻣﺎﻟﯽ درﯾﺎﻓﺘﯽ ﺑﻠﻨﺪﻣﺪت",'color':'secondary','priority':"100",'account_group_code':"4" },  
            {'code':"404","name":"ذﺧﯿﺮه ﻣﺰاﯾﺎی ﭘﺎﯾﺎن ﺧﺪﻣﺖ ﮐﺎرﮐﻨﺎن",'color':'secondary','priority':"100",'account_group_code':"4" },  
            {'code':"405","name":"درآﻣﺪﻫﺎی اﻧﺘﻘﺎﻟﯽ ﺑﻪ دوره ﻫﺎی آﺗﯽ",'color':'secondary','priority':"100",'account_group_code':"4" },  
            #5555555555555555555555555
            {'code':"501","name":"ﺳﺮﻣﺎﯾﻪ ﭘﺮداﺧﺖ ﺷﺪه",'color':'info','priority':"100",'account_group_code':"5" },  
            {'code':"502","name":"اﻧﺪوﺧﺘﻪ ﻗﺎﻧﻮﻧﯽ",'color':'success','priority':"100",'account_group_code':"5" },  
            {'code':"503","name":"ﺳﺎﯾﺮ اﻧﺪوﺧﺘﻪ ﻫﺎ",'color':'info','priority':"100",'account_group_code':"5" },  
            {'code':"504","name":"ﻣﺎزاد ﺗﺠﺪﯾﺪ ارزﯾﺎﺑﯽ داراﯾﯽ ﻫﺎی ﺛﺎﺑﺖ ﻣﺸﻬﻮد",'color':'success','priority':"100",'account_group_code':"5" },  
            {'code':"505","name":"سود ( زیان ) انباشته",'color':'info','priority':"100",'account_group_code':"5" },  
            #6666666666666666666666666
            {'code':"601","name":"فروش", 'color':'info','priority':"100",'account_group_code':"6" },  
            {'code':"602","name":"درآﻣﺪ ﺣﺎﺻﻞ از اراﺋﻪ ﺧﺪﻣﺎت",'color':'info','priority':"100",'account_group_code':"6" },  
            {'code':"603","name":"ﺳﺎﯾﺮ درآﻣﺪﻫﺎی ﻋﻤﻠﯿﺎﺗﯽ",'color':'info','priority':"100",'account_group_code':"6" },  
            {'code':"604","name":"ﺳﺎﯾﺮ درآﻣﺪﻫﺎی ﻏﯿﺮ ﻋﻤﻠﯿﺎﺗﯽ",'color':'info','priority':"100",'account_group_code':"6" },  
            #777777777777777777777777
            {'code':"701","name":"ﺑﻬﺎی ﺗﻤﺎم ﺷﺪه ﮐﺎﻻی ﻓﺮوش رﻓﺘﻪ داﺧﻠﯽ",'color':'primary','priority':"100",'account_group_code':"7" },  
            {'code':"702","name":"ﺑﻬﺎی ﺗﻤﺎم ﺷﺪه ﮐﺎﻻی ﻓﺮوش رﻓﺘﻪ ﺧﺎرﺟﯽ",'color':'primary','priority':"100",'account_group_code':"7" },  
            {'code':"703","name":"ﺑﻬﺎی ﺗﻤﺎم ﺷﺪه ﺧﺪﻣﺎت اراﺋﻪ ﺷﺪه",'color':'primary','priority':"100",'account_group_code':"7" },  
            #888888888888888888888888
            {'code':"801","name":"هزﯾﻨﻪ ﺣﻘﻮق و دﺳﺘﻤﺰد ﮐﺎرﮐﻨﺎن ﻏﯿﺮ ﺗﻮﻟﯿﺪی",'color':'danger','priority':"100",'account_group_code':"8" },  
            {'code':"802","name":"هزﯾﻨﻪ ﻫﺎی ﻋﻤﻠﯿﺎﺗﯽ",'color':'danger','priority':"100",'account_group_code':"8" },  
            {'code':"803","name":"سایر هزﯾﻨﻪ ﻫﺎی ﻋﻤﻠﯿﺎﺗﯽ",'color':'danger','priority':"100",'account_group_code':"8" },  
            {'code':"804","name":"هزینه ﻫﺎی ﻣﺎﻟﯽ",'color':'danger','priority':"100",'account_group_code':"8" },  
            {'code':"805","name":"هزینه ﻫﺎی ﻏﯿﺮ ﻋﻤﻠﯿﺎﺗﯽ",'color':'danger','priority':"100",'account_group_code':"8" },  
            #999999999999999999999999
            {'code':"901","name":"ﺣﺴﺎب ﻫﺎی اﻧﺘﻈﺎﻣﯽ",'color':'secondary','priority':"100",'account_group_code':"9" },  
            {'code':"902","name":"طرف ﺣﺴﺎب ﻫﺎی اﻧﺘﻈﺎﻣﯽ",'color':'secondary','priority':"100",'account_group_code':"9" },  
            {'code':"903","name":"ﺗﺮاز اﻓﺘﺘﺎﺣیه",'color':'secondary','priority':"100",'account_group_code':"9" },  
            {'code':"904","name":"ﺗﺮاز اختتامیه",'color':'secondary','priority':"100",'account_group_code':"9" },  

    ]  
    moein_accounts=[
            #101
            {'code':"10101","name":"صندوق",'color':'success','priority':"100",'basic_account_code':"101" },
            {'code':"10102","name":"بانک",'color':'success','priority':"100",'basic_account_code':"101" },
            {'code':"10103","name":"تنخواه",'color':'success','priority':"100",'basic_account_code':"101" },
            {'code':"10104","name":"وجوه در راه",'color':'success','priority':"100",'basic_account_code':"101" },
            
            
            #102
            {'code':"10201","name":"سهام شرکتهای پذیرفته شده در بورس",'color':'warning','priority':"100",'basic_account_code':"102" },
            {'code':"10202","name":"اوراق مشارکت",'color':'warning','priority':"100",'basic_account_code':"102" },
            {'code':"10203","name":"سرمایه گذاری در سهام شرکتها",'color':'warning','priority':"100",'basic_account_code':"102" },
            {'code':"10204","name":"سپرده های سرمایه گذاری کوتاه مدت",'color':'warning','priority':"100",'basic_account_code':"102" },
            #103
            {'code':"10301","name":"اسناد دریافتنی تجاری / شرکت ها",'color':'success','priority':"100",'basic_account_code':"103" },
            {'code':"10302","name":"اسناد دریافتنی تجاری / اشخاص",'color':'success','priority':"100",'basic_account_code':"103" },
            {'code':"10303","name":"حسابهای دریافتنی تجاری / شرکت ها",'color':'success','priority':"100",'basic_account_code':"103" },
            {'code':"10304","name":"حسابهای دریافتنی تجاری / اشخاص",'color':'success','priority':"100",'basic_account_code':"103" },
            #104
            {'code':"10401","name":"کارکنان ( وام مساعده )",'color':'primary','priority':"100",'basic_account_code':"104" },
            {'code':"10402","name":"اسناد دریافتنی",'color':'primary','priority':"100",'basic_account_code':"104" },
            {'code':"10403","name":"سپرده های موقت",'color':'primary','priority':"100",'basic_account_code':"104" },
            {'code':"10404","name":"سود سهام دریافتنی",'color':'primary','priority':"100",'basic_account_code':"104" },
            {'code':"10405","name":"طلب از شرکت گروهها",'color':'primary','priority':"100",'basic_account_code':"104" },
            {'code':"10406","name":"طلب از سایر اشخاص وابسته",'color':'primary','priority':"100",'basic_account_code':"104" },
            {'code':"10407","name":"سایر اشخاص",'color':'primary','priority':"100",'basic_account_code':"104" },
            #105
            {'code':"10501","name":"کالای ساخته شده",'color':'success','priority':"100",'basic_account_code':"105" },
            {'code':"10502","name":"کالای در جریان ساخت",'color':'success','priority':"100",'basic_account_code':"105" },
            {'code':"10503","name":"مواد اولیه و بسته بندی",'color':'success','priority':"100",'basic_account_code':"105" },
            {'code':"10504","name":"قطعات و لوازم یدکی",'color':'success','priority':"100",'basic_account_code':"105" },
            {'code':"10505","name":"سایر موجودی ها",'color':'success','priority':"100",'basic_account_code':"105" },
            {'code':"10506","name":"کالای در راه",'color':'success','priority':"100",'basic_account_code':"105" },
            #106
            #107

            #201
            {'code':"201/01","name":"زمین",'color':'success','priority':"100",'basic_account_code':"201" },
            {'code':"201/02","name":"ساختمان",'color':'success','priority':"100",'basic_account_code':"201" },
            {'code':"201/03","name":"تاسیسات",'color':'success','priority':"100",'basic_account_code':"201" },
            {'code':"201/04","name":"ماشین آلات و تجهیزات ",'color':'success','priority':"100",'basic_account_code':"201" },
            {'code':"201/05","name":"اثاثه و منصوبات",'color':'success','priority':"100",'basic_account_code':"201" },
            {'code':"201/06","name":"ابزار آلات",'color':'success','priority':"100",'basic_account_code':"201" },
            {'code':"201/07","name":"وسایل نقلیه",'color':'success','priority':"100",'basic_account_code':"201" },
            {'code':"201/08","name":"دارایی ها در دست تکمیل",'color':'success','priority':"100",'basic_account_code':"201" },
            {'code':"201/09","name":"سفارشات و پیش پرداخت های سرمایه ای ",'color':'success','priority':"100",'basic_account_code':"201" },
            {'code':"201/10","name":"اقلام سرمایه ای در انبار",'color':'success','priority':"100",'basic_account_code':"201" },
            #204
            {'code':"20401","name":"حق امتیاز استفاده از خدمات عمومی",'color':'success','priority':"100",'basic_account_code':"204" },
            {'code':"20402","name":"سرقفلی محل کسب",'color':'success','priority':"100",'basic_account_code':"204" },
            {'code':"20403","name":"سایر داراییهای نا مشهود",'color':'success','priority':"100",'basic_account_code':"204" },

            #205


            #501
            {'code':"50101","name":"سرمایه",'color':'success','priority':"100",'basic_account_code':"501" }, 

    ]
    moein2_accounts=[
        
            {"name":"صندوق فروشگاه",'code':"1010101",'color':'success','priority':"100",'moein_account_code':"10101" },
            {"name":"صندوق دفتر",'code':"1010102",'color':'success','priority':"100",'moein_account_code':"10101" },

            {"name":"بانک ملی",'code':"1010201",'color':'success','priority':"100",'moein_account_code':"10102" },
            {"name":"بانک رفاه",'code':"1010202",'color':'success','priority':"100",'moein_account_code':"10102" },
            {"name":"بانک ملت",'code':"1010203",'color':'success','priority':"100",'moein_account_code':"10102" },
            {"name":"بانک تجارت",'code':"1010204",'color':'success','priority':"100",'moein_account_code':"10102" },

            
            #50101
            {'code':"5010101","name":"نقدی",'color':'success','priority':"100",'moein_account_code':"50101" },
            {'code':"5010102","name":"تعهد شده",'color':'success','priority':"100",'moein_account_code':"50101" },
    ]
    tafsili_accounts=[
            {"name":"صندوق بی ضرر",'code':"1011/1/1",'color':'success','priority':"100",'moein_account_code':"1010101" },
            {"name":"صندوق درست",'code':"1011/1/2",'color':'success','priority':"100",'moein_account_code':"1010101" },
            {"name":"صندوق شرباف",'code':"1011/1/1",'color':'success','priority':"100",'moein_account_code':"1010102" },
            {"name":"صندوق معتبر",'code':"1011/1/2",'color':'success','priority':"100",'moein_account_code':"1010102" },

            {"name":"بانک ملی به شماره 0101581354009",'code':"1012/1/1",'color':'success','priority':"100",'moein_account_code':"1010201" },

            {"name":"حسین مقیمی",'code':"1000001",'color':'success','priority':"100",'moein_account_code':"5010101" },
            {"name":"داوود قانع",'code':"1000002",'color':'success','priority':"100",'moein_account_code':"5010101" },

    ]
    return account_groups,basic_accounts,moein_accounts,moein2_accounts,tafsili_accounts

