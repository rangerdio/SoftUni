from artifacts.renaissance_artifact import RenaissanceArtifact
from artifacts.contemporary_artifact import ContemporaryArtifact
from collectors.museum import Museum
from collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    def __init__(self):
        self.artifacts = []
        self.collectors = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        pass

    def register_collector(self, collector_type: str, collector_name: str):
        pass

    def perform_purchase(self, collector_name: str, artifact_name: str):
        pass

    def remove_artifact(self, artifact_name: str):
        pass

    def fundraising_campaigns(self, max_money: float):
        pass

    def get_auction_report(self):
        pass
