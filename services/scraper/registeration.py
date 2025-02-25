from enum import Enum, auto
from typing import Final

from models.plan_origin import PlanOrigin
from scrapers.arte_scraper import ArteScraper
from scrapers.cajhtp_scraper import CAJHTPScraper
from scrapers.cshs_scraper import CSHSScraper, Scraper
from scrapers.geocenter_scraper import GeocenterScraper
from scrapers.greenschool_scraper import GreenSchoolScraper
from scrapers.hcc_scraper import HCCScraper
from scrapers.hnjh_scraper import HNJHScraper
from scrapers.moe_scraper import MoeScraper
from scrapers.shareclass_scraper import ShareClassScraper
from scrapers.sportsbox_scraper import SportsboxScraper


class Origin(Enum):
    # 臺灣藝術教育網
    ARTE = auto()
    # 媒體素養教育資源網
    MOE = auto()
    # 體育課程與教育資源網
    SPORTSBOX = auto()
    # 國立竹山高級中學
    CSHS = auto()
    # 桃園市立興南國民中學
    HNJH = auto()
    # 108科技領域資訊科技新課綱與素養導向資源分享
    CAJHTP = auto()
    # 教育部地理學科中心 - 教學資源
    GEOCENTER = auto()
    # 新竹市教育處國民教育輔導團
    HCC = auto()
    # ShareClass - 均一教育平台
    SHARECLASS = auto()
    # 教育部綠色學校夥伴網路
    GREENSCHOOL = auto()

    def create_scraper(self) -> Scraper:
        return scraper_factory[self]()


scraper_factory: Final[dict] = {
    Origin.ARTE: lambda: ArteScraper(Origin.ARTE.name),
    Origin.MOE: lambda: MoeScraper(Origin.MOE.name),
    Origin.SPORTSBOX: lambda: SportsboxScraper(Origin.SPORTSBOX.name),
    Origin.CSHS: lambda: CSHSScraper(Origin.CSHS.name),
    Origin.HNJH: lambda: HNJHScraper(Origin.HNJH.name),
    Origin.CAJHTP: lambda: CAJHTPScraper(Origin.CAJHTP.name),
    Origin.GEOCENTER: lambda: GeocenterScraper(Origin.GEOCENTER.name),
    Origin.HCC: lambda: HCCScraper(Origin.HCC.name),
    Origin.SHARECLASS: lambda: ShareClassScraper(Origin.SHARECLASS.name),
    Origin.GREENSCHOOL: lambda: GreenSchoolScraper(Origin.GREENSCHOOL.name),
}


Origins: Final[PlanOrigin] = [
    PlanOrigin(
        id=Origin.ARTE.name,
        name="臺灣藝術教育網",
        url="https://ed.arte.gov.tw/ch/index.aspx",
        logo="https://ed.arte.gov.tw/ch/images/favicon.ico",
    ),
    PlanOrigin(
        id=Origin.MOE.name,
        name="媒體素養教育資源網",
        url="https://mlearn.moe.gov.tw/",
        logo="https://mlearn.moe.gov.tw/lib/Images/favicon.ico",
    ),
    PlanOrigin(
        id=Origin.SPORTSBOX.name,
        name="體育課程與教育資源網",
        url="https://sportsbox.sa.gov.tw/",
        logo="",
    ),
    PlanOrigin(
        id=Origin.CSHS.name,
        name="國立竹山高級中學 > 教學資源下載",
        url="http://www.cshs.ntct.edu.tw/editor_model/u_editor_v1.asp?id={24EFC3E4-4286-4080-841D-8F9389C6212E}",
        logo="http://www.cshs.ntct.edu.tw/mediafile/1449/news_editor/254/pic/0001.bmp",
    ),
    PlanOrigin(
        id=Origin.HNJH.name,
        name="桃園市立興南國民中學",
        url="http://www2.hnjh.tyc.edu.tw/index.php",
        logo="https://upload.wikimedia.org/wikipedia/zh/d/d4/Hsing_Nan_Junior_High_Schoo_Logol.gif",
    ),
    PlanOrigin(
        id=Origin.CAJHTP.name,
        name="108科技領域資訊科技新課綱與素養導向資源分享",
        url="http://www.cajh.tp.edu.tw/tech/",
        logo="http://www.cajh.tp.edu.tw/tech/img/profile.jpg",
    ),
    PlanOrigin(
        id=Origin.GEOCENTER.name,
        name="教育部地理學科中心-教學資源 > 分享類 > 性平課程教學教材",
        url="https://sites.google.com/view/geocenter/教學資源",
        logo="",
    ),
    PlanOrigin(
        id=Origin.HCC.name,
        name="新竹市教育處國民教育輔導團",
        url="https://guide.hcc.edu.tw/index.php",
        logo="",
    ),
    PlanOrigin(
        id=Origin.SHARECLASS.name,
        name="ShareClass - 均一教育平台",
        url="https://www.shareclass.org/",
        logo="https://www.junyiacademy.org/favicon-32x32.png?v=20190827",
    ),
    PlanOrigin(
        id=Origin.GREENSCHOOL.name,
        name="教育部綠色學校夥伴網路 > 資源分享 > 教案(材)分享專區",
        url="https://www.greenschool.moe.edu.tw/",
        logo="https://www.greenschool.moe.edu.tw/gs2/x/img/icon.png",
    ),
]
