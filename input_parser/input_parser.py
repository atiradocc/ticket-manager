import yaml


class InputParser:
    def __init__(self, input_file):
        self.input_file = input_file

    def parse_input(self):
        with open(self.input_file, "r") as file:
            data = yaml.safe_load(file)

        summary = data.get("Summary", "")
        reporter = data.get("Reporter", "")
        compliance_mapping = data.get("Compliance Mapping", "")
        provider = data.get("Provider", "")
        short_title = data.get("Short Title", "")
        pillar = data.get("Pillar", "")
        risk_level = data.get("Risk Level", "")
        description = data.get("Description", "")
        rationale = data.get("Rationale", "")
        success_criteria = data.get("Success Criteria", "")
        failure_criteria = data.get("Failure Criteria", "")
        epic_link = data.get("Epic Link", "")

        return {
            "summary": summary,
            "reporter": reporter,
            "compliance_mapping": compliance_mapping,
            "provider": provider,
            "short_title": short_title,
            "pillar": pillar,
            "risk_level": risk_level,
            "description": description,
            "rationale": rationale,
            "success_criteria": success_criteria,
            "failure_criteria": failure_criteria,
            "epic_link": epic_link,
        }
