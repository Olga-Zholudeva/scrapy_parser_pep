import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        """Создаем словарь, чтобы сложить в него данные по статусам."""

        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        """Обрабатываем данные по статусам для выгрузки в таблицу."""

        status = item["status"]
        self.statuses[status] = self.statuses.get(status, 0) + 1
        if not status:
            raise KeyError
        return item

    def close_spider(self, spider):
        """Сохраняем данные по статусам PEP в таблицу."""

        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f"results/status_summary_{now_formatted}.csv/"
        file_path = BASE_DIR / file_name
        with open(file_path, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Статус", "Количество"])
            writer.writerows(self.statuses.items())
            total = sum(self.statuses.values())
            writer.writerow(["Total", total])
