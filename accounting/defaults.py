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
        
        {"name":"دارایی جاری",'color':'success','code':"1",},
        {"name":"دارایی های غیر جاری",'color':'primary','code':"2" },
        {"name":"بدهی های جاری	",'color':'danger','code':"3" },
        {"name":"بدهی های بلند مدت (غیرجاری)",'color':'success','code':"4"  },
        {"name":"حقوق صاحبان سهام",'color':'success','code':"5" },  
        {"name":"درآمد ها",'color':'info','code':"6" },
        {"name":"بهای تمام شده کالای فروش رفته و خدمات ارائه شده",'color':'primary','code':"7" },
        {"name":"هزینه ها",'color':'danger','code':"8" },
        {"name":"سایر حسابها",'color':'success','code':"9" },
        
    ]   

    basic_accounts=[
            #111111111111111111111111111
            {"name":"موجودی نقد و بانک",'code':"101",'account_group_code':1,'color':'success' },
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102",'account_group_code':1,'color':'success'  },
            {"name":"حساب ها و اسناد دریافتنی تجاری",'code':"103",'account_group_code':1,'color':'success' },
            {"name":"سایر حساب های دریافتنی تجاری",'code':"104",'account_group_code':1,'color':'success'  },
            {"name":"موجودی مواد و کالا",'code':"105",'account_group_code':1,'color':'success'  },
            {"name":"جاری شرکا",'code':"106",'account_group_code':1,'color':'success'  },
            {"name":"سفارشات و پیش پرداختها",'code':"107",'account_group_code':1,'color':'success' },
            {"name":"سپرده هایمان نزد دیگران",'code':"108",'account_group_code':1,'color':'success'},
            {"name":"دارایی های نگهداری شده برای فروش",'code':"109",'account_group_code':1,'color':'success'},
            #222222222222222222222222
            {"name":"دارایی های ثابت مشهود",'code':"201",'color':'primary','account_group_code':2 }, 
            {"name":"استهلاک انباشته دارایی های ثابت مشهود",'code':"202",'color':'primary','account_group_code':2 }, 
            {"name":"دارایی های در جریان تکمیل",'code':"203",'color':'primary','account_group_code':2 }, 
            {"name":"دارایی های نامشهود",'code':"204",'color':'primary','account_group_code':2 }, 
            {"name":"سرمایه گذاری های بلند مدت",'code':"205",'color':'primary','account_group_code':2 },  
            #3333333333333333333333333
            {"name":"ﺣﺴﺎب ﻫﺎ و اﺳﻨﺎد ﭘﺮداﺧﺘﻨﯽ ﺗﺠﺎری",'code':"301",'color':'danger','account_group_code':"3" },  
            {"name":"ﺳﺎﯾﺮ ﺣﺴﺎب ﻫﺎ و اﺳﻨﺎد ﭘﺮداﺧﺘﻨﯽ",'code':"302",'color':'danger','account_group_code':"3" },  
            {"name":"ﺳﻔﺎرﺷﺎت و ﭘﯿﺶ درﯾﺎﻓﺖ ﻫﺎ",'code':"303",'color':'danger','account_group_code':"3" },  
            {"name":"ذﺧﯿﺮه ﻣﺎﻟﯿﺎت",'code':"304",'color':'danger','account_group_code':"3" },  
            {"name":"ﺳﻮد ﺳﻬﺎم ﭘﺮداﺧﺘﻨﯽ",'code':"305",'color':'danger','account_group_code':"3" },  
            {"name":"ﺳﭙﺮده ﻫﺎی ﭘﺮداﺧﺘﻨﯽ",'code':"306",'color':'danger','account_group_code':"3" },  
            {"name":"ﺗﺴﻬﯿﻼت و اﻋﺘﺒﺎرات ﻣﺎﻟﯽ درﯾﺎﻓﺘﯽ ﮐﻮﺗﺎه ﻣﺪت",'code':"307",'color':'danger','account_group_code':"3" },  
            {"name":"ذﺧﺎﯾﺮ",'code':"308",'color':'danger','account_group_code':"3" },  
            #4444444444444444444444444
            {"name":"ﺣﺴﺎب ﻫﺎ و اﺳﻨﺎد ﭘﺮداﺧﺘﻨﯽ ﺑﻠﻨﺪ ﻣﺪت ﺗﺠﺎری",'code':"401",'color':'secondary','account_group_code':"4" },  
            {"name":"ﺳﺎﯾﺮ ﺣﺴﺎب ﻫﺎ و اﺳﻨﺎد ﭘﺮداﺧﺘﻨﯽ ﺑﻠﻨﺪﻣﺪت",'code':"402",'color':'secondary','account_group_code':"4" },  
            {"name":"ﺗﺴﻬﯿﻼت و اﻋﺘﺒﺎرات ﻣﺎﻟﯽ درﯾﺎﻓﺘﯽ ﺑﻠﻨﺪﻣﺪت",'code':"403",'color':'secondary','account_group_code':"4" },  
            {"name":"ذﺧﯿﺮه ﻣﺰاﯾﺎی ﭘﺎﯾﺎن ﺧﺪﻣﺖ ﮐﺎرﮐﻨﺎن",'code':"404",'color':'secondary','account_group_code':"4" },  
            {"name":"درآﻣﺪﻫﺎی اﻧﺘﻘﺎﻟﯽ ﺑﻪ دوره ﻫﺎی آﺗﯽ",'code':"405",'color':'secondary','account_group_code':"4" },  
            #5555555555555555555555555
            {"name":"ﺳﺮﻣﺎﯾﻪ ﭘﺮداﺧﺖ ﺷﺪه",'code':"501",'color':'secondary','account_group_code':"5" },  
            {"name":"اﻧﺪوﺧﺘﻪ ﻗﺎﻧﻮﻧﯽ",'code':"502",'color':'secondary','account_group_code':"5" },  
            {"name":"ﺳﺎﯾﺮ اﻧﺪوﺧﺘﻪ ﻫﺎ",'code':"503",'color':'secondary','account_group_code':"5" },  
            {"name":"ﻣﺎزاد ﺗﺠﺪﯾﺪ ارزﯾﺎﺑﯽ داراﯾﯽ ﻫﺎی ﺛﺎﺑﺖ ﻣﺸﻬﻮد",'code':"504",'color':'secondary','account_group_code':"5" },  
            {"name":"سود ( زیان ) انباشته",'code':"505",'color':'secondary','account_group_code':"5" },  
            #6666666666666666666666666
            {"name":"فروش",'code':"601",'color':'secondary','account_group_code':"6" },  
            {"name":"درآﻣﺪ ﺣﺎﺻﻞ از اراﺋﻪ ﺧﺪﻣﺎت",'code':"602",'color':'secondary','account_group_code':"6" },  
            {"name":"ﺳﺎﯾﺮ درآﻣﺪﻫﺎی ﻋﻤﻠﯿﺎﺗﯽ",'code':"603",'color':'secondary','account_group_code':"6" },  
            {"name":"ﺳﺎﯾﺮ درآﻣﺪﻫﺎی ﻏﯿﺮ ﻋﻤﻠﯿﺎﺗﯽ",'code':"604",'color':'secondary','account_group_code':"6" },  
            #777777777777777777777777
            {"name":"ﺑﻬﺎی ﺗﻤﺎم ﺷﺪه ﮐﺎﻻی ﻓﺮوش رﻓﺘﻪ داﺧﻠﯽ",'code':"701",'color':'secondary','account_group_code':"7" },  
            {"name":"ﺑﻬﺎی ﺗﻤﺎم ﺷﺪه ﮐﺎﻻی ﻓﺮوش رﻓﺘﻪ ﺧﺎرﺟﯽ",'code':"702",'color':'secondary','account_group_code':"7" },  
            {"name":"ﺑﻬﺎی ﺗﻤﺎم ﺷﺪه ﺧﺪﻣﺎت اراﺋﻪ ﺷﺪه",'code':"703",'color':'secondary','account_group_code':"7" },  
            #888888888888888888888888
            {"name":"هزﯾﻨﻪ ﺣﻘﻮق و دﺳﺘﻤﺰد ﮐﺎرﮐﻨﺎن ﻏﯿﺮ ﺗﻮﻟﯿﺪی",'code':"801",'color':'danger','account_group_code':"8" },  
            {"name":"هزﯾﻨﻪ ﻫﺎی ﻋﻤﻠﯿﺎﺗﯽ",'code':"802",'color':'danger','account_group_code':"8" },  
            {"name":"سایر هزﯾﻨﻪ ﻫﺎی ﻋﻤﻠﯿﺎﺗﯽ",'code':"803",'color':'danger','account_group_code':"8" },  
            {"name":"هزینه ﻫﺎی ﻣﺎﻟﯽ",'code':"804",'color':'danger','account_group_code':"8" },  
            {"name":"هزینه ﻫﺎی ﻏﯿﺮ ﻋﻤﻠﯿﺎﺗﯽ",'code':"805",'color':'danger','account_group_code':"8" },  
            #999999999999999999999999
            {"name":"ﺣﺴﺎب ﻫﺎی اﻧﺘﻈﺎﻣﯽ",'code':"901",'color':'secondary','account_group_code':"9" },  
            {"name":"طرف ﺣﺴﺎب ﻫﺎی اﻧﺘﻈﺎﻣﯽ",'code':"902",'color':'secondary','account_group_code':"9" },  
            {"name":"ﺗﺮاز اﻓﺘﺘﺎﺣیه",'code':"903",'color':'secondary','account_group_code':"9" },  
            {"name":"ﺗﺮاز اختتامیه",'code':"904",'color':'secondary','account_group_code':"9" },  

    ]  
    moein_accounts=[
        
            {"name":"صندوق",'code':"1011",'color':'success','basic_account_code':"101" },
            {"name":"بانک",'code':"1012",'color':'success','basic_account_code':"101" },
            {"name":"تنخواه",'code':"1013",'color':'success','basic_account_code':"101" },
            {"name":"وجوه در راه",'code':"1014",'color':'success','basic_account_code':"101" },
            
            
            
            {"name":"سهام شرکتهای پذیرفته شده در بورس",'code':"1021",'color':'success','basic_account_code':"102" },
            {"name":"اوراق مشارکت",'code':"1022",'color':'success','basic_account_code':"102" },
            {"name":"سرمایه گذاری در سهام شرکتها",'code':"1023",'color':'success','basic_account_code':"102" },
            {"name":"سپرده های سرمایه گذاری کوتاه مدت",'code':"1024",'color':'success','basic_account_code':"102" },
    ]
    moein2_accounts=[
        
            {"name":"صندوق فروشگاه",'code':"1011/1",'color':'success','moein_account_code':"1011" },
            {"name":"صندوق دفتر",'code':"1011/2",'color':'success','moein_account_code':"1011" },

            {"name":"بانک ملی",'code':"1012/1",'color':'success','moein_account_code':"1012" },
            {"name":"بانک رفاه",'code':"1012/2",'color':'success','moein_account_code':"1012" },
            {"name":"بانک ملت",'code':"1012/3",'color':'success','moein_account_code':"1012" },
            {"name":"بانک تجارت",'code':"1012/4",'color':'success','moein_account_code':"1012" },
    ]
    tafsili_accounts=[
            {"name":"صندوق بی ضرر",'code':"1011/1/1",'color':'success','moein_account_code':"1011/1" },
            {"name":"صندوق درست",'code':"1011/1/2",'color':'success','moein_account_code':"1011/1" },
            {"name":"صندوق شرباف",'code':"1011/1/1",'color':'success','moein_account_code':"1011/2" },
            {"name":"صندوق معتبر",'code':"1011/1/2",'color':'success','moein_account_code':"1011/2" },

            {"name":"بانک ملی به شماره 0101581354009",'code':"1012/1/1",'color':'success','moein_account_code':"1012/1" },


    ]
    return account_groups,basic_accounts,moein_accounts,moein2_accounts,tafsili_accounts

