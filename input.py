import datetime


def record_screen_time_data(data: str) -> None:
    with open('data/screen_time.csv', 'a') as file:
        file.write('\n' + data)


def main_menu() -> None:

    report_or_data = input(
        '\nWould you like to see a report or enter data? \n-> options (report, data): ')

    if report_or_data in ('report', 'r'):
        pass

    elif report_or_data in ('data', 'd'):
        data_entry_menu()


def data_entry_menu() -> None:
    date = input(
        '\nEnter the date you wish to start entered data from \n-> format (dd/mm/yyyy) no hanging zeros: ').strip()

    running = True
    while running:
        data = input(
            f'\nEnter the app name, hours used, and minutes used \nCurrent date is {date} \n-> format (name, hours, minutes): ')
        data = data.split(',')
        data = [part.strip() for part in data]
        new_data = date + ', ' + \
            str(data[0]) + ', ' + str(int(data[1])*60 + int(data[2]))
        record_screen_time_data(new_data)

        increment_change_continue = input(
            '\nWould you like to increment the date, alter the date, or continue? \n-> options (increment, alter, continue): ')

        if increment_change_continue in ('i', 'increment'):
            date_parts = date.split('/')
            datetime_date = datetime.date(
                int(date_parts[2]), int(date_parts[1]), int(date_parts[0]))
            new_datetime_date = datetime_date + datetime.timedelta(days=1)
            date = str(new_datetime_date.day) + '/' + \
                str(new_datetime_date.month) + \
                '/' + str(new_datetime_date.year)
            continue

        if increment_change_continue in ('a', 'alter'):
            data_entry_menu()

        continue
