from datetime import date


def get_date():
    def enter_year():
        count = 0
        year = input("year: ")

        for i in year:
            count += 1
        if count != 4:
            print("Wrong year")
            enter_year()

        for i in year:
            if i.isdigit() != True:
                print("Enter numeric")
                enter_year()

        temp_date.append(year)
        enter_month()
    def enter_month():
        pass
    def enter_day():
        pass
    enter_year()

get_date()
