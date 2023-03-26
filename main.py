def count_ways(days, absent_days):
    attendance = [[0] * absent_days for _ in range(days + 1)]
    attendance[0][0] = 1

    for day in range(1, days + 1):
        attendance[day][0] = sum(attendance[day - 1])

        for i in range(1, absent_days):
            attendance[day][i] = attendance[day - 1][i - 1]

    total_ways = sum(attendance[days])
    probability_to_miss_ceremony = sum(attendance[days - 1][:3])

    return f"{probability_to_miss_ceremony}/{total_ways}"


def helper_func():
    no_of_days = int(input("Please enter the number of days: "))
    absent_days = int(input("Please enter the number of absent days: "))
    cnt = 1

    while absent_days < 4 and cnt < 5:
        absent_days = int(input("Please enter the number of absent days greater than or equal to 4: "))
        cnt += 1

    if cnt == 5:
        return "The number of limits reached, please try after again some time....!!!"

    return count_ways(no_of_days, absent_days)


if __name__ == '__main__':
    print(helper_func())
