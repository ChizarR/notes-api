from typing import Any, NamedTuple, Dict


class ApiRespose(NamedTuple):
    ok: bool
    description: str
    result: Any | None = None

    def to_dict(self) -> Dict:
        response = {
            "ok": self.ok,
            "description": self.description,
            "result": self.result,
        }
        return response
