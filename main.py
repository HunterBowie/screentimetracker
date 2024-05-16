import datetime
import json

import matplotlib.dates as pltdates
import matplotlib.pyplot as plt
import numpy

import util


def format_screen_time_data(data: list[list[str, str, str]]) -> list[list[datetime.date, str, int]]:
    new_data = []
    for row in data:
        new_row = []
        for col in row:
            if row.index(col) == 0:
                new_row.append(util.convert_str_to_date(col))
            elif row.index(col) == 2:
                new_row.append(int(col))
            else:
                new_row.append(col)
        new_data.append(new_row)
    return new_data


def load_screen_time_data() -> None:
    with open('data/screen_time.csv', 'r') as file:
        data = file.read()
        data = data.split('\n')
        data = [row.split(',') for row in data]
        data = [[item.strip() for item in row] for row in data]
        data.pop(0)
        data = format_screen_time_data(data)
        return data


def format_graph(x_values: list, y_values: list, graph: plt.Axes) -> None:
    graph.xaxis.set_major_locator(plt.MaxNLocator(6))
    graph.xaxis.set_major_formatter(pltdates.DateFormatter('%b %d'))
    graph.set_ylim(bottom=0, top=600)
    graph.set_xlim(left=x_values[0], right=x_values[-1])


def main():
    screen_time_data = load_screen_time_data()
    screen_time_categories = json.load(open('data/categories.json', 'r'))
    all_dates = sorted(set([row[0] for row in screen_time_data if row[0]]))
    all_screen_time_usage = [0 for i in range(len(all_dates))]
    netflix_screen_time_usage = all_screen_time_usage.copy()
    youtube_screen_time_usage = all_screen_time_usage.copy()
    current_date = screen_time_data[0][0]
    position = 0
    for date, label, usage in screen_time_data:
        if current_date != date:
            current_date = date
            position += 1
        if label == 'youtube':
            youtube_screen_time_usage[position] = usage
        elif label == 'netflix':
            netflix_screen_time_usage[position] = usage
        all_screen_time_usage[position] += usage

    fig, (netflix_graph, youtube_graph) = plt.subplots(2, 1)

    plt.subplots_adjust(hspace=.70)

    fig.canvas.manager.set_window_title('Screen Time Data')

    format_graph(all_dates, netflix_screen_time_usage, netflix_graph)
    netflix_graph.plot(all_dates, netflix_screen_time_usage)
    netflix_graph.axvspan(all_dates[0], all_dates[9], color='green', alpha=0.3)
    netflix_graph.axvspan(all_dates[9], all_dates[len(
        all_dates)-1], color='yellow', alpha=0.3)
    netflix_graph.set_title('Netflix Usage (per day)')
    netflix_graph.set_xlabel('Date')
    netflix_graph.set_ylabel('Usage (minutes)')
    netflix_graph.axhline(y=numpy.average(netflix_screen_time_usage),
                          color='r', linestyle='--', label='Average')

    format_graph(all_dates, all_screen_time_usage, youtube_graph)
    youtube_graph.plot(all_dates, all_screen_time_usage)
    youtube_graph.axvspan(all_dates[0], all_dates[9], color='green', alpha=0.3)
    youtube_graph.axvspan(all_dates[9], all_dates[len(
        all_dates)-1], color='yellow', alpha=0.3)
    youtube_graph.set_title('All Screen Time Usage (per day)')
    youtube_graph.set_xlabel('Date')
    youtube_graph.set_ylabel('Usage (minutes)')
    youtube_graph.axhline(y=numpy.average(all_screen_time_usage),
                          color='r', linestyle='--', label='Average')

    # plt.plot(all_dates, all_screen_time_usage)
    # plt.axvspan(all_dates[0], all_dates[9], color='green', alpha=0.3)
    # plt.axvspan(all_dates[9], all_dates[len(
    #     all_dates)-1], color='yellow', alpha=0.3)

    # plt.title('Screen Time Usage (per day)')
    # plt.xlabel('Date')
    # plt.ylabel('Usage (minutes)')

    plt.show()


if __name__ == '__main__':
    main()
