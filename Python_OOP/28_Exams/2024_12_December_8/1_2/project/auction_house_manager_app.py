from artifacts.renaissance_artifact import RenaissanceArtifact
from artifacts.contemporary_artifact import ContemporaryArtifact
from collectors.museum import Museum
from collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    def __init__(self):
        self.artifacts = []
        self.collectors = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type == "RenaissanceArtifact":
            artifact = RenaissanceArtifact(artifact_name, artifact_price, artifact_space)
        elif artifact_type == "ContemporaryArtifact":
            artifact = ContemporaryArtifact(artifact_name, artifact_price, artifact_space)
        else:
            return "Invalid artifact type!"

        self.artifacts.append(artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type == "Museum":
            collector = Museum(collector_name)
        elif collector_type == "PrivateCollector":
            collector = PrivateCollector(collector_name)
        else:
            return "Invalid collector type!"

        self.collectors.append(collector)
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = next((c for c in self.collectors if c.name == collector_name), None)
        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)

        if not collector or not artifact:
            return "Invalid collector or artifact name!"

        if collector.can_purchase(artifact.price, artifact.space_required):
            collector.available_money -= artifact.price
            collector.available_space -= artifact.space_required
            collector.purchased_artifacts.append(artifact)
            self.artifacts.remove(artifact)
            return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."
        return "Purchase is impossible."

    def remove_artifact(self, artifact_name: str):
        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)

        if artifact:
            self.artifacts.remove(artifact)
            return f"Removed {artifact.artifact_type}: {artifact.name}; Price: {artifact.price:.2f}; Required space: {artifact.space_required}"
        return "No such artifact."

    def fundraising_campaigns(self, max_money: float):
        count = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                count += 1
        return f"{count} collector/s increased their available money."

    def get_auction_report(self):
        total_sold = sum(len(c.purchased_artifacts) for c in self.collectors)
        available_artifacts = len(self.artifacts)

        report = [
            "**Auction statistics**",
            f"Total number of sold artifacts: {total_sold}",
            f"Available artifacts for sale: {available_artifacts}",
            "***"
        ]

        for collector in sorted(self.collectors, key=lambda c: (-len(c.purchased_artifacts), c.name)):
            artifacts_names = ', '.join(sorted(
                [a.name for a in collector.purchased_artifacts], reverse=True
            )) or "none"

            report.append(
                f"Collector name: {collector.name}; Money available: {collector.available_money:.2f}; "
                f"Space available: {collector.available_space}; Artifacts: {artifacts_names}"
            )

        return "\n".join(report)
