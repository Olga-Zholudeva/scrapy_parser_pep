import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        """Парсим ссылки на страницы PEP и вызываем для них обработчик."""

        pep_links = response.css("section#numerical-index tr a::attr(href)")
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Парсим данные со страниц PEP."""

        _, number, _, *name = response.css("h1.page-title::text").get().split()
        data = {
            "number": number,
            "name": " ".join(name),
            "status": response.css("abbr::text").get(),
        }
        yield PepParseItem(data)
