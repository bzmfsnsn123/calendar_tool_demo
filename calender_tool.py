def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def get_month_day(year, month):
    big_month=[1,3,5,7,8,10,12]
    small_month=[4,6,9,11]
    if month in big_month:
        return 31
    elif month in small_month:
        return 30
    elif month==2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return -1

def main():
    while True:
        print("\n=====简易万历年工具=====")
        print("1.判断某一年是否为闰年")
        print("2.查询某年某月一共有多少天")
        print("0.退出程序")
        try:
            choice=int(input("请输入功能序号："))
            if choice==1:
                year=int(input("输入要查询的年份："))
                if year <= 0:
                    print("年份不能为0或负数！")
                if is_leap_year(year):
                    print(f"{year}年是闰年，2月有29天")
                else:
                    print(f"{year}年是平年，2月有28天")

            elif choice==2:
                y=int(input("输入年份："))
                m=int(input("输入月份（1-12）："))
                if y <= 0:
                    print("年份不合法")
                    continue
                if m<1 or m>12:
                    print("年份必须是1-12之间的数字")
                    continue
                days=get_month_day(y,m)
                print(f"{y}年{m}月一共有{days}天")
            elif choice==0:
                print("程序退出！")
                break

        except ValueError:
            print("输入数字不合法！")

if __name__ == "__main__":
    main()