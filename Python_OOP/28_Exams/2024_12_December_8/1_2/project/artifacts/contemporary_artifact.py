from project.artifacts.base_artifact import BaseArtifact


class ContemporaryArtifact(BaseArtifact):
    artifact_type = "Contemporary Artifact"  # Class attribute

    def __init__(self, name: str, price: float, space_required: int):
        super().__init__(name, price, space_required)

    def artifact_information(self):
        return f"{self.artifact_type}: {self.name}, Price: ${self.price:.2f}, Space Required: {self.space_required} sq ft"
